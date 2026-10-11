# Lab 09 — Traffic permissions

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Technical validation complete](https://img.shields.io/badge/Status-Technical_validation_complete-2E7D32)

**Status:** Technical testing and resource group cleanup completed on October 10, 2026. Posted cost review remains pending. Screenshot publication is in progress; reviewed batches are linked below.

## Purpose

Restrict client-to-application traffic using application security group (ASG) membership and network security group (NSG) rules, then test access removal and restoration using actual HTTP requests.

## Deployed environment

| Component | Configuration |
|---|---|
| Resource group / region | `rg-mrtg-lab09-traffic` / Central US |
| VNet | `vnet-mrtg-lab09`, `10.90.0.0/16` |
| Client subnet / VM address | `snet-client`, `10.90.10.0/24` / `10.90.10.4` |
| App subnet / VM address | `snet-app`, `10.90.20.0/24` / `10.90.20.4` |
| VMs | Two Ubuntu 24.04 LTS VMs, Standard_B2ts_v2 |
| ASGs | `asg-mrtg-lab09-client` and `asg-mrtg-lab09-app`, assigned to their respective VM NICs |
| NSG placement | `nsg-mrtg-lab09-app` associated with the app subnet; no NIC NSGs |
| Public IP / public inbound ports | None |
| OS disks | Standard SSD LRS |

The initial subnet form enabled private subnets. Before creating the VMs, default outbound access was enabled on both subnets to support Azure VM agent / Run Command communication. This temporary lab choice did not assign public IPs to the VMs; production outbound design was outside the tested scope.

## Inbound policy

| Priority | Rule | Source | Destination | Protocol / port | Action |
|---|---|---|---|---|---|
| 100 | Allow-Client-To-App-TCP-8080 | Client ASG | App ASG | TCP / 8080 | Allow |
| 200 | Deny-Other-Inbound-To-App | Any | App ASG | Any / * | Deny |

The custom deny precedes Azure's default AllowVnetInBound rule. It targets app ASG members, rather than automatically targeting every NIC in the subnet.

## Observed results

Both app services listened on ports 8080 and 8081 and returned HTTP 200 locally. Client tests used fresh Python HTTP requests to the app's private address.

| Client ASG state | TCP 8080 | TCP 8081 |
|---|---|---|
| Member | HTTP 200; expected lab response body | Timed out |
| Membership removed | Timed out | Timed out |
| Membership restored | HTTP 200; expected lab response body | Timed out |

These results validate the tested membership and port boundary. They do not claim every protocol, effective-rule export, Network Watcher flow verification, production hardening, or application authentication was tested. ASG membership controls network reachability; it is not an Entra user authorization mechanism.

## Troubleshooting and cleanup

Legacy VM sizes were unavailable. A Basv2-family quota request was unsuccessful; a Bsv2-family limit increase to four vCPUs succeeded, allowing two two-vCPU B2ts_v2 VMs. Quota approval was allocation permission, not actual usage or a capacity guarantee.

Final deployment reviews corrected unexpected availability-zone and public-IP selections before deployment. Accelerated networking remained enabled because the selected size required it.

The lab resource group and its VMs, disks, NICs, SSH key resources, ASGs, NSG and VNet were deleted. The resource group list subsequently showed only NetworkWatcherRG. No private SSH key files are published.

October Cost analysis showed “No cost reported during this period” and Actual cost `--` after cleanup. This is unreported cost data, not a zero-cost result. The posted VM/disk cost review remains pending.

## Reviewed evidence — batch 1

The following twelve screenshots were visually inspected for personal information and secrets. Duplicate upload suffixes were removed from repository filenames. The app ASG membership and outbound-subnet screenshots use the author's redacted replacements. Generated recreations are not used as evidence.

| Screenshot | Evidence and limits |
|---|---|
| [Alternative VM sizes](screenshots/lab09-alternative-vm-size-review.png) | Size comparison during troubleshooting; monthly estimates are not incurred charges |
| [App ASG review](screenshots/lab09-app-asg-review.png) | Creation validation passed |
| [App ASG created](screenshots/lab09-app-asg-created.png) | Provisioning succeeded; four lab tags visible; initial empty membership |
| [App deny rule configuration](screenshots/lab09-app-deny-rule-configuration.png) | Priority 200 deny form targeting the app ASG |
| [Initial app subnet configuration](screenshots/lab09-app-subnet-configuration.png) | Initial private-subnet form; outbound setting changed later |
| [App subnet outbound configuration](screenshots/lab09-app-subnet-default-outbound-enabled.png) | Edit form shows private-subnet setting unchecked, app NSG selected and no NAT gateway; Subnet ID redacted |
| [App subnet NSG association](screenshots/lab09-app-subnet-nsg-associated.png) | App NSG associated with snet-app |
| [App VM ASG membership](screenshots/lab09-app-vm-asg-membership.png) | App NIC and private IP linked to app ASG; subscription ID redacted |
| [App VM authentication](screenshots/lab09-app-vm-authentication.png) | SSH key generation selection and no public inbound ports; no private key content |
| [App VM advanced configuration](screenshots/lab09-app-vm-advanced-configuration.png) | No extensions, custom data or capacity reservation selected |
| [App Run Command readiness](screenshots/lab09-app-run-command-ready.png) | Hostname, Python 3.12.3 and app private IP |
| [App test services ready](screenshots/lab09-app-test-services-ready.png) | Both listeners active and both local requests return HTTP 200 |

## Reviewed evidence — batch 2

These six app VM screenshots were reviewed for personal information and credentials; the VM overview has its subscription ID redacted.

| Screenshot | Evidence |
|---|---|
| [App VM basics](screenshots/lab09-app-vm-basics.png) | Central US, Ubuntu 24.04 LTS x64, B2ts_v2 and no infrastructure redundancy selected |
| [App VM disk configuration](screenshots/lab09-app-vm-disk-configuration.png) | Standard SSD, platform-managed key, delete with VM enabled and no data disks |
| [App VM management](screenshots/lab09-app-vm-management-configuration.png) | Managed identity, Entra login and auto-shutdown off; image-default patch orchestration |
| [App VM monitoring](screenshots/lab09-app-vm-monitoring-configuration.png) | Managed boot diagnostics enabled; guest diagnostics, recommended alerts and application health monitoring off |
| [App VM deployment complete](screenshots/lab09-app-vm-deployment-complete.png) | Portal confirms successful deployment |
| [App VM created](screenshots/lab09-app-vm-created.png) | Running B2ts_v2 VM, ready agent, private IP 10.90.20.4, no public IP and four lab tags |

Creation-form cost figures are monthly estimates, not the lab's actual charges.

## Reviewed evidence — batch 3

Ten screenshots cleared for publication after privacy review. The upper app VM review uses the author's replacement with its preferred email address redacted.

| Screenshot | Evidence and limits |
|---|---|
| [App VM networking](screenshots/lab09-app-vm-networking-configuration.png) | App subnet selected, public IP and NIC NSG set to None, NIC deletion enabled; accelerated networking required |
| [App VM final review](screenshots/lab09-app-vm-review.png) | B2ts_v2, no infrastructure redundancy, Standard SSD LRS, no public IP, no NIC NSG and accelerated networking on; email redacted |
| [App VM lower review](screenshots/lab09-app-vm-review-networking.png) | NIC deletion enabled, management and monitoring settings reviewed, full tag values visible; tag target labels do not establish deployment of an availability set or public IP |
| [App VM tags](screenshots/lab09-app-vm-tags.png) | Four tag keys selected; Project field truncated here, with full value visible in lower review |
| [B1s unavailable reason](screenshots/lab09-b1s-unavailable-reason.png) | Portal reports NotAvailableForSubscription in Central US |
| [Accelerated networking required](screenshots/lab09-b2ts-v2-accelerated-networking-required.png) | Portal control states the selected size requires accelerated networking |
| [Basv2 quota baseline](screenshots/lab09-basv2-family-quota-baseline.png) | Central US Basv2 family current usage 0 and quota limit 0 |
| [Basv2 quota request pending](screenshots/lab09-basv2-quota-request-pending.png) | Request for family limit 4 under review; not an approval |
| [Basv2 request unsuccessful](screenshots/lab09-basv2-quota-request-unsuccessful.png) | Request unsuccessful; 0 of 4 received; reason not displayed |
| [BS family quota review](screenshots/lab09-bs-family-quota-review.png) | Legacy BS family shows usage 0 of limit 10 and End of Life category; quota does not prove SKU availability |

## Reviewed evidence — batch 4

Eight screenshots cleared for publication. Client ASG removal/restoration overview images use the author's replacements with subscription IDs redacted. The post-restoration HTTP result completes the published access removal/restoration sequence.

| Screenshot | Evidence and limits |
|---|---|
| [Initial client port tests](screenshots/lab09-client-to-app-port-tests.png) | HTTP 200 and expected body on port 8080; port 8081 timed out |
| [Client access after ASG removal](screenshots/lab09-client-without-asg-access-denied.png) | Fresh requests to ports 8080 and 8081 both timed out |
| [Custom NSG inbound rules](screenshots/lab09-nsg-custom-inbound-rules.png) | Priority 100 client-ASG to app-ASG TCP 8080 allow; priority 200 other inbound to app-ASG deny; default rules visible |
| [Resource group cleanup](screenshots/lab09-resource-group-cleanup.png) | Resource group list shows only NetworkWatcherRG; lab resource group absent |
| [Client ASG membership removed](screenshots/lab09-client-asg-membership-removed.png) | Client ASG table empty; subscription ID redacted |
| [Client ASG membership restored](screenshots/lab09-client-asg-membership-restored.png) | Client NIC vm-mrtg-lab09-client333 and private IP 10.90.10.4 linked to client ASG; subscription ID redacted |
| [Client access restored](screenshots/lab09-client-asg-access-restored.png) | After membership restoration, port 8080 returns HTTP 200 and expected body; port 8081 still times out |
| [Cost review after cleanup](screenshots/lab09-final-cost-review.png) | October 2026 subscription scope, no cost reported and Actual cost --; posted charges remain pending |


## Reviewed evidence — batch 5

Nine screenshots cleared after visual privacy review. The client ASG overview and final VM review already contain the author's redactions. Creation-form monthly estimates are not incurred charges.

| Screenshot | Evidence and limits |
|---|---|
| [Bsv2 family quota baseline](screenshots/lab09-bsv2-family-quota-review.png) | Central US usage 0 and family limit 0 before the request |
| [Bsv2 quota request pending](screenshots/lab09-bsv2-quota-request-pending.png) | Requested limit 4 under review; approval not yet granted |
| [Bsv2 quota increase approved](screenshots/lab09-bsv2-quota-increase-approved.png) | Request succeeded, 4 of 4 received and new family limit 4; received quota is not deployed usage |
| [Client ASG review](screenshots/lab09-client-asg-review.png) | Creation validation passed for the client ASG in Central US |
| [Client ASG created](screenshots/lab09-client-asg-created.png) | Provisioning succeeded with four lab tags and initially empty membership; subscription ID redacted |
| [Client VM monitoring](screenshots/lab09-client-vm-monitoring-configuration.png) | Managed boot diagnostics enabled; recommended alerts, guest diagnostics and application health monitoring off |
| [Earlier client VM networking form](screenshots/lab09-client-vm-network-configuration.png) | Client subnet, no public IP or NIC NSG and NIC deletion enabled; accelerated networking was off at this earlier stage and enabled before final deployment |
| [Client VM final review](screenshots/lab09-client-vm-review.png) | B2ts_v2, Ubuntu 24.04 LTS, no infrastructure redundancy, Secure Boot and vTPM enabled, Standard SSD LRS, no public IP or NIC NSG and accelerated networking on; email redacted |
| [Client VM lower review](screenshots/lab09-client-vm-review-networking.png) | Accelerated networking on, NIC deletion enabled, management options off and boot diagnostics on; tag target labels do not prove deployment of an availability set or public IP |

The client VM quota-validation error screenshot is withheld pending redaction of its preferred email address and the subscription ID embedded in the error URL. It documents an earlier Basv2 quota failure, not the final Bsv2 deployment configuration.

Additional client deployment and network configuration screenshots will be linked as their reviewed batches are published.

[All labs](../../docs/progress.md)
