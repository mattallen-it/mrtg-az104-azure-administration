# MRTG Azure Administration

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Labs validated](https://img.shields.io/badge/Labs_validated-8_of_32-2E7D32)

Hands-on Azure administration for the fictional **Monroe Redstone Technology Group**, with an emphasis on identity, access control, troubleshooting, and operational accountability.

Each completed lab documents the business problem, configuration decisions, work performed, validation evidence, and cleanup. Planned labs are labeled separately from demonstrated results.

## Labs

**8 of 32 labs validated.** Labs 01–08 include completed Azure work and cleanup evidence, with evidence limits stated in each lab; Labs 09–32 remain planned.

| Lab | Demonstrated work | Status |
|---|---|---|
| [01 — Subscription inventory and cost baseline](labs/lab-01-subscription-inventory-and-cost-baseline/README.md) | Active subscription and Owner access verified; monthly budget configured; tagged resource group created and removed | Validated |
| [02 — Resource organization and management hierarchy](labs/lab-02-resource-organization-and-management-hierarchy/README.md) | Departmental groups and tags validated; inherited Owner access and management hierarchy inspected; groups removed | Validated |
| [03 — Employee and contractor lifecycle](labs/lab-03-employee-and-contractor-lifecycle/README.md) | Synthetic identities and memberships managed through onboarding, transfer, offboarding, and cleanup | Validated — directory state |
| [04 — Scoped administration](labs/lab-04-scoped-administration/README.md) | Group-based Reader and Contributor access scoped to Operations; permitted and denied actions tested under separate identities | Validated — Azure RBAC |
| [05 — Guardrails with policy and locks](labs/lab-05-guardrails-with-policy-and-locks/README.md) | Central US group created; East US blocked in the portal by the named policy; Delete lock prevented deletion; resource group and policy removed | Validated — governance |
| [06 — Password reset and account recovery operations](labs/lab-06-password-recovery-and-licensing/README.md) | Administrator reset, password-change and recovery sign-in evidence, reset-target audit review, and active-user cleanup | Validated — administrator-assisted recovery |
| [07 — Access review and cost review](labs/lab-07-access-review-and-cost-review/README.md) | Excessive Contributor corrected to Reader; reviewer read succeeded and tag write was denied; temporary objects removed | Validated — manual review |
| [08 — Address plan and subnets](labs/lab-08-address-plan-and-subnets/README.md) | Two private subnets deployed; overlapping range rejected by portal validation; original subnets verified and resource group removed | Validated — address planning |

[View all 32 labs and their status](docs/progress.md)

The completed labs connect subscription governance, resource organization, identity lifecycle, scoped access, and policy guardrails. Lab 06 adds administrator-assisted account recovery and audit traceability; forgotten-password SSPR remains outside the tested scope. Lab 07 demonstrates a manual access review with least-privilege remediation and a denied write request. Lab 08 adds a deployed address plan and subnet overlap validation, followed by cleanup. Traffic filtering and connectivity tests remain for future labs, alongside storage, compute, monitoring, and recovery.

The series uses **Microsoft Entra ID Free**. No paid Entra or Microsoft 365 license purchase or trial is planned. Labs use assigned groups, ordinary Azure RBAC, manual access reviews and managed identities; premium identity features remain study/design topics. Azure resource charges and software rights are checked separately before deployment.

## Environment and operating records

[Architecture](docs/architecture.md) · [Access matrix](docs/access-control-matrix.md) · [Decisions](docs/decisions.md) · [Cost ledger](docs/cost-ledger.md) · [Licensing and prerequisites](docs/licensing-and-prerequisites.md)

## Related MRTG projects

[Enterprise IAM](https://github.com/mattallen-it/MRTG-Enterprise-IAM-Lab-Series) · [AZ-900: The Bridge](https://github.com/mattallen-it/mrtg-az900-the-bridge) · [SC-900](https://github.com/mattallen-it/mrtg-sc900-security-compliance-identity)

## Scope

MRTG is a simulated enterprise using synthetic data in a personal lab environment. Results describe the work actually performed, with untested features and retained resources identified. This portfolio does not represent production administration or regulatory compliance certification.

AI assists with planning and documentation; the author performs and validates the Azure work. Published evidence is reviewed for sensitive information.

[MIT License](LICENSE)
