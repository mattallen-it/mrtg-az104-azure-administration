# Repository maintenance

This repository documents the author's MRTG Azure labs. Completed lab records contain implementation details, observed results, sanitized evidence, and cleanup. Planned pages do not claim execution.

Documentation checks run with:

```bash
python3 scripts/check_docs.py
```

The checker validates relative Markdown file/image links, merge-conflict markers, top-level headings, and final newlines. It does not validate external URLs, anchors, rendering, sensitive information, or Azure behavior.


## Completed lab format

Labs 01–15 use the same eight level-two headings, in this order:

1. Outcome
2. Business problem
3. Environment and decisions
4. Work performed
5. Validation results
6. Troubleshooting and lessons
7. Cleanup and costs
8. Evidence and limits

Use the shared AZ-104 and Validated badges only after the lab's demonstrated work has supporting evidence. Keep the outcome concise. Preserve the difference between configuration, observed behavior, operator confirmation, and untested assumptions. Use tables for exact settings and test results. Keep one representative screenshot in the results page and the complete file index in `screenshots/README.md`.

Each gallery must index every image in its folder and state the actual count. Keep specific capture notes when a filename or intermediate setting could be misread. Update the main badge, lab index and progress tracker together when a lab's status changes; the checker derives the completed range from that badge. Use [the lab README template](templates/lab-readme.md) for the next completed lab; planned labs must continue to say Planned until execution is evidenced.

The checker also enforces the completed-lab section order, common badges and navigation, complete gallery coverage and counts, and agreement between the validated count and completed index. It flags malformed table rows and skipped heading levels in Labs 01–15. Screenshots and Azure behavior still require human review.
