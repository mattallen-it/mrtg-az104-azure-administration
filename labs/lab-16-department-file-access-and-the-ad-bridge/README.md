# Lab 16 — Department file access and the AD bridge

![AZ-104](https://img.shields.io/badge/AZ--104-Azure_Administrator-0078D4) ![Status: Planned](https://img.shields.io/badge/Status-Planned-lightgrey)

## MRTG assignment

Request: give an MRTG test group shared file access. Create a tiny file share and test snapshot recovery. For identity-based SMB, first document the chosen supported identity source, client state, DNS, connectivity, and permissions. Implement only after those prerequisites are met. Pass: explain and test share-level versus file-level authorization; if blocked, preserve a design-only gap. A storage-key mount is not proof of identity-based access. Reuse existing AD knowledge without assuming hybrid identity is already configured. [Azure Files identity prerequisites](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview).

## Study alignment

- **Course:** Section 10, lectures 77–78; identity-based SMB is an MRTG extension with separate prerequisites.
- **Microsoft Learn:** [Storage](https://learn.microsoft.com/en-us/training/paths/az-104-manage-storage/).
- Follow the [full course mapping](../../docs/series-guide.md) for prerequisites and study order.

## Before starting

- [ ] Confirm the intended directory/subscription, required roles, dependencies, and licensing.
- [ ] Estimate runtime and cost using [mode B/C](../../docs/series-guide.md#cost-plan); identify resources to remove or retain.
- [ ] Define success, the controlled fault or denial, and the recovery test from the assignment.
- [ ] Plan evidence checkpoints: configuration, observed result, fault/retest, and cleanup. Capture evidence before deleting resources.

## Execution record

Not started. Use the [lab template](../../docs/lab-template.md) when performing the work, keeping only applicable sections. Record actual results and any design-only gaps; update [progress](../../docs/progress.md) after validation.
