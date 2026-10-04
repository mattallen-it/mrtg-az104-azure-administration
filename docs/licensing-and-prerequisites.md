# Licensing and service prerequisites

## Decision

**Series baseline: retain Entra Free; do not purchase paid Entra or Microsoft 365 user licenses or activate trials for this series.** Lab 06 validated administrator-assisted password recovery, password-change and sign-in evidence, audit review, and active-user cleanup using this baseline. The original live end-user SSPR exercise requires an eligible license. This is a review of all 32 current README scopes, not a guarantee for implementations that have not yet been designed.

Entra Free is already part of the Azure environment. Azure subscription charges, Entra user licenses, operating-system/software rights, and service-tier requirements are separate. “No Entra Premium required” does not mean “free lab.”

## Lab-by-lab review

| Lab | Scope | Entra Premium dependency / other prerequisites |
|---|---|---|
| 01 | [Subscription Inventory and Cost Baseline](../labs/lab-01-subscription-inventory-and-cost-baseline/README.md) | Subscription, budget, tags; no premium identity feature. |
| 02 | [Resource Organization and Management Hierarchy](../labs/lab-02-resource-organization-and-management-hierarchy/README.md) | Resource groups, tags, management hierarchy. |
| 03 | [Employee and contractor lifecycle](../labs/lab-03-employee-and-contractor-lifecycle/README.md) | Manual lifecycle and assigned security groups; no Lifecycle Workflows. |
| 04 | [Scoped administration](../labs/lab-04-scoped-administration/README.md) | Ordinary Azure RBAC; no PIM. |
| 05 | [Guardrails with policy and locks](../labs/lab-05-guardrails-with-policy-and-locks/README.md) | Azure Policy and locks. |
| 06 | [Password reset and account recovery operations](../labs/lab-06-password-recovery-and-licensing/README.md) | Administrator-assisted reset of a cloud-created non-admin user; no paid user-license purchase planned. SSPR remains excluded. |
| 07 | [Access review and cost review](../labs/lab-07-access-review-and-cost-review/README.md) | Manual role/membership review; automated Entra Access Reviews would require eligible P2/Governance licensing. |
| 08 | [Address plan and subnets](../labs/lab-08-address-plan-and-subnets/README.md) | VNet/subnet planning; resource charges depend on deployed test workloads. |
| 09 | [Traffic permissions](../labs/lab-09-traffic-permissions/README.md) | NSG/ASG rules and traffic tests. |
| 10 | [Peering and route investigation](../labs/lab-10-peering-and-route-investigation/README.md) | Peering/routes; peering and traffic may incur charges. |
| 11 | [Name resolution and application availability](../labs/lab-11-name-resolution-and-application-availability/README.md) | DNS/load balancer/backend workloads incur service charges. |
| 12 | [Private access and administrator entry](../labs/lab-12-private-access-and-administrator-entry/README.md) | Endpoints and administrator access; private endpoints/Bastion/VPN have their own pricing. Avoid adding Entra Private Access without license review. |
| 13 | [Storage baseline and transfer](../labs/lab-13-storage-baseline-and-transfer/README.md) | Storage capacity, operations and transfer costs. |
| 14 | [Data access boundaries](../labs/lab-14-data-access-boundaries/README.md) | Azure data roles, SAS, revocation and keys. |
| 15 | [Recover an accidental document deletion](../labs/lab-15-recover-an-accidental-document-deletion/README.md) | Versions, soft deletion and retained data can increase storage charges. |
| 16 | [Department file access and the AD bridge](../labs/lab-16-department-file-access-and-the-ad-bridge/README.md) | Conditional infrastructure dependency: choose AD DS, Entra Domain Services or Entra Kerberos; validate clients, identity sync and licensing before deployment. P1 alone does not create a domain. |
| 17 | [Replication and storage incident drill](../labs/lab-17-replication-and-storage-incident-drill/README.md) | Two storage accounts, replication and network costs. |
| 18 | [Reproducible MRTG deployment](../labs/lab-18-reproducible-mrtg-deployment/README.md) | ARM/Bicep needs no premium identity license; deployed resources cost money. |
| 19 | [VM lifecycle](../labs/lab-19-vm-lifecycle/README.md) | VM/disks and managed identity; managed identities have no license requirement. Review OS image terms. |
| 20 | [Disk recovery and relocation](../labs/lab-20-disk-recovery-and-relocation/README.md) | VM disks and snapshots; retained snapshots are chargeable. |
| 21 | [Availability and scale](../labs/lab-21-availability-and-scale/README.md) | Scale-set instances, disks and load-balancing costs. |
| 22 | [Container delivery](../labs/lab-22-container-delivery/README.md) | Registry, container compute and application service costs; choose images with appropriate licenses. |
| 23 | [Managed web application](../labs/lab-23-managed-web-application/README.md) | App Service plan and networking features; no premium identity feature specified. |
| 24 | [Controlled application release](../labs/lab-24-controlled-application-release/README.md) | Deployment slots require Standard, Premium or Isolated App Service plan; Free/Basic won't fulfill the slot test. |
| 25 | [Logs and operational questions](../labs/lab-25-logs-and-operational-questions/README.md) | Azure resource logs/KQL need service budgeting. Entra Free audit/sign-in retention is seven days; Graph activity logs require P1/P2. Choose log categories explicitly. |
| 26 | [Actionable alerts](../labs/lab-26-actionable-alerts/README.md) | Azure Monitor alert rules, notifications and log usage may incur charges. |
| 27 | [Network incident response](../labs/lab-27-network-incident-response/README.md) | Network Watcher/Connection Monitor and telemetry charges. |
| 28 | [Backup with a proven restore](../labs/lab-28-backup-with-a-proven-restore/README.md) | Backup protected instances, storage, retention and restored resources. |
| 29 | [Regional recovery exercise](../labs/lab-29-regional-recovery-exercise/README.md) | Tabletop design has no premium identity dependency; live recovery incurs replication/recovery resource costs. |
| 30 | [Joiner, mover, leaver across services](../labs/lab-30-joiner-mover-leaver-across-services/README.md) | Manual assigned-group membership, Azure RBAC and data access; exclude licensed Lifecycle Workflows, PIM and dynamic user groups. |
| 31 | [MRTG Azure operations capstone](../labs/lab-31-mrtg-azure-operations-capstone/README.md) | Reuse reviewed components; recheck any added premium identity or OS features. |
| 32 | [Independent Rebuild and Operations Handover](../labs/lab-32-rebuild-review-and-exam-readiness/README.md) | Same component dependencies as the rebuilt workload; no blanket all-products license. |

The classification is an engineering inference from the published scope and the official feature prerequisites below. Planned scopes are brief; deployment design, region availability, quotas, roles, software terms and current prices must be checked before execution.

## Features that would change the decision

| Feature | Licensing implication | Series decision |
|---|---|---|
| Ordinary users/groups and Azure RBAC | No premium feature specified in the current exercises | Assigned security groups and ordinary role assignments |
| Cloud-only forgotten-password SSPR | Eligible Microsoft 365 Business Standard/Business Premium or Entra P1/P2; license intended beneficiaries | Excluded from live scope; Lab 06 uses administrator assistance |
| Hybrid password writeback | Entra P1/P2 or Microsoft 365 Business Premium | Not implemented |
| Conditional Access | Entra P1; risk-based policies require P2 | Not required by current scopes |
| Dynamic user group membership | P1 coverage for each unique user in dynamic groups | Use assigned memberships |
| PIM | Entra P2 or eligible Governance licensing | Not required |
| Automated Access Reviews | P2 covers certain existing capabilities; advanced capabilities need Governance | Lab 07 is manual review |
| Lifecycle Workflows | Governance licensing; P2 alone is insufficient | Lab 30 uses manual administration |
| Managed identities for Azure resources | No managed-identity license requirement | Suitable for Lab 19 |
| Graph activity logs | P1/P2; storage/analytics destination also required | Not required for basic Azure resource KQL exercises |

Do not buy one license and assume it covers every beneficiary. Scope and license the users involved according to the feature's rules. A tenant-wide control being technically accessible does not establish licensing entitlement.

## Lab 16: decision still needed

Azure Files supports multiple identity sources, and enabling identity authentication on the storage account has no extra service charge. A functioning identity source and compatible clients are still necessary. AD DS means domain controllers, connectivity and identity synchronization for user-specific share permissions; Entra Domain Services means a separate managed-domain service; Entra Kerberos has its own identity/client prerequisites. These are not interchangeable with buying P1.

Before Lab 16, choose a supported path and estimate storage, client/VM and directory costs. Verify Windows/Windows Server rights for chosen images and devices. If identity-based SMB cannot be implemented within the budget, explicitly separate tested share/snapshot work from an untested identity design.

## Monitoring and service tiers

Free Entra audit/sign-in history is seven days, compared with 30 days for P1/P2. Capture evidence promptly. The current Azure Monitor integration article lists Azure subscription, permissions and workspace prerequisites; it does not establish a blanket P1 requirement for all diagnostic export. Individual categories differ, particularly Graph activity logs. Basic Azure resource telemetry must not be confused with premium identity reporting.

Lab 24's slot test requires a supported paid App Service tier. Bastion, private endpoints, backup and live regional recovery also require service-specific cost estimates. Buying Entra Premium does not pay for any of those services.

## Operating rule

Keep Entra Free for the current revised series. Design every remaining lab to fit this baseline. Premium identity features are study/design topics, not required live exercises. If a feature cannot be demonstrated without a new user-license purchase, replace that portion with a supported hands-on alternative or explicitly labeled design assessment; do not claim the original feature was tested. Before each deployment, check the exact feature, eligible identity/license, Azure SKU/region, expected runtime, retained storage and cleanup path. Do not add Conditional Access, dynamic user groups, PIM, automated Access Reviews, Lifecycle Workflows, Microsoft 365 workloads or premium identity logs as required live tasks. A future change to the license baseline requires an explicit scope decision from the author. Trial eligibility and checkout terms were not verified; no purchase or trial was activated.

## Official references

- [SSPR licensing](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing)
- [Microsoft Entra licensing and managed identities](https://learn.microsoft.com/en-us/entra/fundamentals/licensing)
- [Dynamic membership licensing](https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-membership)
- [Governance licensing](https://learn.microsoft.com/entra/id-governance/licensing-fundamentals)
- [Azure Files identity sources](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)
- [App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)
- [Entra log retention](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-reports-data-retention)
- [Entra logs and Azure Monitor](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs)
- [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/)

[Lab portfolio](progress.md)
