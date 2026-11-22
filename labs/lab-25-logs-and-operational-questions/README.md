# Lab 25 — Logs and operational questions

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

[Portfolio](../../README.md) · [All labs](../../docs/progress.md) · [Evidence gallery](screenshots/README.md)

## Outcome

Exported subscription Administrative Activity Logs to Log Analytics and used five KQL queries to investigate a controlled resource-group deletion failure. The saved records show the preceding writes, a failed delete with `ScopeLocked`, attribution through a matching token object fingerprint, and a successful delete after lock removal. Both lab groups and the export setting were removed. Attributable cost remains unconfirmed.

Executed November 21, 2026 America/Chicago; event timestamps below are November 22 UTC. This is a historical disposable deployment.

## Business problem

MRTG needs an administrator to answer four concrete incident questions: what changed, which identity initiated the failed operation, why it failed, and whether the retry recovered. Configuration alone is insufficient: the investigation must retain query results and distinguish source events, ingestion delay, caller fields and token claims.

## Environment and decisions

| Component | Tested configuration |
|---|---|
| Monitoring group | `rg-mrtg-lab25-logs`, East US 2 |
| Workspace | `law-mrtg-lab25`, PerGB2018, 30-day configured retention |
| Subscription diagnostic setting | `diag-mrtg-lab25-activity`; Administrative enabled; destination ID compared with the workspace ID |
| Controlled target | Separate empty group `rg-mrtg-lab25-target`, East US 2 |
| Guardrail | `lock-lab25-delete`, CanNotDelete |
| Tags | Environment=Lab, Project=MRTG-AZ104-Administration, Lab=Lab-25; target ChangeTicket=LAB25-001 |
| Query scope | `AzureActivity`, target resource group, relative two-hour window |

Microsoft.Insights and Microsoft.OperationalInsights were Registered. Initial workspace and subscription diagnostic-setting lists had no rows. Collection covered subscription-wide Administrative events; target filtering happened in KQL. No VM, Sentinel, Entra premium feature, sign-in-log collection or data-plane logging was introduced. Provisioning used the existing administrator session; minimum permissions were not tested.

## Work performed

1. Created the workspace and subscription export; checked the configured destination against the intended workspace ID.
2. Created the empty target group, updated its ChangeTicket tag and added the delete lock. A delete attempt returned ScopeLocked, and the group still existed.
3. Inspected native Activity Logs, then queried the workspace. An initial target query had no rows; a workspace-wide count showed five older records. A later target query returned the generated events.
4. Saved event summary, failed-operation detail and an ordered timeline. Parsed the failure status message to extract its error code and retained correlation IDs.
5. Compared pseudonymized caller, CLI account and signed-in object values. Because the raw Caller fingerprint differed, checked the failed event's token object claim against the signed-in user object fingerprint.
6. Removed the lock and deleted the target. Repeated the recovery query until both failed and successful deletes were captured.
7. Exported selected configuration, retained the original evidence ZIP and SHA-256 manifest, then removed the subscription export and monitoring group.

The initial pasted guarded command emitted a Bash command-substitution EOF error. That script is not presented as a clean execution. The actual deletion failure is independently supported by the native Activity Log and saved AzureActivity records.

## Validation results

| Question | Observed result |
|---|---|
| Did delivery reach the workspace? | Target-specific results eventually appeared after an earlier empty result; initial workspace count contained five older records |
| What operations preceded failure? | Eight timeline records: two group-write Start/Success pairs, one lock-write Start/Success pair and one delete Start/Failure pair |
| Why did deletion fail? | `Failure`, substatus `Conflict`, parsed error `ScopeLocked` at `2026-11-22T03:11:30.6475455Z` |
| Which request connects its start and failure? | Correlation ID `11187121-9c30-41e3-a403-2774b0dadfa6` |
| Did Caller directly match the CLI account or object? | Caller fingerprint `87d277775c36` differed from the CLI account fingerprint and signed-in object fingerprint |
| Did token claims support attribution? | Failed-event TokenObjectFingerprint `c429cf354885` matched the independently queried signed-in user object fingerprint |
| Did retry recover? | Saved recovery result contains the earlier failure and a Success at `2026-11-22T03:30:46.7957431Z`, correlation ID `cfba7423-48f8-4c48-bd76-951db5d4e1e1` |
| Was cleanup checked? | Target existence=false; final subscription diagnostic-setting list `[]`; monitoring and target group existence both false |
| Were artifacts preserved intact? | All 12 SHA256SUMS entries matched extracted files; JSON results/configuration parsed successfully |

The summary groups the eight timeline events into six operation/status rows. Native Activity Log status names differ from the AzureActivity values; the screenshots and saved results preserve those original representations. Group-write events establish operations, not a complete before/after tag diff.

## Troubleshooting and lessons

Ingestion is asynchronous. The initial empty target result did not prove a broken export: older workspace events existed, and the generated records appeared later. The first recovery query also contained only the failure; the final saved result contains both outcomes. No ingestion SLA was measured.

The CLI installed the preview log-analytics extension after prompting that no stable version was available. That installation output is not query evidence; the published results are the later successful queries.

Caller is not automatically the current CLI username or object ID. The raw Caller mismatch remains unexplained. The token object claim match supports attribution to the signed-in directory object for the failed request; it does not prove which physical person operated the session. Fingerprints are 12 hexadecimal characters of SHA-256 over normalized values. They are pseudonymized comparison aids, not full anonymization or cryptographic identity proof.

CanNotDelete is a management lock, not an RBAC denial. Authorized removal of the lock followed by a successful delete distinguishes the guardrail failure from an unresolved permission problem.

## Cleanup and costs

The lock was removed, the target group deleted and its absence checked before final evidence preservation. The subscription diagnostic setting was deleted; the final list was empty. The monitoring group was deleted, and both group checks returned false. Provider registrations were retained. Unrelated resources and budgets were not re-audited. Workspace permanent purge and irreversible data erasure were not verified.

The November 21 cost-filter search for `rg-mrtg-lab25-logs` returned **No items found**. Background **USD 6.69 Actual** and **USD 9.83 Forecast** are broader billing-scope values, not Lab 25 usage. The East US 2 USD 0.00 tile does not establish this lab's charge. Attributable cost remains unconfirmed; this is not a final invoice or a zero-cost claim. See the [cost ledger](../../docs/cost-ledger.md).

## Evidence and limits

The [gallery](screenshots/README.md) publishes 17 screenshots. The [evidence directory](evidence/README.md) preserves five KQL queries, five result exports, selected export/workspace configuration, the original manifest and the byte-identical evidence ZIP.

Original bundle SHA-256: `63bb688ec19555ffe20cb3e4d0e6c2bfbd2fcd819de7eff5f2e66a58993759ee`.

Queries use `ago(2h)` and CLI PT2H; rerunning them later does not reproduce this historical window automatically. Results are captured observations, not a current inventory. The configuration export omits the destination ID; the separate screenshot records the destination comparison. The recovery result does not contain a separate lock-removal event. No alert notification, action group, automated response, least-privilege role test, sign-in investigation or production compliance certification is claimed. Alerting belongs to Lab 26.
