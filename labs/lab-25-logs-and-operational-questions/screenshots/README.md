# Lab 25 evidence gallery

**19 published screenshots.**

Executed November 21, 2026 America/Chicago; event records use November 22 UTC. Images retain the supplied bytes and filenames.

## 1. monitoring prerequisite check

Provider registration and initial empty workspace/export lists.

![Provider registration and initial empty workspace/export lists.](lab25-monitoring-prerequisite-check.png)

## 2. log analytics workspace created

East US 2 workspace Succeeded, PerGB2018, retention 30 days.

![East US 2 workspace Succeeded, PerGB2018, retention 30 days.](lab25-log-analytics-workspace-created.png)

## 3. activity log export configured

Administrative export enabled; destination comparison verified the intended workspace.

![Administrative export enabled; destination comparison verified the intended workspace.](lab25-activity-log-export-configured.png)

## 4. target change and lock blocked delete

Target tags and CanNotDelete lock; pasted Bash EOF error, actual ScopeLocked failure and group still present. Subscription identifiers are author-redacted.

![Target tags and CanNotDelete lock; pasted Bash EOF error, actual ScopeLocked failure and group still present. Subscription identifiers are author-redacted.](lab25-target-change-and-lock-blocked-delete.png)

## 5. source activity log events

Native Activity Log independently records writes, lock creation and failed delete.

![Native Activity Log independently records writes, lock creation and failed delete.](lab25-source-activity-log-events.png)

## 6. workspace initial ingestion confirmed

Workspace contained five older records before target events appeared; this is an ingestion checkpoint.

![Workspace contained five older records before target events appeared; this is an ingestion checkpoint.](lab25-workspace-initial-ingestion-confirmed.png)

## 7. kql target event summary

Six operation/status summary rows represent eight target events.

![Six operation/status summary rows represent eight target events.](lab25-kql-target-event-summary.png)

## 8. kql failed delete scopelocked

Failure detail: Conflict, ScopeLocked, timestamp, caller fingerprint and correlation ID.

![Failure detail: Conflict, ScopeLocked, timestamp, caller fingerprint and correlation ID.](lab25-kql-failed-delete-scopelocked.png)

## 9. kql event timeline part1

Ordered group-write Start/Success pairs.

![Ordered group-write Start/Success pairs.](lab25-kql-event-timeline-part1.png)

## 10. kql event timeline part2

Lock creation and delete Start/Failure pairs; CLI account fingerprint differs from Caller.

![Lock creation and delete Start/Failure pairs; CLI account fingerprint differs from Caller.](lab25-kql-event-timeline-part2.png)

## 11. signed in object fingerprint check

Independent signed-in user object lookup produces a pseudonymized comparison value.

![Independent signed-in user object lookup produces a pseudonymized comparison value.](lab25-signed-in-object-fingerprint-check.png)

## 12. kql token object attribution verified

Failed-event token object fingerprint matches the signed-in object fingerprint.

![Failed-event token object fingerprint matches the signed-in object fingerprint.](lab25-kql-token-object-attribution-verified.png)

## 13. lock removed target deleted

Lock removal and group deletion commands; target existence=false.

![Lock removal and group deletion commands; target existence=false.](lab25-lock-removed-target-deleted.png)

## 14. kql delete failure and recovery

Final saved recovery query contains both failed and successful deletion outcomes.

![Final saved recovery query contains both failed and successful deletion outcomes.](lab25-kql-delete-failure-and-recovery.png)

## 15. evidence bundle hashes

Manifest and original evidence bundle SHA-256 recorded before cleanup.

![Manifest and original evidence bundle SHA-256 recorded before cleanup.](lab25-evidence-bundle-hashes.png)

## 16. export and resource groups cleaned up

Export deletion, empty diagnostic-setting list and both group checks false.

![Export deletion, empty diagnostic-setting list and both group checks false.](lab25-export-and-resource-groups-cleaned-up.png)

## 17. cost filter no match

Author-redacted cost review: no matching lab group; broader USD 6.69 actual and USD 9.83 forecast are not lab charges.

![Author-redacted cost review: no matching lab group; broader USD 6.69 actual and USD 9.83 forecast are not lab charges.](lab25-cost-filter-no-match.png)

[Lab results](../README.md)

## November 23 cost-filter follow-up: rg-mrtg-lab25-logs

Search returned No items found. Cropped filter capture does not expose the full billing scope or establish zero cost. Review date comes from the author-supplied file/session context.

![November 23 no-match search for rg-mrtg-lab25-logs](lab25-logs-cost-filter-no-match-2026-11-23.png)

## November 23 cost-filter follow-up: rg-mrtg-lab25-target

Search returned No items found. Cropped filter capture does not expose the full billing scope or establish zero cost. Review date comes from the author-supplied file/session context.

![November 23 no-match search for rg-mrtg-lab25-target](lab25-target-cost-filter-no-match-2026-11-23.png)
