# Lab 27 evidence gallery

**21 published screenshots.**

November 25, 2026 America/Chicago; later CLI timestamps use November 26 UTC. Reviewed author-supplied originals; the creation image masks the subscription ID. Configuration, observed outcomes and evidence limits are distinguished.

[Lab results](../README.md)

## 1. preflight subscription quota

Subscription enabled, existing Network Watcher and available regional/family quota.

![Subscription enabled, existing Network Watcher and available regional/family quota.](lab27-preflight-subscription-quota.png)

## 2. vm sku check

B2s restricted; B2s_v2 restrictions empty.

![B2s restricted; B2s_v2 restrictions empty.](lab27-vm-sku-check.png)

## 3. network subnets

Client and app subnet provisioning Succeeded.

![Client and app subnet provisioning Succeeded.](lab27-network-subnets.png)

## 4. vms deployed

Both B2s_v2 VMs running at the expected private addresses; key paths contain no key material.

![Both B2s_v2 VMs running at the expected private addresses; key paths contain no key material.](lab27-vms-deployed.png)

## 5. app setup command

Run Command setup script for Nginx and the synthetic application response.

![Run Command setup script for Nginx and the synthetic application response.](lab27-app-setup-command.png)

## 6. app install and local validation

Nginx installation, active state and successful localhost response.

![Nginx installation, active state and successful localhost response.](lab27-app-install-and-local-validation.png)

## 7. baseline client to app

Client private-IP HTTP baseline returned 200 at 23:02:23Z.

![Client private-IP HTTP baseline returned 200 at 23:02:23Z.](lab27-baseline-client-to-app.png)

## 8. monitoring prerequisites

Workspace and both Network Watcher extensions Succeeded.

![Workspace and both Network Watcher extensions Succeeded.](lab27-monitoring-prerequisites.png)

## 9. connection monitor test config

TCP 80, 30-second frequency, 10% failed-check and 100 ms RTT thresholds.

![TCP 80, 30-second frequency, 10% failed-check and 100 ms RTT thresholds.](lab27-connection-monitor-test-config.png)

## 10. connection monitor test group

Corrected individual client and app VM endpoints; enabled extensions.

![Corrected individual client and app VM endpoints; enabled extensions.](lab27-connection-monitor-test-group.png)

## 11. connection monitor workspace

Custom law-mrtg-lab27 workspace selected in Central US.

![Custom law-mrtg-lab27 workspace selected in Central US.](lab27-connection-monitor-workspace.png)

## 12. connection monitor review

Corrected review; portal banner USD 0 versus row USD 0.3/month are estimates, not session spend.

![Corrected review; portal banner USD 0 versus row USD 0.3/month are estimates, not session spend.](lab27-connection-monitor-review.png)

## 13. connection monitor created

Connection Monitor created under NetworkWatcherRG with the intended workspace; subscription ID masked by author.

![Connection Monitor created under NetworkWatcherRG with the intended workspace; subscription ID masked by author.](lab27-connection-monitor-created.png)

## 14. connection monitor healthy baseline

Green TCP baseline, zero failed checks and 2.22 ms RTT.

![Green TCP baseline, zero failed checks and 2.22 ms RTT.](lab27-connection-monitor-healthy-baseline.png)

## 15. fault injected client timeout

Priority-200 deny rule Succeeded; client HTTP 000 and curl timeout exit 28.

![Priority-200 deny rule Succeeded; client HTTP 000 and curl timeout exit 28.](lab27-fault-injected-client-timeout.png)

## 16. diagnosis nsg deny app healthy

IP flow names Deny-Client-HTTP while Nginx remains active with localhost HTTP 200.

![IP flow names Deny-Client-HTTP while Nginx remains active with localhost HTTP 200.](lab27-diagnosis-nsg-deny-app-healthy.png)

## 17. connection monitor fault detected

Red test and 53.5% failed checks over a mixed one-hour window.

![Red test and 53.5% failed checks over a mixed one-hour window.](lab27-connection-monitor-fault-detected.png)

## 18. recovery ip flow and http200

After rule removal, IP flow Allow and client HTTP 200.

![After rule removal, IP flow Allow and client HTTP 200.](lab27-recovery-ip-flow-and-http200.png)

## 19. connection monitor recovered

Post-correction 8:05–8:07 PM window: green, zero failures, 2.61 ms RTT.

![Post-correction 8:05–8:07 PM window: green, zero failures, 2.61 ms RTT.](lab27-connection-monitor-recovered.png)

## 20. cleanup verified

Lab group exists=false and zero matching monitors after separate monitor/group deletion.

![Lab group exists=false and zero matching monitors after separate monitor/group deletion.](lab27-cleanup-verified.png)

## 21. Cost follow-up — November 26, 2026

November 2026 billing-account view filtered to rg-mrtg-lab27-network: Actual USD 0.69; VMs USD 0.62, Virtual Network USD 0.04, Storage USD 0.03, Bandwidth below USD 0.01 and Log Analytics USD 0.00. Author-redacted screenshot; rounded posted snapshot, not final billing. The separately stored NetworkWatcherRG monitor is outside this filter.

![November 26 posted cost for the lab resource group: USD 0.69.](lab27-cost-review-2026-11-26.png)
