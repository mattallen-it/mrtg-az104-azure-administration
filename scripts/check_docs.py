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
    return files, errors

if __name__ == '__main__':
    files, errors = check(ROOT)
    for error in errors:
        print(error)
    print(f'Checked {len(files)} Markdown files; {len(errors)} issue(s).')
    sys.exit(bool(errors))
