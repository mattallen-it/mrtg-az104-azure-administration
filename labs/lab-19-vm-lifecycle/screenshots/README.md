# Lab 19 — Evidence gallery

[Lab results](../README.md) · [Portfolio](../../../README.md)

**51 published screenshots.** Fifty execution images were captured during the November 14, 2026 lab session (America/Chicago); the added cost review is dated November 15. Files retain the submitted PNG bytes, including the author's redactions. This is a chronological index of setup, live checks, unsuccessful troubleshooting, completed tests and cleanup.

The submitted package contained 50 PNGs. The author supplied a corrected `lab19-bastion-inprivate-session-failed.png` with its account label redacted; that replacement is included here. The other 49 files retain the original package bytes. Filenames are descriptive labels, not additional proof: in particular, the SSH rule form does not establish its final effective source restriction.

| # | Capture | What it establishes / limit |
|---|---|---|
| 01 | [Subscription and size prerequisites](lab19-subscription-and-vm-sku-check.png) | Enabled subscription and empty restriction lists; allocation capacity is not guaranteed. |
| 02 | [Tagged resource group](lab19-resource-group-created.png) | Creation returned Succeeded in Central US with the four ownership tags. |
| 03 | [Network and service endpoint](lab19-vnet-and-subnet-created.png) | VNet/subnet creation and live subnet readback: default outbound false and Microsoft.Storage endpoint. |
| 04 | [Subnet NSG baseline](lab19-nsg-rules-and-subnet-association.png) | VirtualNetwork SSH allow and custom inbound deny; NSG associated with snet-vm. Sensitive subscription text was redacted in the supplied image. |
| 05 | [VM basics form](lab19-vm-basics-and-price.png) | Selected Ubuntu, original size and SSH settings; setup selection, not deployment proof. |
| 06 | [OS disk form](lab19-os-disk-configuration.png) | Selected 30 GiB Standard SSD and deletion setting; setup form. |
| 07 | [VM networking form](lab19-vm-networking-configuration.png) | Initially no public IP or NIC NSG; selected subnet and accelerated networking. |
| 08 | [Management and identity form](lab19-managed-identity-configuration.png) | System-assigned identity enabled; Entra OS login not enabled. |
| 09 | [Monitoring form](lab19-monitoring-configuration.png) | Managed boot diagnostics selected; guest diagnostics, alerts and health monitoring off. |
| 10 | [Advanced VM form](lab19-vm-advanced-configuration.png) | No initial extensions or cloud-init; SCSI controller selected. |
| 11 | [Resource tags form](lab19-vm-resource-tags.png) | Four selected ownership tags; deployment-stage selection. |
| 12 | [Initial monthly estimate](lab19-vm-estimated-monthly-cost.png) | USD 8.61 compute plus USD 2.40 disk, USD 11.01 displayed total; historical estimate, not posted usage. |
| 13 | [Reviewed image and basic settings](lab19-vm-review-basics.png) | Final review shows Canonical image terms and original configuration; account address redacted in supplied capture. |
| 14 | [Reviewed network and identity settings](lab19-vm-review-network-identity-tags.png) | Final form includes no initial public IP, system identity and tags; not an individual live readback of every field. |
| 15 | [Deployment complete](lab19-vm-deployment-succeeded.png) | Portal deployment completion, separate from configuration forms. |
| 16 | [Live deployed baseline](lab19-deployed-vm-configuration-verified.png) | CLI returns running B2ts_v2, Canonical publisher, private address, no public address, Standard SSD and SystemAssigned. |
| 17 | [Bastion provisioning](lab19-bastion-developer-provisioning-verified.png) | Developer SKU and Succeeded provisioning; not successful SSH entry. |
| 18 | [Bastion session error response](lab19-bastion-session-error-response.png) | Generic internal-server-error response; does not identify a root cause. |
| 19 | [Guest SSH health](lab19-ssh-service-diagnostic.png) | VM Agent Run Command: correct hostname, SSH active and TCP 22 listening. |
| 20 | [Unsupported platform-IP check](lab19-platform-ip-flow-check-unsupported.png) | Network Watcher rejects restricted source address; not an NSG deny verdict. |
| 21 | [Candidate troubleshooting rule](lab19-bastion-developer-ssh-rule.png) | Priority 110 TCP 22 exception from the proposed platform source; did not resolve the session failure. |
| 22 | [Diagnostic did not execute, part 1](lab19-bastion-diagnostic-not-executed-01.png) | Copilot explicitly reports diagnostic non-execution before giving generic guidance; not a diagnostic finding. |
| 23 | [Diagnostic guidance continuation](lab19-bastion-diagnostic-not-executed-02.png) | Generic gateway/subnet advice; not verified Developer-SKU remediation. |
| 24 | [InPrivate session failure](lab19-bastion-inprivate-session-failed.png) | Corrected author-supplied capture with account label redacted; InPrivate attempt still returned an internal session error, without establishing its cause. |
| 25 | [Continuing Bastion failure](lab19-bastion-session-failed-after-recreate.png) | Session error persisted after an operator-reported recreate; no separate recreation-operation log in this package. |
| 26 | [Fallback SSH rule form](lab19-ssh-source-ip-restricted-rule.png) | My IP address, priority 120, TCP 22 to 10.190.10.4/32; pre-save form with source CIDR omitted, not final effective-rule proof. |
| 27 | [Temporary public IP on NIC](lab19-temporary-public-ip-associated.png) | NIC readback shows fallback public IP associated with ipconfig1; historical IP, deleted with group. |
| 28 | [Host fingerprint comparison](lab19-ssh-host-fingerprint-verified.png) | OpenSSH prompt compared with trusted VM Agent ssh-keygen output before host acceptance. |
| 29 | [Successful fallback SSH session](lab19-source-restricted-ssh-session-verified.png) | whoami and hostname identify azureuser on the expected VM; screenshot alone does not prove source restriction despite filename. |
| 30 | [Guest baseline](lab19-vm-cpu-memory-disk-baseline.png) | 2 CPUs, 840 MiB usable memory and 30 GiB OS disk before attaching the data disk. |
| 31 | [Managed disk attachment](lab19-data-disk-attached.png) | 4 GiB Standard SSD created and attached at LUN 0 with caching None; Azure readback follows. |
| 32 | [Guest disk identification](lab19-data-disk-device-identified.png) | New 4 GiB sdb and Azure LUN-0 symlink identified before formatting. |
| 33 | [Filesystem and first mount](lab19-data-disk-formatted-and-mounted.png) | GPT/ext4 creation, ownership, findmnt and df output for /mnt/mrtg-data. |
| 34 | [UUID-based persistent mount](lab19-fstab-configuration-verified.png) | fstab backup and UUID entry; verification reports no errors or warnings. Filesystem UUIDs are non-secret identifiers. |
| 35 | [Remount and hash baseline](lab19-persistent-mount-and-data-baseline.png) | Fixture SHA-256 saved on OS disk; unmount/remount through fstab passed checksum. |
| 36 | [Deallocated power state](lab19-vm-deallocated-verified.png) | Azure readback shows VM deallocated at the original size. |
| 37 | [Larger size and estimate](lab19-resize-target-and-price.png) | B2s_v2 target selection with displayed USD 68.62 monthly compute estimate; not a bill. |
| 38 | [Running larger VM](lab19-vm-resized-and-started.png) | CLI shows B2s_v2 running with SystemAssigned identity and the same observed IP addresses. |
| 39 | [Guest checks after resize](lab19-resize-memory-and-data-persistence-verified.png) | 2 CPUs, 7.7 GiB memory, automatically mounted filesystem, fixture content and checksum OK. |
| 40 | [Original size restored](lab19-original-vm-size-restored.png) | Deallocate, resize back and start; Azure readback shows B2ts_v2 running with identity. |
| 41 | [Storage security baseline](lab19-storage-account-created.png) | Succeeded; anonymous and Shared Key access false, HTTPS true and TLS1_2. Network initially Allow for authenticated setup. |
| 42 | [Temporary administrator data role](lab19-administrator-storage-setup-role.png) | Storage Blob Data Contributor assigned to the User at the new storage-account scope for fixture creation. |
| 43 | [Known private-container fixtures](lab19-storage-test-containers-and-blobs.png) | Entra login creates both private containers and uploads proof.txt; listings show 39 and 41 bytes. |
| 44 | [VM container-scoped Reader](lab19-vm-container-reader-role-assigned.png) | Storage Blob Data Reader assignment to ServicePrincipal; command scopes it to lab19-readable. |
| 45 | [Network restriction and role cleanup](lab19-storage-network-restricted-and-setup-role-removed.png) | Default Deny, bypass None, one subnet, zero IP rules; exact bootstrap role deleted and matching count 0. Public network remains Enabled. |
| 46 | [Permitted managed-identity read](lab19-managed-identity-blob-read-allowed.png) | IMDS token held in a variable; HTTP 200 and expected readable fixture. Actual token value is not displayed. |
| 47 | [Write and cross-container denials](lab19-managed-identity-write-and-cross-container-denied.png) | PUT in readable and GET in restricted each return HTTP 403 with AuthorizationPermissionMismatch. |
| 48 | [Final controls after restoring size](lab19-final-access-and-data-persistence-verified.png) | Permitted GET 200, 2 CPUs, 840 MiB memory, mount now /dev/sda1, checksum OK; token unset. |
| 49 | [Azure resource cleanup](lab19-resource-group-cleanup-verified.png) | Ten-resource inventory, group deletion and az group exists false. |
| 50 | [Local key path removed](lab19-local-private-key-removal-verified.png) | Remove-Item followed by Test-Path False for the downloaded PEM path; not proof of secure erasure or every copy. |
| 51 | [November 15 cost review](lab19-cost-review-2026-11-15.png) | November 2026, billing-account scope filtered to Lab 19: Actual USD 0.05; VMs 0.03, Storage 0.01, Virtual Network/Bandwidth each below 0.01. Author-redacted identity; rounded posted snapshot, not final invoice. |

Bastion session establishment was unsuccessful and its cause remains unresolved. Monthly prices shown are historical portal estimates; the November 15 image records USD 0.05 in posted usage, not a final invoice. Read the lab results for test scope and conclusions.

The additional November 15 cost image preserves the author-supplied redacted bytes. Only the first 50 images document the November 14 execution session.
