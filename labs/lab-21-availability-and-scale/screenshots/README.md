# Lab 21 evidence gallery

**17 published screenshots.**

Supplied PNG bytes are preserved unchanged. All 52 supplied captures were reviewed. This gallery contains the 17 images accepted for upload so far; the other 35 remain pending after automatic approval review rejected some image uploads as unverified. The author-reviewed cost image hides billing identity. No credential or private-key contents are included.

| Capture | What it establishes and limits |
|---|---|
| [lab21-autoscale-cpu-load-instance-049f759a.png](lab21-autoscale-cpu-load-instance-049f759a.png) | Run Command on 049f759a: transient all-core load active; runtime bounded at 1200 seconds. |
| [lab21-autoscale-cpu-load-instance-99ce2d52.png](lab21-autoscale-cpu-load-instance-99ce2d52.png) | Run Command on 99ce2d52: transient load active; Running as unit on stderr is informational. |
| [lab21-autoscale-cpu-load-stopped-049f759a.png](lab21-autoscale-cpu-load-stopped-049f759a.png) | Stop/status check shows inactive; does not distinguish timeout from explicit stop timing. |
| [lab21-autoscale-cpu-load-stopped-99ce2d52.png](lab21-autoscale-cpu-load-stopped-99ce2d52.png) | Second load unit inactive after stop/status check; no visible stderr. |
| [lab21-autoscale-cpu-scale-in-rule.png](lab21-autoscale-cpu-scale-in-rule.png) | CPU average <30%, 10-minute duration, decrease 1, 5-minute cooldown; rule editor capture. |
| [lab21-autoscale-cpu-scale-out-rule.png](lab21-autoscale-cpu-scale-out-rule.png) | CPU average >70%, 5-minute duration, increase 1, 5-minute cooldown; rule editor capture. |
| [lab21-autoscale-policy-saved.png](lab21-autoscale-policy-saved.png) | Saved generated policy name Autoscale-396, two rules, min/default 2, max 3; predictive off. |
| [lab21-autoscale-save-provider-registration-error.png](lab21-autoscale-save-provider-registration-error.png) | Save rejected with MissingSubscriptionRegistration for Microsoft.Insights; failed intermediate state. |
| [lab21-autoscale-scale-out-and-in-succeeded.png](lab21-autoscale-scale-out-and-in-succeeded.png) | Both autoscale events Succeeded; observed capacity 2 → 3 → 2; local timestamps 20:40:23 and 21:01:23. |
| [lab21-autoscale-scale-out-succeeded.png](lab21-autoscale-scale-out-succeeded.png) | Autoscale scale-up Succeeded, observed count rose to 3; before later scale-in. |
| [lab21-cost-review-2026-11-16.png](lab21-cost-review-2026-11-16.png) | Author-redacted November billing-account view filtered to lab group: USD 0.34 Actual; rounded service breakdown, not final invoice. |
| [lab21-lb-backend-pool-two-instances.png](lab21-lb-backend-pool-two-instances.png) | Initial two backend NIC members, private IPs 10.210.10.4/5 and zones 2/1; Running is VM state, not probe health. |
| [lab21-lb-http-after-autoscale-scale-in.png](lab21-lb-http-after-autoscale-scale-in.png) | 20 post-autoscale responses from SCSKHA and DG1WO2, no visible curl errors; sampled after completion. |
| [lab21-lb-http-after-scale-in.png](lab21-lb-http-after-scale-in.png) | 30 post-manual-scale-in responses from 1A6D22 and SCSKHA; removed T8EIPL absent. |
| [lab21-lb-http-both-backends-restored.png](lab21-lb-http-both-backends-restored.png) | 20 frontend requests include both original hostnames after service restoration. |
| [lab21-lb-http-both-backends.png](lab21-lb-http-both-backends.png) | 20 separate initial curl requests include both original hostnames; not a throughput benchmark. |
| [lab21-lb-http-first-response.png](lab21-lb-http-first-response.png) | Browser HTTP page through historical public frontend; T8EIPL hostname returned; HTTP is unencrypted. |


The intermediate Basics screenshot is not the final VM size. Final review and deployed instance lists show Standard_B2ts_v2. The first restart check is intentionally retained despite its failed immediate curl; the later local and frontend checks establish recovery. Autoscale events and sampled traffic do not prove zero downtime, a zone outage, external-source denial, or final billing.

[Lab results](../README.md) · [Portfolio](../../../README.md)
