# Lab 25 query and configuration evidence

[Lab results](../README.md) · [Screenshot gallery](../screenshots/README.md)

| Query | Saved result | Purpose |
|---|---|---|
| [01-event-summary.kql](01-event-summary.kql) | [JSON](01-event-summary-results.json) | Count target events by operation/status |
| [02-failed-operation.kql](02-failed-operation.kql) | [JSON](02-failed-operation-results.json) | Parse ScopeLocked and retain failure correlation |
| [03-event-timeline.kql](03-event-timeline.kql) | [JSON](03-event-timeline-results.json) | Order eight events and compare caller fingerprints |
| [04-caller-claims-check.kql](04-caller-claims-check.kql) | [JSON](04-caller-claims-check-results.json) | Compare token object claim fingerprint with signed-in user lookup |
| [05-delete-recovery.kql](05-delete-recovery.kql) | [JSON](05-delete-recovery-results.json) | Retain failed and successful delete outcomes |

[export-setting.json](export-setting.json) retains the setting name and category flags; it does not retain the workspace destination ID. [workspace-config.json](workspace-config.json) retains name, location, SKU and configured retention. Destination comparison and cleanup are separate screenshot observations.

[SHA256SUMS](SHA256SUMS) covers these 12 original files. All entries were verified against the extracted files before publication. [lab25-evidence.zip](lab25-evidence.zip) is the original byte-identical bundle, including its manifest. Its SHA-256 is `63bb688ec19555ffe20cb3e4d0e6c2bfbd2fcd819de7eff5f2e66a58993759ee`. This README was added for navigation and is outside the original manifest.

Queries use a relative `ago(2h)` window and were executed with CLI PT2H. Their saved JSON captures historical observations; later execution requires an appropriate historical time range and available retained data. Twelve-character hash prefixes pseudonymize identity values for comparison; they do not provide complete anonymization. Raw caller values, IP addresses, tokens and bulk claims are not part of these selected exports. Correlation IDs remain for request grouping.
