# Architecture and operations decisions

Decisions distinguish accepted plans from configurations demonstrated in the lab.

| ID | Decision | Reason | Tradeoff | Status |
|---|---|---|---|---|
| ADR-001 | Use disposable workloads and preserve configuration/evidence | Control lab cost and enable rebuilds | Rebuild effort between sessions | Accepted plan |
| ADR-003 | Validate cloud-only identities before optional hybrid work | Avoid introducing unverified synchronization dependencies | Hybrid scenarios remain a later extension | Accepted plan |
| ADR-004 | Separate Operations and Security into tagged resource groups | Make departmental ownership and resource scope explicit | Tags identify responsibility but do not enforce permissions; subscription Owner still inherited | Demonstrated and cleaned up in [Lab 02](../labs/lab-02-resource-organization-and-management-hierarchy/README.md) |
