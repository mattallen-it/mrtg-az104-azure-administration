# Lab 08 — Address plan and subnets

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

**Completed:** October 6, 2026. **Status:** Validated — address configuration, portal overlap validation, and cleanup.

## Business problem

MRTG needs a clear address plan for future Operations and Security workloads. This exercise establishes separate subnet ranges and tests how the portal handles an overlapping proposal before workloads are introduced.

## Environment and address plan

Subscription: `MRTG-AZ104-Lab-Subscription`. Resource group: `rg-mrtg-lab08-network`. Region: Central US.

| Component | Name | CIDR | Address range |
|---|---|---|---|
| Virtual network | `vnet-mrtg-lab08` | `10.80.0.0/16` | 10.80.0.0–10.80.255.255 |
| Operations subnet | `snet-operations` | `10.80.10.0/24` | 10.80.10.0–10.80.10.255 |
| Security subnet | `snet-security` | `10.80.20.0/24` | 10.80.20.0–10.80.20.255 |
| Rejected proposal | `snet-overlap-test` | `10.80.10.128/25` | 10.80.10.128–10.80.10.255 |

Tags: Environment = Lab; Project = MRTG-AZ104-Administration; Lab = Lab-08; Owner = MRTG-Cloud-Operations.

Both subnets were configured with private subnet enabled (no default outbound access). NAT gateway, network security group, route table, and delegation were set to None; service endpoints were unselected. The deployment review showed Bastion, Firewall, and DDoS Network Protection disabled. No compute workloads were deployed.

## Work performed and validation

1. Created the tagged resource group and captured its empty resource list.
2. Replaced the wizard's default address plan with `10.80.0.0/16` and configured the two /24 subnets.
3. Reviewed validation and settings, deployed the VNet, and captured successful deployment and resource overview.
4. Inspected the deployed subnet list: both intended CIDRs appeared, each with 251 available IPs and no attached NSG, route table, or delegation.
5. Proposed `10.80.10.128/25`. The portal displayed an overlap error naming `10.80.10.0/24` and stating that subnets in the same VNet cannot overlap.
6. Closed the unsaved proposal and refreshed. Only the two original subnets remained with unchanged CIDRs.
7. Verified that the lab resource group contained only the VNet, deleted the group, and captured the final unfiltered resource-group list.
8. Reviewed October subscription costs after cleanup: Actual cost displayed `--` with “No cost reported during this period.”

## Evidence

All 13 screenshots are preserved with consistent filenames. Configuration and review screens establish intended settings; deployment and resource screens establish the deployed state.

| # | Screenshot | Checkpoint |
|---|---|---|
| 1 | [lab08-final-cost-review.png](screenshots/lab08-final-cost-review.png) | Final subscription cost review |
| 2 | [lab08-operations-subnet-configuration.png](screenshots/lab08-operations-subnet-configuration.png) | Operations subnet configuration |
| 3 | [lab08-overlapping-subnet-rejected.png](screenshots/lab08-overlapping-subnet-rejected.png) | Overlapping subnet validation error |
| 4 | [lab08-resource-group-cleanup.png](screenshots/lab08-resource-group-cleanup.png) | Unfiltered resource-group cleanup |
| 5 | [lab08-resource-group-created.png](screenshots/lab08-resource-group-created.png) | Tagged resource group created |
| 6 | [lab08-resources-before-cleanup.png](screenshots/lab08-resources-before-cleanup.png) | Resources before cleanup |
| 7 | [lab08-security-subnet-configuration.png](screenshots/lab08-security-subnet-configuration.png) | Security subnet configuration |
| 8 | [lab08-subnets-unchanged-after-rejection.png](screenshots/lab08-subnets-unchanged-after-rejection.png) | Subnets unchanged after rejected overlap |
| 9 | [lab08-subnets-verified.png](screenshots/lab08-subnets-verified.png) | Deployed subnet list |
| 10 | [lab08-vnet-address-configuration.png](screenshots/lab08-vnet-address-configuration.png) | VNet address configuration |
| 11 | [lab08-vnet-created.png](screenshots/lab08-vnet-created.png) | Created VNet overview |
| 12 | [lab08-vnet-deployment-complete.png](screenshots/lab08-vnet-deployment-complete.png) | Deployment completed |
| 13 | [lab08-vnet-review.png](screenshots/lab08-vnet-review.png) | Validated deployment review |

## Cleanup and retained state

The final unfiltered list no longer contained `rg-mrtg-lab08-network`; only `NetworkWatcherRG` remained. Its contents were not inspected. The lab VNet and its subnets were removed with their resource group.

## Findings and evidence limits

The attempted /25 lies entirely inside the Operations /24. The captured result is portal validation of an unsaved proposal, not a submitted deployment failure.

Separate subnet ranges establish address organization, not a tested traffic security boundary. No NSG rules, packet flows, internet connectivity, peering, routing behavior, or identity access tests were performed in this lab. Private subnet configuration was captured; outbound behavior was not tested.

The final cost view records the subscription's reported state at capture time. It does not prove a final $0 bill, remaining credits, or a current budget alert. No paid Entra or Microsoft 365 license or trial was used.

## Next lab

[Lab 09 — Traffic permissions](../lab-09-traffic-permissions/README.md) extends the network work into traffic controls.

[All labs](../../docs/progress.md) · [Architecture](../../docs/architecture.md) · [Cost ledger](../../docs/cost-ledger.md)
