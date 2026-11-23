# Lab 26 evidence gallery

**24 published screenshots.**

November 22, 2026 America/Chicago. Author-redacted originals; configuration review, sample delivery, actual alerts and cleanup observations are distinguished.

## 1. subscription budget verified

Monthly USD 10 budget; preflight subscription spend/forecast, not lab charges.

![Monthly USD 10 budget; preflight subscription spend/forecast, not lab charges.](lab26-subscription-budget-verified.png)

## 2. budget alert thresholds verified

Actual 50/80/100% and forecast 100%; no action group attached to budget thresholds.

![Actual 50/80/100% and forecast 100%; no action group attached to budget thresholds.](lab26-budget-alert-thresholds-verified.png)

## 3. monitoring and target groups created

Both groups returned Succeeded; displayed paste is not a clean deployment script.

![Both groups returned Succeeded; displayed paste is not a clean deployment script.](lab26-monitoring-and-target-groups-created.png)

## 4. action group review

Global email action group reviewed; no automation actions; tags shown.

![Global email action group reviewed; no automation actions; tags shown.](lab26-action-group-review.png)

## 5. email action group created

Created group and Verified email receiver; address/ID redacted.

![Created group and Verified email receiver; address/ID redacted.](lab26-email-action-group-created.png)

## 6. action group test succeeded

Azure test reports successful Email notification.

![Azure test reports successful Email notification.](lab26-action-group-test-succeeded.png)

## 7. action group test email received

Received synthetic Activity Log sample; not the real target event.

![Received synthetic Activity Log sample; not the real target event.](lab26-action-group-test-email-received.png)

## 8. failed delete alert rule review

Target selection, Failed Administrative deletion and email group attached; enabled upon creation.

![Target selection, Failed Administrative deletion and email group attached; enabled upon creation.](lab26-failed-delete-alert-rule-review.png)

## 9. target delete lock created

CanNotDelete lock creation result.

![CanNotDelete lock creation result.](lab26-target-delete-lock-created.png)

## 10. target delete blocked

Baseline 19:24:24Z attempt; ScopeLocked and true.

![Baseline 19:24:24Z attempt; ScopeLocked and true.](lab26-target-delete-blocked.png)

## 11. real delete alert fired

Baseline real alert, status Failed, suppression None.

![Baseline real alert, status Failed, suppression None.](lab26-real-delete-alert-fired.png)

## 12. real delete alert email received

Received baseline alert email; event ID matches portal instance.

![Received baseline alert email; event ID matches portal instance.](lab26-real-delete-alert-email-received.png)

## 13. suppression processing rule review

Target scope and exact rule-name filter; Suppress notifications, Always, enabled.

![Target scope and exact rule-name filter; Suppress notifications, Always, enabled.](lab26-suppression-processing-rule-review.png)

## 14. suppression test delete blocked

20:06:55Z attempt; ScopeLocked and true.

![20:06:55Z attempt; ScopeLocked and true.](lab26-suppression-test-delete-blocked.png)

## 15. alert fired notifications suppressed

New 2:13 PM Central fired alert explicitly shows Suppressed.

![New 2:13 PM Central fired alert explicitly shows Suppressed.](lab26-alert-fired-notifications-suppressed.png)

## 16. alert rule reenabled

Enabled readback after temporarily disabling the wrong rule.

![Enabled readback after temporarily disabling the wrong rule.](lab26-alert-rule-reenabled.png)

## 17. notification recovery delete blocked

20:57:14Z recovery attempt; ScopeLocked and true.

![20:57:14Z recovery attempt; ScopeLocked and true.](lab26-notification-recovery-delete-blocked.png)

## 18. notification recovery alert fired

New 3:03 PM Central fired alert shows suppression None.

![New 3:03 PM Central fired alert shows suppression None.](lab26-notification-recovery-alert-fired.png)

## 19. notification recovery email received

Received recovery email; structured 21:03 UTC fired time and event ID match portal.

![Received recovery email; structured 21:03 UTC fired time and event ID match portal.](lab26-notification-recovery-email-received.png)

## 20. resource groups cleanup verified

Already absent ResourceGroupNotFound responses, followed by both existence checks false.

![Already absent ResourceGroupNotFound responses, followed by both existence checks false.](lab26-resource-groups-cleanup-verified.png)

## 21. Alert rule accidentally disabled

The detection rule was briefly disabled by mistake; the existing re-enabled capture records its correction before recovery testing.

![Detection rule temporarily Disabled](lab26-alert-rule-accidentally-disabled.png)

## 22. Suppression processing rule disabled

Correct processing rule Disabled before the final notification recovery test; tenant domain is author-redacted.

![Suppression processing rule Disabled](lab26-suppression-rule-disabled.png)

[Lab results](../README.md)

## November 23 cost-filter follow-up: rg-mrtg-lab26-target

Search returned No items found. Cropped filter capture does not expose the full billing scope or establish zero cost. Review date comes from the author-supplied file/session context.

![November 23 no-match search for rg-mrtg-lab26-target](lab26-target-cost-filter-no-match-2026-11-23.png)

## November 23 alerts-group cost review

November 2026 filtered to rg-mrtg-lab26-alerts: Azure Monitor, Global and subscription breakdowns USD 0.00; Actual cost headline --. Displayed service values are not a confirmed final zero total. Billing name is author-redacted.

![November 23 alerts-group cost review](lab26-cost-review-2026-11-23.png)
