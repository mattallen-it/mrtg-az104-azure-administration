# Repository maintenance

This repository documents the author's MRTG Azure labs. Completed lab records contain implementation details, observed results, sanitized evidence, and cleanup. Planned pages do not claim execution.

Documentation checks run with:

```bash
python3 scripts/check_docs.py
```

The checker validates relative Markdown file/image links, merge-conflict markers, top-level headings, and final newlines. It does not validate external URLs, anchors, rendering, sensitive information, or Azure behavior.
