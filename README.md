# MRTG Azure Administration

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Labs validated](https://img.shields.io/badge/Labs_validated-3_of_32-2E7D32)

Hands-on Azure administration for the fictional **Monroe Redstone Technology Group**, with an emphasis on identity, access control, troubleshooting, and operational accountability.

Each completed lab documents the business problem, configuration decisions, work performed, validation evidence, and cleanup. Planned labs are labeled separately from demonstrated results.

## Labs

| Lab | Demonstrated work | Status |
|---|---|---|
| [01 — Subscription inventory and cost baseline](labs/lab-01-subscription-inventory-and-cost-baseline/README.md) | Active subscription and Owner access verified; monthly budget configured; tagged resource group created and removed | Validated |
| [02 — Resource organization and management hierarchy](labs/lab-02-resource-organization-and-management-hierarchy/README.md) | Departmental groups and tags validated; inherited Owner access and management hierarchy inspected; groups removed | Validated |
| [03 — Employee and contractor lifecycle](labs/lab-03-employee-and-contractor-lifecycle/README.md) | Synthetic identities and memberships managed through onboarding, transfer, offboarding, and cleanup | Validated — directory state |

[View all 32 labs and their status](docs/progress.md)

The planned portfolio covers Azure governance, scoped identity and data access, networking, storage, compute, monitoring, and recovery.

## Environment and operating records

[Architecture](docs/architecture.md) · [Access matrix](docs/access-control-matrix.md) · [Decisions](docs/decisions.md) · [Cost ledger](docs/cost-ledger.md)

## Related MRTG projects

[Enterprise IAM](https://github.com/mattallen-it/MRTG-Enterprise-IAM-Lab-Series) · [AZ-900: The Bridge](https://github.com/mattallen-it/mrtg-az900-the-bridge) · [SC-900](https://github.com/mattallen-it/mrtg-sc900-security-compliance-identity)

## Scope

MRTG is a simulated enterprise using synthetic data in a personal lab environment. Results describe the work actually performed, with untested features and retained resources identified. This portfolio does not represent production administration or regulatory compliance certification.

AI assists with planning and documentation; the author performs and validates the Azure work. Published evidence is reviewed for sensitive information.

[MIT License](LICENSE)
