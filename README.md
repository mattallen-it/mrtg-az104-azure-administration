# MRTG Azure Administration

Hands-on Azure administration with an identity and security focus, built for the fictional **Monroe Redstone Technology Group**.

**Current state:** Repository prepared · **0/32 labs validated** · AZ-104 preparation in progress.

This series follows Scott Duffy’s AZ-104 course and Microsoft Learn. It extends earlier MRTG AD/IAM and Microsoft fundamentals projects into practical cloud operations. Azure deployments and results will be recorded as they are performed.

## Start here

| Looking for | Open |
|---|---|
| Environment and planned architecture | [Architecture](docs/architecture.md) |
| Project stories and supporting evidence | [Case studies](case-studies/README.md) |
| Full curriculum and course mapping | [Series guide](docs/series-guide.md) |
| Lab index and completion status | [Progress](docs/progress.md) |
| First hands-on task | [Lab 01: subscription and cost baseline](labs/lab-01-subscription-inventory-and-cost-baseline/README.md) |

## What the work will demonstrate

- **Controlled access:** scoped permissions, identity lifecycle, managed identities, and tested denial.
- **Protected workloads:** compute, networking, and data access with documented troubleshooting.
- **Operational recovery:** useful alerts, verified restores, reproducible builds, and cost-aware cleanup.

These are planned outcomes. The [evidence standard](docs/evidence-standard.md) defines when a result can be claimed.

## Operating records

[Access matrix](docs/access-control-matrix.md) · [Decision log](docs/decisions.md) · [Cost ledger](docs/cost-ledger.md) · [Incident reports](incidents/README.md) · [Runbooks](runbooks/README.md)

## Existing MRTG foundation

[Enterprise IAM](https://github.com/mattallen-it/MRTG-Enterprise-IAM-Lab-Series) · [AZ-900: The Bridge](https://github.com/mattallen-it/mrtg-az900-the-bridge) · [SC-900](https://github.com/mattallen-it/mrtg-sc900-security-compliance-identity)

## Scope and transparency

MRTG is a simulated enterprise, not production administration experience or a claim of regulatory compliance. Use synthetic data and authorized personal lab resources. AI assists with planning and documentation; the author performs and validates Azure work. Published evidence is reviewed for sensitive information.

Default region: Central US, subject to availability. Additional cash allowance: up to $100 for the series; budget alerts do not enforce a spending cap.

Documentation checks validate local file links and basic Markdown hygiene; they do not validate Azure configurations or external websites. See [contributing](CONTRIBUTING.md).

[MIT License](LICENSE)
