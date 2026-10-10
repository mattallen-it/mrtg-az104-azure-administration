# Lab 09 — Traffic permissions

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Technical validation complete](https://img.shields.io/badge/Status-Technical_validation_complete-2E7D32)

**Status:** Technical testing and resource group cleanup completed on October 10, 2026. Posted cost review remains pending. Screenshot publication is in progress; the first reviewed batch is linked below.

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

The following eleven screenshots were visually inspected for personal information and secrets. Duplicate upload suffixes were removed from repository filenames. The app ASG membership screenshot uses the author's redacted replacement. The outbound-subnet screenshot is held until its subscription ID is redacted. Generated recreations are not used as evidence.

| Screenshot | Evidence and limits |
|---|---|
| [Alternative VM sizes](screenshots/lab09-alternative-vm-size-review.png) | Size comparison during troubleshooting; monthly estimates are not incurred charges |
| [App ASG review](screenshots/lab09-app-asg-review.png) | Creation validation passed |
| [App ASG created](screenshots/lab09-app-asg-created.png) | Provisioning succeeded; four lab tags visible; initial empty membership |
| [App deny rule configuration](screenshots/lab09-app-deny-rule-configuration.png) | Priority 200 deny form targeting the app ASG |
| [Initial app subnet configuration](screenshots/lab09-app-subnet-configuration.png) | Initial private-subnet form; outbound setting changed later |
| [App subnet NSG association](screenshots/lab09-app-subnet-nsg-associated.png) | App NSG associated with snet-app |
| [App VM ASG membership](screenshots/lab09-app-vm-asg-membership.png) | App NIC and private IP linked to app ASG; subscription ID redacted |
| [App VM authentication](screenshots/lab09-app-vm-authentication.png) | SSH key generation selection and no public inbound ports; no private key content |
| [App VM advanced configuration](screenshots/lab09-app-vm-advanced-configuration.png) | No extensions, custom data or capacity reservation selected |
| [App Run Command readiness](screenshots/lab09-app-run-command-ready.png) | Hostname, Python 3.12.3 and app private IP |
| [App test services ready](screenshots/lab09-app-test-services-ready.png) | Both listeners active and both local requests return HTTP 200 |

Client traffic, quota, final VM review, membership changes and cleanup screenshots will be linked as their reviewed batches are published.

[All labs](../../docs/progress.md)
