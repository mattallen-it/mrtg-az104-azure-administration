# Lab 27 — Network incident response

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

[Portfolio](../../README.md) · [All labs](../../docs/progress.md) · [Evidence gallery](screenshots/README.md)

## Outcome

Validated a private client-to-application connection, a controlled NSG denial, Network Watcher diagnosis and verified recovery. Client HTTP returned **200 → timeout / 000 → 200**. IP flow verify identified **Deny-Client-HTTP**, then returned Allow after its removal. Connection Monitor showed healthy, failed and recovered states. Cleanup returned resource-group existence=false and zero matching connection monitors.

Executed November 25, 2026 America/Chicago; the later CLI timestamps fall on November 26 UTC. Twenty reviewed screenshots preserve setup, observed tests and cleanup. Final attributable cost remains unverified.

## Business problem

MRTG operations must distinguish an unreachable application from a stopped application service. A network access change can block users while the server remains healthy. Establish a working baseline, identify the enforcing rule, correct that rule and verify recovery from the client and monitoring perspectives.

## Environment and decisions

| Component | Configuration |
|---|---|
| Subscription and region | MRTG-AZ104-Lab-Subscription; Central US |
| Disposable resource group | rg-mrtg-lab27-network |
| VNet | vnet-mrtg-lab27; 10.27.0.0/16 |
| Client subnet and VM | snet-client, 10.27.1.0/24; vm-mrtg-lab27-client, 10.27.1.4 |
| App subnet and VM | snet-app, 10.27.2.0/24; vm-mrtg-lab27-app, 10.27.2.4 |
| Compute | Two Standard_B2s_v2 Ubuntu2204 VMs; Standard LRS 32 GiB OS disks requested |
| Administration and egress | Azure Run Command; generated SSH keys, but no SSH session tested; named Standard public IPs requested for egress; --nsg-rule NONE |
| Network controls | Separate NIC NSGs nsg-mrtg-lab27-client and nsg-mrtg-lab27-app requested by deployment; existing VNet default allow used for baseline |
| Test application | Nginx, HTTP port 80; synthetic response MRTG Lab 27 - application healthy |
| Diagnostic extensions | AzureNetworkWatcherExtension on both VMs, publisher Microsoft.Azure.NetworkWatcher, NetworkWatcherAgentLinux 1.4 requested; both Succeeded |
| Workspace | law-mrtg-lab27; Central US; PerGB2018, 30-day retention requested; Succeeded |
| Connection Monitor | cm-mrtg-lab27-client-app; Central US, stored under NetworkWatcherRG; custom workspace law-mrtg-lab27 |
| Test group and configuration | tg-client-to-app; tcp-app-80; individual client and app VM endpoints; TCP 80 every 30 seconds; failed-check threshold 10%, RTT threshold 100 ms; Listen on port unchecked |
| Controlled fault | App NSG inbound Deny-Client-HTTP, priority 200, TCP, source 10.27.1.4/32, any source port, destination 10.27.2.4/32:80 |
| Requested tags | Environment=Lab, Project=MRTG-AZ104-Administration, Lab=Lab-27, Owner=MRTG-Cloud-Operations |

Preflight showed the subscription Enabled, an existing NetworkWatcher_centralus in NetworkWatcherRG, regional usage 0/16 vCPUs and Bsv2 usage 0/6. Standard_B2s was restricted for this subscription/location; Standard_B2s_v2 returned an empty restrictions list and subsequently deployed successfully. This is historical availability evidence, not a capacity reservation.

## Work performed

1. Checked subscription, existing group/Network Watcher state, quota and SKU restrictions. Created the tagged lab group and two subnets; both subnets showed Succeeded.
2. Deployed the two VMs at the expected private addresses; both showed VM running and Succeeded. Installed Nginx on the app through Run Command and wrote the synthetic response. Local HTTP passed, then the client private-IP request returned 200.
3. Installed Network Watcher extensions on both VMs and created the dedicated workspace. Replaced initial subnet selections with individual VM endpoints and selected the custom workspace instead of the default before creation. The submitted archive retains the corrected configuration.
4. Created Connection Monitor and captured the healthy TCP baseline. Added the narrowly targeted NSG deny rule and verified a fresh client request timed out. Connection Monitor later showed a failed test.
5. Ran inbound IP flow verify against the app at 10.27.2.4:80 with remote client 10.27.1.4:60000. Azure identified securityRules/Deny-Client-HTTP. During the same fault, Nginx remained active and localhost HTTP returned 200.
6. Removed only the fault rule. IP flow verify returned Allow via defaultSecurityRules/AllowVnetInBound; a new client request returned 200. A post-correction monitoring window showed green status and zero failed checks.
7. Deleted the connection monitor separately from NetworkWatcherRG, then deleted the disposable lab group. Verified group absence and zero matching monitors in Central US.

## Validation results

| Stage | Evidence time / window | Observed result |
|---|---|---|
| Client baseline | 2026-11-25 23:02:23Z | Synthetic healthy response; HTTP 200 |
| Monitor baseline | November 25, 6:23–7:28 PM portal window | Green, 0% failed checks; RTT 2.22 ms |
| Fault command | 2026-11-26 01:30:39Z, immediately before rule creation | Deny rule priority 200, Succeeded; timestamp is command start, not measured enforcement time |
| Client fault test | 2026-11-26 01:31:06Z | HTTP 000; curl exit 28; connection timeout after approximately 5001 ms |
| Rule diagnosis | During fault | IP flow verify: Deny, securityRules/Deny-Client-HTTP |
| Server health | 2026-11-26 01:33:25Z | Nginx active; localhost synthetic response and HTTP 200 |
| Monitor fault | Last 1 hour selected | Red, 53.5% failed checks; mixed healthy/fault window, not 100% loss throughout the hour |
| Rule removal and policy readback | 2026-11-26 02:04:14Z after deletion command | Allow via defaultSecurityRules/AllowVnetInBound |
| Client recovery | 2026-11-26 02:04:41Z | Synthetic healthy response; HTTP 200 |
| Monitor recovery | November 25, 8:05–8:07 PM portal window | Green, 0% failed checks; RTT 2.61 ms |
| Cleanup | Final named checks | rg-mrtg-lab27-network exists=false; matching connection monitor count=0 |

The rule diagnostic evaluates the specified packet against network security rules; the independent client curl establishes actual application reachability. Remote port 60000 is a representative diagnostic source port, not an exported port from the failed curl connection. The fault rule matched any source port.

## Troubleshooting and lessons

Quota and SKU availability are separate checks. Selecting B2s_v2 after inspecting restrictions avoided treating the available older BS-family quota as a guarantee that B2s could deploy.

The portal initially selected whole subnets and a default workspace. Selecting the individual VMs and law-mrtg-lab27 kept the monitored path and data destination aligned with the exercise. The archive contains the corrected test group, workspace and review screens, not the discarded intermediate selections. Private-IP choices were made during setup; no independent endpoint JSON export was retained.

A successful Run Command invocation means the management action ran; it does not mean curl succeeded. During the fault, the wrapper reported Enable succeeded while curl timed out with exit 28. Local HTTP 200 and the named NSG denial distinguished service health from network admission.

The monitor's one-hour failure percentage includes earlier healthy checks. The recovery window was narrowed to exclude the fault period; it demonstrates sampled recovery for that short window, not a long-term availability SLA. No exact detection delay or continuous outage duration was measured.

## Cleanup and costs

The final script separately deleted cm-mrtg-lab27-client-app in Central US before deleting rg-mrtg-lab27-network. The named existence check returned false and the regional monitor list contained zero matching names. The existing Network Watcher and NetworkWatcherRG were retained; unrelated resources were not audited. Group deletion covers the contained VM, disk, NIC, public IP, NSG, VNet and workspace resources, but a separate per-child post-deletion inventory and permanent workspace purge were not captured. Cloud Shell generated SSH key files; their subsequent removal was not verified.

Two VMs, managed disks, Standard public IPs and monitoring/log ingestion can incur charges. The creation review displayed a USD 0 banner but USD 0.3 estimated monthly cost in the test-group row. These inconsistent portal estimates are not measured session spend, and neither represents the combined compute/network/logging cost. No Cost Analysis screenshot or machine-readable cost export was supplied. Attributable posted usage, final billing, credit application and cash spend remain unverified; do not record zero cost. See the [cost ledger](../../docs/cost-ledger.md).

No paid Entra or Microsoft 365 user license or trial was introduced. The existing subscription, directory, shared Network Watcher and administrator context were retained; the budget was not revalidated in this exercise.

## Evidence and limits

[Twenty reviewed screenshots](screenshots/README.md) preserve the supplied filenames and image bytes. The supplied created-state image has the subscription ID masked. No private-key content, password or access token was found in the reviewed package; the VM command capture includes key file paths, not key material. SHA256SUMS.txt records the packaged screenshot hashes for integrity checks, not proof of Azure authenticity.

The exercise validates one synthetic private TCP/HTTP path with a controlled NSG fault. No DNS fault, route fault, packet capture, KQL investigation, TLS, application authentication, managed identity, least-privilege administrator test or external-source denial was performed. SSH key generation does not establish SSH access. Deployment commands request no inbound SSH rule, but a full effective-rule inventory or external-port scan was not retained. No original ARM/Bicep deployment, endpoint export, raw monitoring records or independent incident timeline export is included. The table above is reconstructed from visible evidence, not a production incident record. No alert notification or automated remediation was tested.

Official references: [Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-create-using-portal), [IP flow verify](https://learn.microsoft.com/en-us/azure/network-watcher/diagnose-vm-network-traffic-filtering-problem), [Network Watcher agent](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-agent-manage), [Linux Run Command](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/run-command).
