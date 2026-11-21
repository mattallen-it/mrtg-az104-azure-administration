# Lab Portfolio

**22/32 labs validated (Labs 01–22).** Labs 23–32 remain planned. Each validated record separates configuration, observed results, troubleshooting, cleanup and evidence limits.

[Lab 21 — Availability and scale](../labs/lab-21-availability-and-scale/README.md) verifies initial placement across two zones, web-service failure/recovery, automatic application bootstrap on scale-out, and manual plus CPU-driven autoscale **2 → 3 → 2**. Final HTTP samples passed through both remaining backends. The gallery publishes **33 screenshots**, including author-redacted cleanup, cost and NSG captures.

The November 16 Lab 21 posted-cost snapshot is **USD 0.34**, not a final invoice. Earlier labs retain their own limits: configured features do not establish observed execution, failed administrator entry is not reported as successful, and unavailable cost data is not assumed zero. See each lab and the [cost ledger](cost-ledger.md) for scope and dates.

[Lab 22 — Container delivery](../labs/lab-22-container-delivery/README.md) validates registry-scoped managed-identity image pulls to ACI and Container Apps, HTTP/HTTPS 200, ingress 503 → 200 recovery, matching template hashes and group absence. Its 17 screenshots, including both dated cost reviews, and two original ARM templates are published. Posted usage increased from **USD 0.28 on November 19** to **USD 0.32 on November 20**; neither snapshot is a final invoice.

## Lab index

| Lab | Assignment | Status |
|---|---|---|
| 01 | [Subscription inventory and cost baseline](../labs/lab-01-subscription-inventory-and-cost-baseline/README.md) | Validated — portal baseline |
| 02 | [Resource organization and management hierarchy](../labs/lab-02-resource-organization-and-management-hierarchy/README.md) | Validated — organization and inheritance |
| 03 | [Employee and contractor lifecycle](../labs/lab-03-employee-and-contractor-lifecycle/README.md) | Validated — directory state |
| 04 | [Scoped administration](../labs/lab-04-scoped-administration/README.md) | Validated — scoped Azure RBAC |
| 05 | [Guardrails with policy and locks](../labs/lab-05-guardrails-with-policy-and-locks/README.md) | Validated — policy and delete lock |
| 06 | [Password reset and account recovery operations](../labs/lab-06-password-recovery-and-licensing/README.md) | Validated — administrator-assisted recovery |
| 07 | [Access review and cost review](../labs/lab-07-access-review-and-cost-review/README.md) | Validated — manual access and cost review |
| 08 | [Address plan and subnets](../labs/lab-08-address-plan-and-subnets/README.md) | Validated — subnet configuration and overlap validation |
| 09 | [Traffic permissions](../labs/lab-09-traffic-permissions/README.md) | Validated — ASG traffic tests, cleanup and posted cost review |
| 10 | [Peering and route investigation](../labs/lab-10-peering-and-route-investigation/README.md) | Validated — peering, route failure/recovery, cleanup and posted costs |
| 11 | [Name resolution and application availability](../labs/lab-11-name-resolution-and-application-availability/README.md) | Validated — private DNS, load balancing, backend and DNS recovery, cleanup and posted costs |
| 12 | [Private access and administrator entry](../labs/lab-12-private-access-and-administrator-entry/README.md) | Validated — service/private endpoints, managed-identity blob read, Bastion, private DNS, public denial, cleanup and posted costs |
| 13 | [Storage baseline and transfer](../labs/lab-13-storage-baseline-and-transfer/README.md) | Validated — Entra-authenticated transfers, SHA-256 mismatch/retry and final matches, cleanup |
| 14 | [Data access boundaries](../labs/lab-14-data-access-boundaries/README.md) | Validated — scoped access, read-only SAS, key rotation and cleanup; SAS attribution limit documented |
| 15 | [Recover an accidental document deletion](../labs/lab-15-recover-an-accidental-document-deletion/README.md) | Validated — soft-delete/version recovery and SHA-256 matches; lifecycle configuration, cleanup and cost review |
| 16 | [Department file access and the AD bridge](../labs/lab-16-department-file-access-and-the-ad-bridge/README.md) | Validated — snapshot recovery; AD DS, VPN/private endpoint, department read/write and cross-read denial, AES-256 Kerberos; Azure/hosts/AD-object cleanup verified |
| 17 | [Replication and storage incident drill](../labs/lab-17-replication-and-storage-incident-drill/README.md) | Validated — new-blob object replication, Complete status, matching initial/post-recovery hashes, 403 network fault/recovery and cleanup |
| 18 | [Reproducible MRTG deployment](../labs/lab-18-reproducible-mrtg-deployment/README.md) | Validated — Bicep baseline, controlled tag override, invalid-priority preflight rejection, unchanged-source rebuild, matching outputs, no-change plan and cleanup |
| 19 | [VM lifecycle](../labs/lab-19-vm-lifecycle/README.md) | Validated — SSH fallback, disk/UUID mount, deallocate/resize/return with hash matches, managed-identity read/deny controls and cleanup; Bastion unresolved |
| 20 | [Disk recovery and relocation](../labs/lab-20-disk-recovery-and-relocation/README.md) | Validated — snapshot recovery, three original SHA-256 matches before/after restored-disk group relocation; cleanup reviewed, local key removed |
| 21 | [Availability and scale](../labs/lab-21-availability-and-scale/README.md) | Validated — zonal VMSS, service fault/recovery, manual and automatic 2 → 3 → 2 scaling; cleanup reviewed |
| 22 | [Container delivery](../labs/lab-22-container-delivery/README.md) | Validated — managed-identity image delivery, ACI/Container Apps HTTP tests, ingress fault/recovery, templates and cleanup |
| 23 | [Managed web application](../labs/lab-23-managed-web-application/README.md) | Planned |
| 24 | [Controlled application release](../labs/lab-24-controlled-application-release/README.md) | Planned |
| 25 | [Logs and operational questions](../labs/lab-25-logs-and-operational-questions/README.md) | Planned |
| 26 | [Actionable alerts](../labs/lab-26-actionable-alerts/README.md) | Planned |
| 27 | [Network incident response](../labs/lab-27-network-incident-response/README.md) | Planned |
| 28 | [Backup with a proven restore](../labs/lab-28-backup-with-a-proven-restore/README.md) | Planned |
| 29 | [Regional recovery exercise](../labs/lab-29-regional-recovery-exercise/README.md) | Planned |
| 30 | [Joiner, mover, leaver across services](../labs/lab-30-joiner-mover-leaver-across-services/README.md) | Planned |
| 31 | [MRTG Azure operations capstone](../labs/lab-31-mrtg-azure-operations-capstone/README.md) | Planned |
| 32 | [Independent rebuild and operations handover](../labs/lab-32-rebuild-review-and-exam-readiness/README.md) | Planned |
