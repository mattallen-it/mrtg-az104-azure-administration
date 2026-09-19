# Lab 01 — Subscription Inventory and Cost Baseline

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4)
![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)
![Deployment and configuration](https://img.shields.io/badge/Lab-Deployment%20and%20configuration-555555)

## Objective

Establish a usable Azure subscription for MRTG administration labs with verified access, a spending baseline, budget notifications, and a tested resource-group cleanup process.

In this lab, I:

- Investigated the missing subscription and confirmed the previous subscription was deleted.
- Created a new subscription and verified Active status and Owner access.
- Configured and verified a $10 monthly budget with actual and forecast alerts.
- Created an empty resource group using MRTG naming and tagging conventions.
- Manually deleted the group and verified cleanup.

## Business Problem Solved

Monroe Redstone Technology Group needed a controlled starting point for its simulated Azure environment. The previous lab subscription was no longer usable, and deploying workloads without confirming access, ownership, costs, and cleanup responsibilities could create administrative confusion and unexpected charges.

This lab established the subscription and cost-notification baseline before any paid workload deployment. MRTG is a fictional organization; this work was performed in a personal learning environment.

## Scenario

**Lab type: Deployment and configuration.**

I used the existing Entra directory and dedicated MRTG account, upgraded the billing account to pay-as-you-go with Basic support, and created a new Azure subscription. I retained the subscription and monthly budget for later labs. The only resource group created for this exercise was empty and was deleted afterward.

## Azure Services and Resources Used

| Service or resource | Purpose |
|---|---|
| Azure portal | Inspected billing, subscription access, configuration, and cleanup |
| Microsoft Entra ID | Existing identity directory associated with the subscription |
| Azure subscription and Azure RBAC | Established the resource/billing scope and verified Owner access |
| Azure Cost Management budgets | Recorded reported spending and configured notifications |
| Azure resource group | Practiced organization, tagging, and manual lifecycle management |

## Environment

| Item | Value |
|---|---|
| Organization | Monroe Redstone Technology Group — simulated enterprise |
| Project | MRTG Azure Administration |
| Subscription | `MRTG-AZ104-Lab-Subscription` |
| Directory | Existing Default Directory |
| Subscription status / role | Active / Owner |
| Billing plan / support | Pay-as-you-go Azure Plan / Basic |
| Region | Central US |
| Temporary resource group | `rg-mrtg-az104-lab01-centralus-001` |
| Budget | `budget-mrtg-az104-monthly` — USD 10, monthly reset |
| Reported spend at inspection | USD 0.00; not a final invoice |
| Final resource-group state | Temporary group deleted; no groups listed |

### Resource Naming and Tags

Naming pattern: `<type>-mrtg-az104-labNN-centralus-001`.

The temporary resource group used these seven tags:

| Tag | Value |
|---|---|
| Project | MRTG-AZ104-Administration |
| Lab | Lab-01 |
| Environment | Lab |
| Owner | MRTG-Cloud-Operations |
| CostCenter | Training |
| ManagedBy | Azure-Portal |
| DeleteAfter | 2026-09-17 |

The subscription was also tagged with Project, Environment, Owner, CostCenter, and ManagedBy. The DeleteAfter tag recorded the intended cleanup date; it did not perform deletion.

## Steps Performed

Account identifiers and the alert recipient address were masked in the screenshots. Blank areas represent redaction, not missing configuration.

### 1. Investigated the Previous Subscription

The resource-access subscription list was empty. I checked the billing subscription list and found `MRTG-AZ900-Lab-Subscription` with a Deleted status. Microsoft Entra ID Free remained active.

![Previous AZ-900 subscription with Deleted status](screenshots/lab01-old-subscription-deleted.png)

**Validation:** The billing list established the subscription's status. The cause of deletion was not determined.

### 2. Created and Verified the New Subscription

After upgrading the billing account, I created `MRTG-AZ104-Lab-Subscription` in the existing directory with the dedicated MRTG account as subscription owner. I confirmed an empty resource inventory before creating the test group.

![Active AZ-104 subscription with Owner access and reported zero cost](screenshots/lab01-subscription-active-owner.png)

**Validation:** The overview showed Active status, Owner access, and 0.00 reported cost at inspection.

### 3. Corrected and Verified the Monthly Budget

The subscription wizard initially produced an annual budget. Its reset period could not be changed in the edit screen, so I replaced it with `budget-mrtg-az104-monthly`.

| Setting | Saved value |
|---|---|
| Scope | Entire AZ-104 subscription; no filters |
| Amount / reset | USD 10 / Monthly |
| Start / expiration | September 1, 2026 / August 31, 2028 |
| Actual-cost alerts | 50% ($5), 80% ($8), 100% ($10) |
| Forecast-cost alert | 100% ($10) |
| Recipient | Dedicated MRTG email; redacted in public evidence |
| Action groups | None |

![Saved monthly budget with actual and forecast alert thresholds](screenshots/lab01-monthly-budget-alerts.png)

**Validation:** The saved overview confirmed the monthly reset and all four alert conditions. Email delivery and threshold firing were not tested.

### 4. Created the Tagged Resource Group

I configured `rg-mrtg-az104-lab01-centralus-001` in Central US and applied the seven tags listed above.

![Resource-group creation review showing name, region, and seven tags](screenshots/lab01-resource-group-tags.png)

**Validation:** The pre-creation review showed the intended configuration. The deployed overview below confirmed the group actually existed.

### 5. Verified the Group Was Empty

I opened the created group's overview and inspected its resource list.

![Created resource group with no resources listed](screenshots/lab01-resource-group-empty.png)

**Validation:** The group existed in Central US, with no resources listed and the type/location filters set to all.

### 6. Deleted the Temporary Group and Verified Cleanup

I manually deleted only the named temporary group, then refreshed the resource-group list.

![Resource-group list showing no resource groups after cleanup](screenshots/lab01-cleanup-confirmed.png)

**Validation:** The list showed “No resource groups to display.” The subscription and monthly budget were retained.

## Validation

| Check | Expected | Observed result |
|---|---|---|
| Subscription | Active with administrative access | Active; Owner role confirmed |
| Budget period | Monthly | Saved overview showed monthly reset |
| Alerts | Three actual thresholds and one forecast threshold | All four configurations verified; delivery untested |
| Cost baseline | Record current reported spending | USD 0.00 shown; charges may be delayed |
| Resource-group configuration | Intended name, region, and tags | Review showed seven tags; deployed group confirmed |
| Resource inventory | Empty test group | No resources listed |
| Cleanup | Test group removed | No resource groups displayed |
| Understanding | Distinguish identity, billing, alerts, and deletion | Budget misconception corrected; manual deletion understood |
| Public evidence | Readable results with identifiers masked | Six sanitized screenshots published |

The observed operational blocker was the missing usable subscription; the retest showed the new subscription Active with Owner access. No permission-denial test was performed in this inventory exercise.

## IAM and Security Relevance

The lab separated three concepts:

| Concept | Role in this lab |
|---|---|
| Entra tenant | Identity directory containing users, groups, and applications |
| Azure subscription | Resource-management and billing boundary linked to a directory |
| Azure RBAC | Authorization to manage resources at an assigned scope |

Owner access was observed for the lab administrator. This exercise did not demonstrate least-privilege delegation or changes to directory roles. Broad lab ownership should not be presented as a production access model.

## Governance and Cost Decisions

| Decision | Reason |
|---|---|
| Reuse the existing directory | Preserve the identity environment without creating an unnecessary tenant |
| Apply consistent naming and tags | Record purpose, ownership, and cleanup responsibility |
| Set a $10 monthly budget | Provide early spending notifications |
| Retain a separate $100 series allowance | Track total planned cash exposure across multiple months |
| Create only an empty test group | Practice lifecycle management without deploying a paid workload |
| Delete the test group manually | Prove cleanup and avoid abandoned lab objects |

Reported spending was USD 0.00 at inspection. Remaining credit was not verified and is not assumed. No final invoice or measured savings is claimed. Recheck reported charges next session because cost reporting can lag; record results in the [cost ledger](../../docs/cost-ledger.md).

**A budget is an alerting mechanism, not a spending cap.** A running VM can continue generating charges after the budget threshold is reached.

## Troubleshooting Notes

| Issue | Investigation and resolution | Retest |
|---|---|---|
| No subscription in the resource-access list | Checked billing subscriptions; old subscription showed Deleted. Upgraded billing account and created a new subscription. Deletion cause remained unknown. | New subscription showed Active and Owner access |
| Annual budget instead of monthly | Found an annual reset period; could not change it in the edit screen. Replaced the initial budget. | Saved replacement showed monthly reset and all four alerts |

## What I Would Do Differently in Production

- Use approved subscription provisioning and defined billing ownership.
- Assign routine administrative permissions at the narrowest practical scope instead of relying on standing subscription Owner access.
- Establish workload budgets, monitored recipients, and an operational response when alerts arrive.
- Require review of resource ownership and dependencies before deletion.
- Use policy and documented lifecycle procedures where required; descriptive tags alone do not enforce controls.

These are proposed production practices, not controls implemented or tested in this lab.

## Lessons Learned

- An empty resource-access list does not by itself prove that a subscription was deleted.
- A tenant is an identity directory; the Azure portal is the management interface.
- Verify saved budget settings rather than assuming the creation wizard chose the intended period.
- I initially expected a budget to block spending. The corrected understanding is that alerts do not stop running resources or prevent further charges.
- DeleteAfter communicates intent; manual action performed the deletion.

## Cleanup

| Resource or configuration | Final state | Reason |
|---|---|---|
| AZ-104 subscription | Retained | Required for subsequent labs |
| Monthly budget | Retained | Ongoing spending notifications |
| Initial annual budget | Replaced | Did not match monthly tracking requirements |
| Temporary Lab 01 resource group | Deleted and absence verified | Lifecycle exercise complete |
| VMs and other paid workloads | Not deployed | Not required for this lab |

## Outcome and Completion Checklist

The portal baseline and cleanup exercise are validated. MRTG has an active subscription, documented administrative access, a saved monthly budget, and evidence of controlled resource-group creation and removal.

- [x] Confirmed subscription status and role
- [x] Recorded the empty starting inventory and reported cost
- [x] Verified monthly budget and alert configuration
- [x] Created and inspected the tagged test group
- [x] Deleted the group and verified its absence
- [x] Reviewed the tenant/subscription distinction and budget limitations
- [x] Published six sanitized screenshots with captions

**Follow-up:** Alert delivery remains untested. CLI/PowerShell inventory validation was outside this portal-based lab’s scope.


[All labs](../../docs/progress.md)
