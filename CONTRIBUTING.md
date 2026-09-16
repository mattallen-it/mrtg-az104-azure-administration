# Working on this repository

1. Follow the course mapping and select the applicable lab.
2. Record the starting state, scope, permissions, cost estimate, and cleanup plan.
3. Perform and validate the work using synthetic data.
4. Update the lab README and evidence inventory; use the incident and case-study templates where useful.
5. Update the progress tracker and homepage count only after validation.
6. Run `python scripts/check_docs.py` before committing.
7. Review images, outputs, and scripts for sensitive information.

The checker validates relative Markdown file/image links, merge-conflict markers, missing top-level headings, and final newlines. It ignores fenced code examples and remote URLs. It does not validate URL availability, anchors, reference-style links, Markdown rendering, secrets, or Azure behavior. Manual review remains required.

Keep the homepage concise. Store deep implementation detail in lab READMEs, and link rather than duplicate evidence. Do not mark template checklists completed before work is performed.
