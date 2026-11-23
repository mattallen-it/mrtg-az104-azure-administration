# Lab 26 — Actionable alerts

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

[Portfolio](../../README.md) · [All labs](../../docs/progress.md) · [Evidence gallery](screenshots/README.md)

## Outcome

Validated Azure Monitor email delivery for a real failed resource-group deletion, suppression of notifications while a second alert still fired, and restored delivery after suppression was disabled. The three alert instances show suppression states **None → Suppressed → None**. The target stayed protected by a CanNotDelete lock during all three attempts. Final existence checks returned false for both lab groups.

Executed November 22, 2026 America/Chicago. Twenty-four author-redacted screenshots preserve configuration, sample delivery, real events, recovery and cleanup. A later cost review is documented below; the final total remains unverified.

## Business problem

MRTG operations needs actionable notification of a management failure while retaining alert visibility during a maintenance suppression period. An alert rule detects the condition, an action group delivers notification, and an alert processing rule controls whether actions run. These are separate controls: disabling detection would not demonstrate notification suppression.

## Environment and decisions

| Component | Configuration |
|---|---|
| Subscription | MRTG-AZ104-Lab-Subscription; existing administrator session |
| Monitoring group | rg-mrtg-lab26-alerts; East US 2 group metadata |
| Target group | rg-mrtg-lab26-target; separate empty group, East US 2 |
| Action group | ag-mrtg-lab26-email; Global; display MRTG-L26 |
| Notification | Lab26-Operator-Email; receiver Verified; no automation actions |
| Alert rule | alert-lab26-target-delete-failed; Global; stored in monitoring group, target group selected |
| Condition | Administrative, Microsoft.Resources/subscriptions/resourceGroups/delete, Failed; event level and initiator unrestricted |
| Observed alert severity | Sev4 / Verbose; event level Error |
| Processing rule | apr-lab26-suppress-delete-email; target group scope; exact alert rule name filter; Suppress notifications; Always schedule |
| Target lock | lock-lab26-delete; CanNotDelete |
| Tags on reviewed monitor resources | Environment=Lab, Project=MRTG-AZ104-Administration, Lab=Lab-26, Owner=MRTG-Cloud-Operations |

The exercise used native Activity Logs without a VM, Log Analytics workspace or premium Entra feature. No narrowed administrator role was tested. Common alert schema was selected in the creation flow; the package contains the resulting notification emails rather than an exported receiver configuration.

## Work performed

1. Rechecked the existing monthly USD 10 subscription budget and its 50%, 80% and 100% Actual thresholds plus 100% Forecast threshold. Budget actions showed None; budget email delivery was not tested here.
2. Created monitoring and target groups; both returned Succeeded. Created the email action group, verified its receiver and ran an Activity Log sample test. Azure reported Success and the sample email arrived.
3. Created the enabled failed-deletion alert rule with the email action group attached. Added the target's CanNotDelete lock and attempted deletion; ScopeLocked and existence=true were captured.
4. Verified the first real fired alert and matching email. Created a processing rule to suppress this alert's notifications, allowed propagation, then repeated the blocked deletion. A distinct new alert still fired and reported Suppressed.
5. During recovery, the alert rule was briefly disabled by mistake. It was re-enabled; the processing rule was disabled instead. The final archive retains the alert rule's Enabled readback. After the planned propagation wait, a third blocked deletion produced a new unsuppressed alert and matching email.
6. Ran cleanup commands for the lock and both groups. ResourceGroupNotFound messages indicated groups were already absent at that point; final named existence checks both returned false.

## Validation results

| Stage | Attempt timestamp UTC | Observed fired time | Suppression | Notification |
|---|---|---|---|---|
| Action-group sample | Sample email shows 19:06 UTC | Synthetic test-activityLogAlertRule | Not a live target event | Portal test Success; sample email received |
| Baseline failed delete | 19:24:24Z | Portal 1:28 PM Central; email structured Fired time 19:28 UTC | None | Real rule/target email received |
| Suppression test | 20:06:55Z | Portal 2:13 PM Central | Suppressed | Azure suppression state is the evidence; no inbox absence screenshot |
| Restored notification | 20:57:14Z | Portal 3:03 PM Central; email structured Fired time 21:03 UTC | None | New real email received |

Each deletion attempt returned ScopeLocked and target existence=true. Portal instances contain different event data IDs. Baseline and recovery emails match their respective portal event IDs, supporting the link between each fired instance and received message. Email headline timestamps use a different presentation from the portal; this record uses the structured UTC Fired time and labeled Central portal values, without claiming measured delivery latency.

| Additional check | Evidence |
|---|---|
| Budget retained | Monthly USD 10; evaluated spend USD 6.75, forecast USD 9.89, progress 67.51% at preflight |
| Email receiver | Created action group overview shows Verified |
| Detection restored | Alert rules list shows the original rule Enabled and target rg-mrtg-lab26-target |
| Cleanup state | Target group exists=false; alerts group exists=false |

## Troubleshooting and lessons

A successful action-group sample verifies a delivery path, not the live alert condition. The real locked-delete attempt and matching alert/email establish that condition separately.

Alert rules and alert processing rules serve different purposes. Accidentally disabling the alert rule temporarily stopped detection; restoring its Enabled state was necessary before the final recovery test. The processing-rule Disabled readback and the accidental alert-rule disable are included alongside the later Enabled readback. Recovery is directly evidenced by a new alert with suppression None and its received email. The optional History capture is also absent; the suppression test relies on Azure's explicit Suppressed summary value.

The operator allowed a planned 30-minute window for processing-rule changes before subsequent tests. Exact configuration-change timestamps were not exported, so this is not a measured propagation guarantee. A missing email alone would not prove suppression. Likewise, a rule found through search was not recreated; the final list verified the existing rule enabled.

The target lock is a management guardrail, not a scoped RBAC denial. No unauthorized principal, data-plane operation or identity sign-in failure was tested. Sev4 is the observed alert severity, distinct from the underlying event's Error level; production severity and escalation policy would need deliberate tuning.

## Cleanup and costs

The final commands requested lock removal and deletion of rg-mrtg-lab26-target and rg-mrtg-lab26-alerts. ResourceGroupNotFound was returned for already absent groups, followed by two false existence checks. This establishes final group absence, not the exact earlier deletion time or an independently recorded successful lock-removal operation. The action group, alert rule and processing rule had been placed in the monitoring group. No independent post-deletion inventory of each child resource was captured.

The subscription, administrator and existing USD 10 budget were retained. The budget was revalidated before this lab; earlier records stating it was not revalidated remain historical observations. Its evaluated spend USD 6.75 and forecast USD 9.89 are subscription preflight values, not Lab 26 charges or final cash spend. Budget email recipients were redacted; threshold delivery and automatic spending enforcement were not tested.

The design used an Activity Log alert and a small number of email notifications, with no compute or workspace deployment. Microsoft lists Activity Log alerts at no charge and 1,000 included emails monthly; subscription allowance consumption and final billed costs were not independently verified. The initial package had no Cost Analysis capture; the November 23 follow-up below records the later observation. See the [cost ledger](../../docs/cost-ledger.md).

**Cost follow-up — November 23, 2026:** The [target-group search](screenshots/lab26-target-cost-filter-no-match-2026-11-23.png) returned No items found. A separate author-supplied November 2026 view filtered to rg-mrtg-lab26-alerts displayed Azure Monitor, Global and subscription breakdowns USD 0.00, with Actual cost headline `--`. This is a displayed service-cost observation, not a confirmed final zero total. The [author-redacted full cost screenshot](screenshots/lab26-cost-review-2026-11-23.png) is published.

## Evidence and limits

[Twenty-four published screenshots](screenshots/README.md) retain the supplied filenames and image bytes. Recipient addresses, caller identity fields and subscription IDs are author-redacted. Review screens show intended configuration; later created-state views and actual fired alerts establish observed behavior. The initial group-creation paste contains a malformed-looking echoed line; both Succeeded outputs are retained without claiming the displayed text is a clean reusable script.

No original ARM/Bicep configuration export, alert payload JSON, processing-rule History capture, or machine-readable cost export is included. Suppression applies to notifications; the target failure remained visible. Restoring notification delivery did not resolve the target condition: the lock still blocked deletion until cleanup. Alert acknowledgment, automated remediation, recurrence scheduling, alternate receivers, delivery SLA, least-privilege administration and production compliance were not tested.

Official references: [Action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups), [Activity Log alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log), [Alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules), [Azure Monitor pricing](https://azure.microsoft.com/en-us/pricing/details/monitor/).
