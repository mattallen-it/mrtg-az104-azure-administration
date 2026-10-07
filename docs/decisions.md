# Architecture and operations decisions

Decisions distinguish accepted plans from configurations demonstrated in the lab.

| ID | Decision | Reason | Tradeoff | Status |
|---|---|---|---|---|
| ADR-001 | Use disposable workloads and preserve configuration/evidence | Control lab cost and enable rebuilds | Rebuild effort between sessions | Accepted plan |
| ADR-003 | Validate cloud-only identities before optional hybrid work | Avoid introducing unverified synchronization dependencies | Hybrid scenarios remain a later extension | Accepted plan |
| ADR-004 | Separate Operations and Security into tagged resource groups | Make departmental ownership and resource scope explicit | Tags identify responsibility but do not enforce permissions; subscription Owner still inherited | Demonstrated and cleaned up in [Lab 02](../labs/lab-02-resource-organization-and-management-hierarchy/README.md) |
| ADR-006 | Use Entra Free and administrator-assisted recovery for Lab 06; retain premium identity features as study/design topics | Complete a practical recovery workflow without buying user licenses or activating trials | Forgotten-password SSPR is excluded from live validation; Azure resource charges remain separate | Recovery demonstrated and active-user cleanup verified in [Lab 06](../labs/lab-06-password-recovery-and-licensing/README.md); [series baseline](licensing-and-prerequisites.md) accepted |
| ADR-007 | Review assigned memberships and scoped Azure RBAC manually; replace excessive Contributor with Reader | Match access to the reviewer's read-only business need without premium identity licensing | Manual review requires recorded findings and separate access tests; automated Entra Access Reviews remain untested | Demonstrated and cleaned up in [Lab 07](../labs/lab-07-access-review-and-cost-review/README.md) |
| ADR-008 | Establish an address plan using two private /24 subnets within a /16 VNet; validate an overlapping /25 before deploying workloads | Demonstrate configuration validation and preserve explicit address ownership | Separate subnet ranges do not demonstrate traffic isolation; no workload connectivity was tested | Demonstrated and cleaned up in [Lab 08](../labs/lab-08-address-plan-and-subnets/README.md) |
