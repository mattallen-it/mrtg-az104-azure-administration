# Lab 09 — Traffic permissions

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

**Status:** Validated. Technical testing and resource group cleanup completed on October 10, 2026; posted cost review completed on October 11. All submitted screenshots have been reviewed and published.

## Purpose

Restrict client-to-application traffic using application security group (ASG) membership and network security group (NSG) rules, then test access removal and restoration using actual HTTP requests.

## Architecture

```mermaid
flowchart TD
  V["VNet 10.90.0.0/16"] --> C["Client subnet 10.90.10.0/24"]
  V --> A["App subnet 10.90.20.0/24"]
  C --> CV["Client VM 10.90.10.4 • Client ASG"]
  A --> AV["App VM 10.90.20.4 • App ASG"]
  CV -->|"TCP 8080 allowed by app-subnet NSG"| AV
```

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

October Cost analysis showed “No cost reported during this period” and Actual cost `--` after cleanup. This is unreported cost data, not a zero-cost result. On October 11, the billing-account Cost analysis view filtered to `rg-mrtg-lab09-traffic` showed USD 0.02 total, Virtual Machines USD 0.02, Storage below USD 0.01 and Bandwidth below USD 0.01. The personal billing-account name is redacted. This is the rounded posted-usage snapshot at review time, not a finalized invoice or cash-payment amount; later reporting can change the total.

## Validation evidence

Published screenshots were visually reviewed for personal information and credentials. Where necessary, the author's redacted replacements hide subscription IDs and email addresses. Filenames omit duplicate upload suffixes. Setup forms, deployed state, troubleshooting and test results are captioned separately.

### Network foundation

| Screenshot | Evidence and limits |
|---|---|
| [Initial app subnet configuration](screenshots/lab09-app-subnet-configuration.png) | Initial private-subnet form; outbound setting changed later |
| [App subnet outbound configuration](screenshots/lab09-app-subnet-default-outbound-enabled.png) | Edit form shows private-subnet setting unchecked, app NSG selected and no NAT gateway; Subnet ID redacted |
| [App subnet NSG association](screenshots/lab09-app-subnet-nsg-associated.png) | App NSG associated with snet-app |
| [Initial client subnet configuration](screenshots/lab09-client-subnet-configuration.png) | 10.90.10.0/24 within 10.90.0.0/16; private subnet initially checked, changed before VM deployment |
| [Client subnet outbound configuration](screenshots/lab09-client-subnet-default-outbound-enabled.png) | Edit form shows private-subnet setting unchecked, 10.90.10.0/24, no NAT gateway, NSG or route table; Subnet ID redacted |
| [Initial deployed subnets](screenshots/lab09-deployed-subnets-verified.png) | Client 10.90.10.0/24 and app 10.90.20.0/24 deployed; no NSG associated at this initial stage |
| [Resource group created](screenshots/lab09-resource-group-created.png) | Central US group with four tags and no deployments; subscription ID redacted |
| [VNet deployment complete](screenshots/lab09-vnet-deployment-complete.png) | Portal confirms successful VNet deployment |
| [Initial VNet review](screenshots/lab09-vnet-review.png) | 10.90.0.0/16 and two /24 subnets, both initially private; Bastion, Firewall and DDoS Network Protection disabled |
| [VNet subnet configuration form](screenshots/lab09-vnet-subnets-configured.png) | Two /24 subnets within the /16; no NAT gateway selected |

### Traffic rules and ASG membership

| Screenshot | Evidence and limits |
|---|---|
| [App ASG review](screenshots/lab09-app-asg-review.png) | Creation validation passed |
| [App ASG created](screenshots/lab09-app-asg-created.png) | Provisioning succeeded; four lab tags visible; initial empty membership |
| [App deny rule configuration](screenshots/lab09-app-deny-rule-configuration.png) | Priority 200 deny form targeting the app ASG |
| [App VM ASG membership](screenshots/lab09-app-vm-asg-membership.png) | App NIC and private IP linked to app ASG; subscription ID redacted |
| [Client access after ASG removal](screenshots/lab09-client-without-asg-access-denied.png) | Fresh requests to ports 8080 and 8081 both timed out |
| [Custom NSG inbound rules](screenshots/lab09-nsg-custom-inbound-rules.png) | Priority 100 client-ASG to app-ASG TCP 8080 allow; priority 200 other inbound to app-ASG deny; default rules visible |
| [Client ASG membership removed](screenshots/lab09-client-asg-membership-removed.png) | Client ASG table empty; subscription ID redacted |
| [Client ASG membership restored](screenshots/lab09-client-asg-membership-restored.png) | Client NIC vm-mrtg-lab09-client333 and private IP 10.90.10.4 linked to client ASG; subscription ID redacted |
| [Client access restored](screenshots/lab09-client-asg-access-restored.png) | After membership restoration, port 8080 returns HTTP 200 and expected body; port 8081 still times out |
| [Client ASG review](screenshots/lab09-client-asg-review.png) | Creation validation passed for the client ASG in Central US |
| [Client ASG created](screenshots/lab09-client-asg-created.png) | Provisioning succeeded with four lab tags and initially empty membership; subscription ID redacted |
| [Client-to-app allow rule form](screenshots/lab09-client-to-app-allow-rule-configuration.png) | Priority 100, client ASG to app ASG, TCP destination 8080, source ports *, Allow |
| [Initial client VM ASG membership](screenshots/lab09-client-vm-asg-membership.png) | Client NIC vm-mrtg-lab09-client333 and private IP 10.90.10.4 linked to client ASG; subscription ID redacted |
| [Default NSG inbound rules](screenshots/lab09-nsg-default-inbound-rules.png) | Initial AllowVnetInBound, AllowAzureLoadBalancerInBound and DenyAllInBound rules before custom rules |

### VM deployment and configuration

| Screenshot | Evidence and limits |
|---|---|
| [App VM authentication](screenshots/lab09-app-vm-authentication.png) | SSH key generation selection and no public inbound ports; no private key content |
| [App VM advanced configuration](screenshots/lab09-app-vm-advanced-configuration.png) | No extensions, custom data or capacity reservation selected |
| [App Run Command readiness](screenshots/lab09-app-run-command-ready.png) | Hostname, Python 3.12.3 and app private IP |
| [App VM basics](screenshots/lab09-app-vm-basics.png) | Central US, Ubuntu 24.04 LTS x64, B2ts_v2 and no infrastructure redundancy selected |
| [App VM disk configuration](screenshots/lab09-app-vm-disk-configuration.png) | Standard SSD, platform-managed key, delete with VM enabled and no data disks |
| [App VM management](screenshots/lab09-app-vm-management-configuration.png) | Managed identity, Entra login and auto-shutdown off; image-default patch orchestration |
| [App VM monitoring](screenshots/lab09-app-vm-monitoring-configuration.png) | Managed boot diagnostics enabled; guest diagnostics, recommended alerts and application health monitoring off |
| [App VM deployment complete](screenshots/lab09-app-vm-deployment-complete.png) | Portal confirms successful deployment |
| [App VM created](screenshots/lab09-app-vm-created.png) | Running B2ts_v2 VM, ready agent, private IP 10.90.20.4, no public IP and four lab tags |
| [App VM networking](screenshots/lab09-app-vm-networking-configuration.png) | App subnet selected, public IP and NIC NSG set to None, NIC deletion enabled; accelerated networking required |
| [App VM final review](screenshots/lab09-app-vm-review.png) | B2ts_v2, no infrastructure redundancy, Standard SSD LRS, no public IP, no NIC NSG and accelerated networking on; email redacted |
| [App VM lower review](screenshots/lab09-app-vm-review-networking.png) | NIC deletion enabled, management and monitoring settings reviewed, full tag values visible; tag target labels do not establish deployment of an availability set or public IP |
| [App VM tags](screenshots/lab09-app-vm-tags.png) | Four tag keys selected; Project field truncated here, with full value visible in lower review |
| [Client VM monitoring](screenshots/lab09-client-vm-monitoring-configuration.png) | Managed boot diagnostics enabled; recommended alerts, guest diagnostics and application health monitoring off |
| [Earlier client VM networking form](screenshots/lab09-client-vm-network-configuration.png) | Client subnet, no public IP or NIC NSG and NIC deletion enabled; accelerated networking was off at this earlier stage and enabled before final deployment |
| [Client VM final review](screenshots/lab09-client-vm-review.png) | B2ts_v2, Ubuntu 24.04 LTS, no infrastructure redundancy, Secure Boot and vTPM enabled, Standard SSD LRS, no public IP or NIC NSG and accelerated networking on; email redacted |
| [Client VM lower review](screenshots/lab09-client-vm-review-networking.png) | Accelerated networking on, NIC deletion enabled, management options off and boot diagnostics on; tag target labels do not prove deployment of an availability set or public IP |
| [Client VM advanced configuration](screenshots/lab09-client-vm-advanced-configuration.png) | No extensions, VM applications, custom data or capacity reservation selected |
| [Client VM created](screenshots/lab09-client-vm-created.png) | Running Ubuntu 24.04 B2ts_v2 VM, ready agent, private IP 10.90.10.4, no public IP, Secure Boot and vTPM enabled; subscription ID redacted |
| [Client VM deployment complete](screenshots/lab09-client-vm-deployment-complete.png) | Portal confirms successful client VM deployment |
| [Client VM disk configuration](screenshots/lab09-client-vm-disk-configuration.png) | Image-default 30 GiB Standard SSD, platform-managed key, delete with VM enabled and no data disks; estimate uses 32 GiB billing tier |
| [Client VM management configuration](screenshots/lab09-client-vm-management-configuration.png) | Managed identity, Entra login, auto-shutdown and periodic assessment off; image-default patch orchestration |
| [Client B2ts_v2 size selection](screenshots/lab09-client-vm-b2ts-v2-size-selection.png) | Selected size has two vCPUs and 1 GiB RAM; displayed monthly compute estimate is not actual cost |
| [Client VM tags](screenshots/lab09-client-vm-tags.png) | Four lab tag keys selected; full Project value confirmed in final review |

### Quota and deployment troubleshooting

| Screenshot | Evidence and limits |
|---|---|
| [Alternative VM sizes](screenshots/lab09-alternative-vm-size-review.png) | Size comparison during troubleshooting; monthly estimates are not incurred charges |
| [B1s unavailable reason](screenshots/lab09-b1s-unavailable-reason.png) | Portal reports NotAvailableForSubscription in Central US |
| [Accelerated networking required](screenshots/lab09-b2ts-v2-accelerated-networking-required.png) | Portal control states the selected size requires accelerated networking |
| [Basv2 quota baseline](screenshots/lab09-basv2-family-quota-baseline.png) | Central US Basv2 family current usage 0 and quota limit 0 |
| [Basv2 quota request pending](screenshots/lab09-basv2-quota-request-pending.png) | Request for family limit 4 under review; not an approval |
| [Basv2 request unsuccessful](screenshots/lab09-basv2-quota-request-unsuccessful.png) | Request unsuccessful; 0 of 4 received; reason not displayed |
| [BS family quota review](screenshots/lab09-bs-family-quota-review.png) | Legacy BS family shows usage 0 of limit 10 and End of Life category; quota does not prove SKU availability |
| [Bsv2 family quota baseline](screenshots/lab09-bsv2-family-quota-review.png) | Central US usage 0 and family limit 0 before the request |
| [Bsv2 quota request pending](screenshots/lab09-bsv2-quota-request-pending.png) | Requested limit 4 under review; approval not yet granted |
| [Bsv2 quota increase approved](screenshots/lab09-bsv2-quota-increase-approved.png) | Request succeeded, 4 of 4 received and new family limit 4; received quota is not deployed usage |
| [Earlier client VM quota validation failure](screenshots/lab09-client-vm-quota-validation-failed.png) | Basv2 quota exceeded in Central US: current family limit 0, usage 0 and two additional vCPUs required; email and subscription-specific URL redacted. This earlier B2ats_v2 form does not represent the final B2ts_v2 deployment configuration. |
| [Client VM form reset](screenshots/lab09-client-vm-form-reset.png) | Troubleshooting snapshot: blank VM name, zone 1 and unavailable D2s_v3 selected; settings restored before deployment, reset cause unconfirmed |
| [Regional vCPU quota baseline](screenshots/lab09-regional-vcpu-quota-baseline.png) | Total Regional vCPUs in Central US shows usage 0 and limit 10; separate from VM-family quota |

### HTTP validation

| Screenshot | Evidence and limits |
|---|---|
| [App test services ready](screenshots/lab09-app-test-services-ready.png) | Both listeners active and both local requests return HTTP 200 |
| [Initial client port tests](screenshots/lab09-client-to-app-port-tests.png) | HTTP 200 and expected body on port 8080; port 8081 timed out |

### Cleanup and cost review

| Screenshot | Evidence and limits |
|---|---|
| [Resource group cleanup](screenshots/lab09-resource-group-cleanup.png) | Resource group list shows only NetworkWatcherRG; lab resource group absent |
| [Cost review after cleanup](screenshots/lab09-final-cost-review.png) | October 2026 subscription scope, no cost reported and Actual cost --; posted charges remain pending |
| [Cost baseline before VMs](screenshots/lab09-cost-before-vms.png) | October subscription scope shows no cost reported, Actual cost -- and forecast unavailable; not a confirmed zero-cost baseline |
| [NSG creation review](screenshots/lab09-nsg-review.png) | Validation passed in Central US with four lab tags |
| [Resources before cleanup](screenshots/lab09-resources-before-cleanup.png) | Twelve lab resources visible: two ASGs, two SSH key resources, NSG, two VMs, two NICs, two OS disks and VNet; subscription ID redacted |
| [Resources removed during cleanup](screenshots/lab09-resources-cleanup-verified.png) | Resource group shows no matching resources with type/location filters set to all; intermediate cleanup state, followed by final group deletion; subscription ID redacted |

| [Posted cost review — October 11](screenshots/lab09-posted-cost-review.png) | October 2026 billing-account view filtered to rg-mrtg-lab09-traffic: USD 0.02 displayed total; VM USD 0.02, Storage and Bandwidth each below USD 0.01. Billing name redacted; posted snapshot, not final invoice. |

## Lessons learned

- Check regional and VM-family quotas separately; a quota increase does not guarantee SKU capacity.
- Review the complete VM form before deployment, including size, zone, public IP and required accelerated networking.
- Apply the app-subnet NSG and both ASG memberships before interpreting traffic tests. Use fresh requests after membership changes.
- Prove both permitted and denied traffic, then prove removal and restoration. Network reachability does not establish user authorization.
- Verify resource group deletion separately from an empty resource list. Review posted charges after cleanup; missing cost data is not zero cost.

[All labs](../../docs/progress.md)
