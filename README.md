# MRTG Azure Administration

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Labs validated](https://img.shields.io/badge/Labs_validated-18_of_32-2E7D32)

An Azure administration portfolio for the fictional **Monroe Redstone Technology Group (MRTG)**. The work connects identity and access control, resource governance, networking, storage, troubleshooting, and recovery.

**18 of 32 labs validated: Labs 01–18.** Lab 16 now includes AD DS authentication, private VPN connectivity, Finance/HR permission tests and cleanup. Lab 18 demonstrates a parameterized Bicep deployment, controlled changes, preflight rejection and a clean rebuild from unchanged source. Labs 19–32 are planned. Each completed lab follows the same structure: outcome, business problem, environment, work performed, validation, troubleshooting, cleanup, and evidence limits.

[Lab progress](docs/progress.md) · [Architecture](docs/architecture.md) · [Access matrix](docs/access-control-matrix.md) · [Cost ledger](docs/cost-ledger.md)

## Demonstrated work

| Lab | Demonstrated work | Status |
|---|---|---|
| [01 — Subscription inventory and cost baseline](labs/lab-01-subscription-inventory-and-cost-baseline/README.md) | Active subscription and Owner access verified; monthly budget configured; tagged resource group created and removed | Validated |
| [02 — Resource organization and management hierarchy](labs/lab-02-resource-organization-and-management-hierarchy/README.md) | Departmental groups and tags validated; inherited Owner access and management hierarchy inspected; groups removed | Validated |
| [03 — Employee and contractor lifecycle](labs/lab-03-employee-and-contractor-lifecycle/README.md) | Synthetic identities and memberships managed through onboarding, transfer, offboarding, and cleanup | Validated |
| [04 — Scoped administration](labs/lab-04-scoped-administration/README.md) | Group-based Reader and Contributor access scoped to Operations; permitted and denied actions tested under separate identities | Validated |
| [05 — Guardrails with policy and locks](labs/lab-05-guardrails-with-policy-and-locks/README.md) | Central US group created; East US blocked in the portal by the named policy; Delete lock prevented deletion; resource group and policy removed | Validated |
| [06 — Password reset and account recovery operations](labs/lab-06-password-recovery-and-licensing/README.md) | Administrator reset, password-change and recovery sign-in evidence, reset-target audit review, and active-user cleanup | Validated |
| [07 — Access review and cost review](labs/lab-07-access-review-and-cost-review/README.md) | Excessive Contributor corrected to Reader; reviewer read succeeded and tag write was denied; temporary objects removed | Validated |
| [08 — Address plan and subnets](labs/lab-08-address-plan-and-subnets/README.md) | Two private subnets deployed; overlapping range rejected by portal validation; original subnets verified and resource group removed | Validated |
| [09 — Traffic permissions](labs/lab-09-traffic-permissions/README.md) | ASG-based HTTP access tested through removal and restoration; port 8081 blocked; resource group deleted | Validated |
| [10 — Peering and route investigation](labs/lab-10-peering-and-route-investigation/README.md) | Private-IP traffic verified across peered VNets; a more specific drop route caused failure; route removal restored connectivity; cleanup and posted costs reviewed | Validated |
| [11 — Name resolution and application availability](labs/lab-11-name-resolution-and-application-availability/README.md) | Private DNS and an internal load balancer tested with two web backends; backend failure and DNS misconfiguration isolated and recovered; cleanup verified; USD 0.15 posted cost reviewed | Validated |
| [12 — Private access and administrator entry](labs/lab-12-private-access-and-administrator-entry/README.md) | Service and private endpoint blob reads with a container-scoped managed identity; private DNS, Bastion entry, public access denial, cleanup and USD 1.74 posted cost reviewed | Validated |
| [13 — Storage baseline and transfer](labs/lab-13-storage-baseline-and-transfer/README.md) | Entra-authenticated upload/download of three synthetic files; SHA-256 mismatch detected, CSV downloaded again, all final hashes matched; resource group cleanup verified | Validated |
| [14 — Data access boundaries](labs/lab-14-data-access-boundaries/README.md) | Account Reader versus blob-data access tested; container-scoped reads allowed, restricted-container reads and uploads denied; read-only SAS GET 200/PUT 403; old/new key rotation tests and redacted cost review | Validated |
| [15 — Recover an accidental document deletion](labs/lab-15-recover-an-accidental-document-deletion/README.md) | Soft-delete and overwritten-version recovery verified by SHA-256; lifecycle policy exported; cleanup verified | Validated |
| [16 — Department file access and the AD bridge](labs/lab-16-department-file-access-and-the-ad-bridge/README.md) | Snapshot recovery; rebuilt private-endpoint/VPN access with AD DS, Finance/HR folder boundaries, AES-256 Kerberos and cleanup | Validated |
| [17 — Replication and storage incident drill](labs/lab-17-replication-and-storage-incident-drill/README.md) | New block blob replicated; source status Complete; initial and post-network-recovery SHA-256 matches; 403 fault/recovery, cleanup verified | Validated |
| [18 — Reproducible MRTG deployment](labs/lab-18-reproducible-mrtg-deployment/README.md) | Parameterized Bicep baseline; tag override, invalid-priority preflight rejection, clean rebuild, identical outputs and source hashes, no-change plan and cleanup | Validated |

[View all 32 labs and planned work](docs/progress.md)

## How to review this portfolio

Start with a lab's **Outcome** and **Validation results**, then inspect its **Evidence and limits** and complete screenshot gallery. Setup forms, observed behavior, recovery tests, and cleanup are distinguished so the conclusions can be checked against the captures.

- **Identity and governance — Labs 01–07:** subscription ownership, organization, joiner/mover/leaver administration, scoped Azure RBAC, policy and locks, administrator-assisted account recovery, and manual least-privilege review.
- **Networking — Labs 08–12:** address planning, ASG traffic tests, peering and route failure/recovery, DNS and backend fault isolation, and managed-identity storage access through service and private endpoints.
- **Storage and recovery — Labs 13–17:** byte-level transfer verification, container-scoped permissions, read-only SAS tests, key rotation, soft-delete recovery, version recovery, and Lab 16 file-share snapshot recovery plus AD DS authentication and department folder boundaries over VPN/private endpoint; Lab 17 object replication, SHA-256 verification and a controlled network fault/recovery.

- **Infrastructure as code — Lab 18:** Bicep build, what-if review, parameter overrides, provider validation, baseline restoration and clean rebuild; preserved source, checksums and matching output exports.

## Evidence and operating boundaries

These are historical disposable lab deployments. Temporary lab resources were removed after testing; retained subscription, budget, directory, and shared-resource state is recorded in each lab. Directory cleanup captures distinguish active-user removal from permanent deletion.

Reported usage is a dated snapshot, not a final invoice. Labs 13–14 show USD 0.00 breakdown tiles with an unavailable Actual cost total; this does not establish zero final cost. Lab 14 states the limits of attributing a SAS denial to revocation. Lab 15 verifies both recovery downloads with matching SHA-256 hashes; the lifecycle tier transition was configured but not observed.

The series uses **Microsoft Entra ID Free** without a paid Entra or Microsoft 365 license purchase or trial. Premium identity features remain study/design topics. Azure resource charges and software rights are considered separately.

## Operating records

[Architecture](docs/architecture.md) · [Access matrix](docs/access-control-matrix.md) · [Decisions](docs/decisions.md) · [Cost ledger](docs/cost-ledger.md) · [Licensing and prerequisites](docs/licensing-and-prerequisites.md)

## Related MRTG projects

[Enterprise IAM](https://github.com/mattallen-it/MRTG-Enterprise-IAM-Lab-Series) · [AZ-900: The Bridge](https://github.com/mattallen-it/mrtg-az900-the-bridge) · [SC-900](https://github.com/mattallen-it/mrtg-sc900-security-compliance-identity)

## Scope and documentation

MRTG is a simulated enterprise using synthetic data in a personal lab environment. Results describe the tested actions and captured states, with untested behavior and retained resources identified. This portfolio does not represent production administration or regulatory compliance certification.

AI assists with planning and documentation; the author performs and validates the Azure work. Published evidence is reviewed for sensitive information. [Repository maintenance](CONTRIBUTING.md) defines the lab format and validation checks.

[MIT License](LICENSE)
