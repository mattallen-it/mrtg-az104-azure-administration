"""Dependency-free documentation hygiene checks; see CONTRIBUTING.md for limits."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def check(root):
    errors = []
    files = sorted(root.rglob('*.md'))
    for path in files:
        if '.git' in path.parts:
            continue
        text = path.read_text(encoding='utf-8')
        label = path.relative_to(root)
        if not text.endswith('\n'):
            errors.append(f'{label}: missing final newline')
        # Only inspect rendered prose; code examples can contain illustrative paths.
        body = re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1\s*$', '', text)
        if not re.search(r'^#\s+\S', body, re.M):
            errors.append(f'{label}: missing level-one heading')
        if re.search(r'^(<<<<<<< |=======$|>>>>>>> )', body, re.M):
            errors.append(f'{label}: unresolved merge conflict')
        for match in re.finditer(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"\n]*")?\)', body):
            target = match.group(1).strip('<>')
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            relative = unquote(parts.path)
            destination = (root / relative.lstrip('/') if relative.startswith('/') else path.parent / relative).resolve()
            if not destination.is_relative_to(root.resolve()):
                errors.append(f'{label}: link escapes repository: {target}')
            elif not destination.exists():
                errors.append(f'{label}: missing link target: {target}')
    errors.extend(check_portfolio(root))
    return files, errors

LAB_SECTIONS = [
    'Outcome', 'Business problem', 'Environment and decisions', 'Work performed',
    'Validation results', 'Troubleshooting and lessons', 'Cleanup and costs',
    'Evidence and limits',
]

def check_portfolio(root):
    errors = []
    main = (root / 'README.md').read_text(encoding='utf-8')
    badge = re.search(r'Labs_validated-(\d+)_of_32', main)
    if not badge:
        return ['README.md: missing validated-lab count badge']
    completed = int(badge[1])
    if not 1 <= completed <= 32:
        return ['README.md: validated count must be between 1 and 32']
    for number in range(1, completed + 1):
        matches = sorted((root / 'labs').glob(f'lab-{number:02}-*/README.md'))
        if len(matches) != 1:
            errors.append(f'Lab {number:02}: expected one results README')
            continue
        path = matches[0]
        text = path.read_text(encoding='utf-8')
        body = re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1\s*$', '', text)
        label = path.relative_to(root)
        if re.findall(r'^## (.+)$', body, re.M) != LAB_SECTIONS:
            errors.append(f'{label}: completed-lab section order differs from template')
        for expected in ['Exam-AZ--104-0078D4', 'Status-Validated-2E7D32',
                         '[Portfolio](../../README.md)',
                         '[All labs](../../docs/progress.md)',
                         '[Evidence gallery](screenshots/README.md)']:
            if expected not in text:
                errors.append(f'{label}: missing standard badge or navigation: {expected}')
        previous = 0
        for line in body.splitlines():
            heading = re.match(r'^(#{1,6}) ', line)
            if heading:
                level = len(heading[1])
                if level > previous + 1:
                    errors.append(f'{label}: skipped heading level: {line}')
                previous = level
        lines = body.splitlines()
        for index, line in enumerate(lines):
            if not re.match(r'^\|[ :|-]+\|$', line):
                continue
            if index == 0 or not lines[index-1].startswith('|'):
                errors.append(f'{label}: table separator has no header')
                continue
            count = len(re.split(r'(?<!\\)\|', lines[index-1]))
            for row in lines[index:]:
                if not row.startswith('|'):
                    break
                if len(re.split(r'(?<!\\)\|', row)) != count:
                    errors.append(f'{label}: inconsistent table columns: {row}')
        gallery = path.parent / 'screenshots/README.md'
        images = sorted(p.name for p in gallery.parent.iterdir()
                        if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'})
        if not gallery.exists():
            errors.append(f'{label}: missing evidence gallery')
            continue
        content = gallery.read_text(encoding='utf-8')
        if f'**{len(images)} published screenshots.**' not in content:
            errors.append(f'{gallery.relative_to(root)}: screenshot count differs from files')
        for name in images:
            if f']({name})' not in content:
                errors.append(f'{gallery.relative_to(root)}: unindexed image: {name}')
    main = (root / 'README.md').read_text(encoding='utf-8')
    rows = re.findall(r'^\| \[([0-9]{2}) —', main, re.M)
    if rows != [f'{n:02}' for n in range(1, completed + 1)]:
        errors.append(f'README.md: completed index must list 01–{completed:02} once, in order')
    if f'{completed} of 32 labs validated' not in main:
        errors.append('README.md: completed count is inconsistent')
    progress = (root / 'docs/progress.md').read_text(encoding='utf-8')
    if f'{completed}/32 labs validated' not in progress:
        errors.append('docs/progress.md: completed count is inconsistent')
    return errors

if __name__ == '__main__':
    files, errors = check(ROOT)
    for error in errors:
        print(error)
    print(f'Checked {len(files)} Markdown files; {len(errors)} issue(s).')
    sys.exit(bool(errors))

