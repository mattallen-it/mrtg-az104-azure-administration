# Lab 07 — Evidence gallery

[Lab results](../README.md) · [Portfolio](../../../README.md) · [All labs](../../../docs/progress.md)

**19 published screenshots.** Configuration forms show intended settings at capture time; deployed-state and test captures support the observed results. Scope, cleanup and evidence limits are recorded in the lab README.

## Screenshot index

| Screenshot | Capture |
|---|---|
| [lab07-cost-baseline.png](lab07-cost-baseline.png) | cost baseline |
| [lab07-excessive-contributor-assignment.png](lab07-excessive-contributor-assignment.png) | excessive contributor assignment |
| [lab07-final-cost-review.png](lab07-final-cost-review.png) | final cost review |
| [lab07-prior-month-cost-review.png](lab07-prior-month-cost-review.png) | prior month cost review |
| [lab07-reader-remediation.png](lab07-reader-remediation.png) | reader remediation |
| [lab07-resource-group-cleanup.png](lab07-resource-group-cleanup.png) | resource group cleanup |
| [lab07-resource-group-created.png](lab07-resource-group-created.png) | resource group created |
| [lab07-resource-groups-baseline.png](lab07-resource-groups-baseline.png) | resource groups baseline |
| [lab07-review-group-cleanup.png](lab07-review-group-cleanup.png) | review group cleanup |
| [lab07-review-group-created.png](lab07-review-group-created.png) | review group created |
| [lab07-review-group-membership.png](lab07-review-group-membership.png) | review group membership |
| [lab07-review-group-owner.png](lab07-review-group-owner.png) | review group owner |
| [lab07-review-user-cleanup.png](lab07-review-user-cleanup.png) | review user cleanup |
| [lab07-review-user-created.png](lab07-review-user-created.png) | review user created |
| [lab07-review-user-effective-access.png](lab07-review-user-effective-access.png) | review user effective access |
| [lab07-reviewer-read-verified.png](lab07-reviewer-read-verified.png) | reviewer read verified |
| [lab07-reviewer-tag-write-denied.png](lab07-reviewer-tag-write-denied.png) | reviewer tag write denied |
| [lab07-role-assignment-cleanup.png](lab07-role-assignment-cleanup.png) | role assignment cleanup |
| [lab07-subscription-access-baseline.png](lab07-subscription-access-baseline.png) | subscription access baseline |

## Capture notes

### Validation evidence


| Evidence | What it proves |
|---|---|
| [October cost baseline](lab07-cost-baseline.png) | Actual cost `--`; no cost reported. |
| [September cost review](lab07-prior-month-cost-review.png) | Prior month also had no reported cost. |
| [Resource group baseline](lab07-resource-groups-baseline.png) | No resource groups displayed before setup. |
| [Subscription access baseline](lab07-subscription-access-baseline.png) | Existing administrator Owner at subscription scope. |
| [Temporary resource group](lab07-resource-group-created.png) | Central US, four tags, no deployments or listed resources. |
| [Synthetic reviewer](lab07-review-user-created.png) | Enabled Member; no licenses or directory roles shown at creation. |
| [Assigned security group](lab07-review-group-created.png) | Cloud security group with Assigned membership. |
| [Group ownership](lab07-review-group-owner.png) | MRTG Cloud Operations is the sole listed owner. |
| [Group membership](lab07-review-group-membership.png) | MRTG Lab07 Review User is the sole direct member. |
| [Excessive assignment](lab07-excessive-contributor-assignment.png) | Group Contributor at This resource; administrator Owner inherited. |
| [Reader remediation](lab07-reader-remediation.png) | Reader replaces Contributor at This resource. |
| [User assignment check](lab07-review-user-effective-access.png) | Reader derived through MRTG-Lab07-Reviewers. |
| [Read test](lab07-reviewer-read-verified.png) | Reviewer identity and loaded resource group Overview. |
| [Write test](lab07-reviewer-tag-write-denied.png) | Tag save failed with AuthorizationFailed. |
| [Role cleanup](lab07-role-assignment-cleanup.png) | Only inherited administrator Owner remains. |
| [Resource group cleanup](lab07-resource-group-cleanup.png) | No resource groups displayed with all subscriptions/locations selected. |
| [Group cleanup](lab07-review-group-cleanup.png) | Exact group-name search returns zero groups. |
| [Active user cleanup](lab07-review-user-cleanup.png) | Unfiltered active list contains only original administrator. |
| [Final October cost review](lab07-final-cost-review.png) | Actual cost `--`; no cost reported after cleanup. |

### Least-privilege correction

[Reader replaces Contributor at resource-group scope](lab07-reader-remediation.png)

### Actual denied write

[Reviewer tag save rejected with AuthorizationFailed](lab07-reviewer-tag-write-denied.png)
