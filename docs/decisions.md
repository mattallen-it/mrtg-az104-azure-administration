# Architecture and operations decisions

Record meaningful tradeoffs, not every portal selection. Initial entries below are planning decisions, not deployment results.

| ID | Decision | Reason | Tradeoff | Status |
|---|---|---|---|---|
| ADR-001 | Use disposable workloads and preserve configuration/evidence | Control lab cost and enable rebuilds | Rebuild effort between sessions | Accepted plan |
| ADR-003 | Validate cloud-only identities before optional hybrid work | Avoid introducing unverified synchronization dependencies | Hybrid scenarios remain a later extension | Accepted plan |

## Entry format

ID and date; requirement; options considered; decision; justification; cost and security implications; evidence; limitations; conditions that would cause reconsideration.
