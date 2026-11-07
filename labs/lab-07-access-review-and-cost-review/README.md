# Lab 07 — Access review and cost review

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

[Portfolio](../../README.md) · [All labs](../../docs/progress.md) · [Evidence gallery](screenshots/README.md)

## Outcome

Replaced an excessive group Contributor assignment with Reader. The reviewer opened the resource group and received AuthorizationFailed on a tag write. Temporary access, identities and resource group were cleaned up.

## Business problem

A synthetic reviewer needed read-only access to a temporary MRTG resource group. A deliberately excessive Contributor assignment was identified during a manual review, removed, and replaced with Reader. The reviewer successfully opened the resource group and received **AuthorizationFailed** when saving a tag.

**Status: validated; temporary role assignment, resource group, security group, and active review user cleaned up.** The evidence below comes from the restarted execution on October 4, 2026.

## Environment and decisions

| Item | Recorded configuration |
|---|---|
| Subscription | MRTG-AZ104-Lab-Subscription |
| Administrator | MRTG Cloud Operations; subscription Owner inherited at resource-group scope |
| Resource group | `rg-mrtg-lab07-access-review`; Central US; empty test scope |
| Review identity | MRTG Lab07 Review User; cloud-only Member |
| Security group | `MRTG-Lab07-Reviewers`; Assigned membership; one direct reviewer member |
| Group owner | MRTG Cloud Operations |
| Tags | Environment = Lab; Project = MRTG-AZ104-Administration; Lab = Lab-07; Owner = MRTG-Cloud-Operations |
| License baseline | Entra Free; no paid Entra/Microsoft 365 license purchase or trial |

Group ownership and group membership were reviewed separately. The Owner tag is metadata; it grants no access. This is a **manual Azure RBAC review**, not the automated Microsoft Entra Access Reviews product.

## Work performed

1. Reviewed October and prior-month September Cost analysis at subscription scope; captured the empty resource-group baseline and existing subscription Owner assignment.
2. Created the tagged empty resource group, enabled synthetic Member user, and Assigned security group.
3. Set the administrator as group owner and added only the reviewer as a direct member.
4. Assigned the group Contributor on the temporary resource group to introduce the controlled excessive-access finding.
5. Compared the assignment with the read-only business requirement. Removed Contributor and assigned Reader to the same group at the same scope.
6. Used resource-group IAM **Check access** for the reviewer; confirmed Reader through the group.
7. Opened a separate reviewer session and loaded the resource group's Overview.
8. Attempted to save `ReviewWriteTest = DeniedExpected` under Tags. Azure rejected the write with **AuthorizationFailed**.
9. Returned to the administrator session, removed the temporary Reader assignment, and verified only inherited Owner remained.
10. Deleted the resource group and security group, then deleted the synthetic user from active users.
11. Rechecked October Cost analysis after cleanup.

## Validation results

### Review finding

| Requirement | Excessive access | Remediation | Observed result |
|---|---|---|---|
| Reviewer reads this resource group | Contributor at resource-group scope | Replace Contributor with Reader through the Assigned security group | Overview loaded; tag write rejected |

The group-derived role check established the assignment path; the reviewer session established actual read and write behavior. Visible portal buttons alone were not treated as proof of permission.

## Troubleshooting and lessons

- Review permissions against a stated business need; a valid assignment can still be excessive.
- Check membership, ownership, assignment scope, and inheritance before changing a role.
- Test both a required action and a prohibited action as the actual user.
- Remove temporary role assignments before deleting their principals and test scope.
- Cost-analysis absence is recorded as absence of reported data, not a verified bill.
- No automated access review, premium identity governance, PIM, storage data access, or role-change audit-log review is claimed.

## Cleanup and costs

### Cleanup and cost result

The role-assignment cleanup capture shows only the original administrator's inherited subscription Owner. The resource-group list is empty, the review-group search returns zero results, and the active-user list contains only the administrator. Permanent user deletion and post-removal session enforcement were not tested.

September and October Cost analysis showed **Actual cost `--`** and **No cost reported during this period**. The final October view showed the same result. No metered workload was deployed. These captures do not establish a finalized $0 invoice, available credits, cumulative cash spend, or continued budget-alert configuration; the cost views show Budget: None.

## Evidence and limits

![Lab 07 validation checkpoint](screenshots/lab07-reviewer-tag-write-denied.png)

**19 published screenshots:** [complete evidence gallery](screenshots/README.md). The gallery indexes every image in this lab’s screenshot folder. Validation applies to the recorded tests and states; it does not establish production hardening or regulatory compliance.

---

[← Lab 06](../lab-06-password-recovery-and-licensing/README.md) · [All labs](../../docs/progress.md) · [Lab 08 →](../lab-08-address-plan-and-subnets/README.md)
