# Lab 19 — VM lifecycle

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

[Portfolio](../../README.md) · [All labs](../../docs/progress.md) · [Evidence gallery](screenshots/README.md)

## Outcome

**Validated November 14, 2026 (America/Chicago):** deployed an Ubuntu VM, connected through a temporary SSH fallback, attached and persistently mounted a managed data disk, deallocated and resized the VM, and verified unchanged data after returning to the original size. The system-assigned managed identity read its permitted blob with HTTP 200; a write and a read from a different container each returned HTTP 403 with `AuthorizationPermissionMismatch`. A final permitted read returned 200.

The resource group was deleted and `az group exists` returned `false`. The downloaded private-key path was removed and `Test-Path` returned `False`. **Bastion Developer provisioned successfully but never established a session; its session error remains unresolved.** Validation of the VM lifecycle and storage boundary used the SSH fallback. November 15 posted usage was USD 0.05; final billed charges remain unverified.

## Business problem

MRTG needs an administrator to change compute capacity without losing application data and give a workload only the storage access it needs. VM power state, guest filesystem persistence, network reachability, operating-system sign-in and data authorization are separate checks. A successful deployment alone establishes none of the others.

This exercise separates the administrator's temporary setup permission from the VM's container-scoped read permission. It also preserves an unsuccessful access path alongside the completed work so another operator can see what was actually tested.

## Environment and decisions

| Component | Tested configuration |
|---|---|
| Context | `MRTG-AZ104-Lab-Subscription`; resource group `rg-mrtg-lab19-vm`; Central US |
| Ownership tags | `Environment=Lab`, `Project=MRTG-AZ104-Administration`, `Lab=Lab-19`, `Owner=MRTG-Cloud-Operations` |
| Network | `vnet-mrtg-lab19`, `10.190.0.0/16`; `snet-vm`, `10.190.10.0/24`; default outbound access false; `Microsoft.Storage` service endpoint |
| Subnet NSG | `nsg-mrtg-lab19-vm`: VirtualNetwork SSH allow at priority 100 and custom inbound deny at 1000; troubleshooting/fallback exceptions described below; no NIC NSG |
| VM and image | `vm-mrtg-lab19-01`; Canonical Ubuntu Server 22.04 LTS, x64 Gen2; deployed publisher readback `canonical` |
| Compute | Initial/restored `Standard_B2ts_v2`: 2 vCPU, 1 GiB nominal RAM; resize target `Standard_B2s_v2`: 2 vCPU, 8 GiB nominal RAM |
| OS security and access | Trusted Launch, Secure Boot and vTPM; local `azureuser` with RSA SSH key; system-assigned managed identity; no Entra OS login |
| NIC and entry | `vm-mrtg-lab19-01228`, private `10.190.10.4` allocated dynamically; initially no public IP; temporary `pip-mrtg-lab19-ssh` added for fallback |
| Disks | 30 GiB Standard SSD OS disk; `disk-mrtg-lab19-data01`, 4 GiB `StandardSSD_LRS`, LUN 0, caching None |
| Storage | `stmrtgl19aec191bf`, StorageV2, Standard LRS, Hot; HTTPS required, TLS 1.2 minimum, anonymous blob access and Shared Key disabled |
| Test data | Private containers `lab19-readable` and `lab19-restricted`, each containing synthetic `proof.txt`; local disk fixture under `/mnt/mrtg-data` |
| Monitoring | Managed boot diagnostics enabled; guest diagnostics, alerts and application health monitoring disabled; no backup or Site Recovery test |

The subscription/SKU check returned Enabled and empty restriction lists for both sizes. This was a session prerequisite check; it did not guarantee allocation capacity. The portal forms record selected settings; deployment completion and CLI readbacks establish the separately captured live properties. Image publisher and terms were checked before deployment rather than relying on the Ubuntu display name alone.

## Work performed

1. Created and tagged the resource group, VNet, service-endpoint subnet and subnet NSG. Deployed the VM without a public IP. Read back successful provisioning, running power state, original size, Canonical publisher, Standard SSD OS disk, private address and system-assigned identity.
2. Attempted Bastion Developer SSH. Provisioning succeeded, but session requests returned an internal-server-error message. VM Agent Run Command showed the expected hostname, active SSH service and TCP 22 listeners. A candidate priority-110 SSH exception from `168.63.129.16/32` to `10.190.10.4/32` did not resolve the error. This was an unsuccessful troubleshooting change, not a verified Bastion source requirement.
3. Used a temporary Standard static public IP for direct SSH. Selected **My IP address** for the priority-120 inbound TCP 22 rule targeting `10.190.10.4/32`. Compared the SSH client's server fingerprint with `ssh-keygen` output obtained through VM Agent Run Command, then connected as `azureuser` and checked the hostname. The published rule capture precedes saving and omits the source CIDR; it cannot independently prove the final effective source restriction.
4. Created and attached the 4 GiB managed data disk using Cloud Shell. In the SSH guest session, checked `lsblk` and the Azure LUN-0 symlink before partitioning the new disk. Created GPT and an ext4 partition labeled `MRTG-LAB19`, mounted it at `/mnt/mrtg-data`, and assigned directory ownership to `azureuser`.
5. Backed up `/etc/fstab`, added the filesystem UUID with `ext4 defaults,nofail 0 2`, reloaded systemd and ran `findmnt --verify --verbose`. Wrote `lifecycle-proof.txt`, saved a SHA-256 baseline on the OS disk, unmounted/remounted using the fstab entry and checked the hash.
6. Deallocated the VM and captured `VM deallocated`. Resized to `Standard_B2s_v2`, started it, reconnected and checked CPU, memory, automatic mount, fixture content and checksum. Deallocated again, restored `Standard_B2ts_v2`, started and repeated the final guest checks. Both sizes retained the system-assigned identity in the Azure readback.
7. Created the storage account with public network access initially enabled and default action Allow for authenticated setup. Temporarily assigned the administrator Storage Blob Data Contributor at that account, created both private containers and seeded the two known blobs with `--auth-mode login` in Cloud Shell.
8. Assigned the VM identity **Storage Blob Data Reader only on `lab19-readable`**. Added `snet-vm` to the storage network rules, changed default action to Deny and bypass to None, and verified one allowed subnet with zero IP rules. Removed the exact temporary administrator data-role assignment and read back zero matching assignments at that account scope.
9. In the VM, retrieved a Storage-audience managed-identity token from IMDS into a shell variable and issued authenticated Blob REST requests. The permitted GET succeeded, while the write and cross-container GET were denied. Repeated the permitted GET successfully and unset the token. The token value was not printed; no storage keys, SAS or interactive Azure login inside the VM were used for these requests.
10. Inventoried the ten resources, deleted the lab group, verified its absence and removed the downloaded local private-key file.

The storage path used a **service endpoint and the normal public storage hostname**. Public network access remained Enabled with default Deny and one subnet exception. No private endpoint or private DNS resolution test was part of this lab.

## Validation results

| Check | Observed result | Conclusion and boundary |
|---|---|---|
| VM deployment | Succeeded; running; `Standard_B2ts_v2`; Canonical publisher; initial public IP empty | Captured live baseline, separate from setup forms |
| Bastion entry | Provisioning Succeeded; session requests failed | Bastion sign-in not validated; cause unresolved |
| Guest SSH readiness | Service active; listeners on `0.0.0.0:22` and `[::]:22` | Guest service readiness; does not prove Bastion session establishment |
| Server identity and SSH | Client/VM Agent fingerprints matched; `whoami` was `azureuser`, hostname was `vm-mrtg-lab19-01` | Successful fallback guest sign-in; source-rule evidence limit remains |
| Disk preparation | LUN 0 identified as the new 4 GiB disk; ext4 mounted; about 3.9 GiB filesystem | New data disk prepared and available |
| Persistent configuration | fstab verification reported no errors/warnings; unmount/remount checksum OK | UUID entry and data baseline passed the tested remount |
| Deallocation | Azure showed `VM deallocated` | Explicit deallocation observed |
| Increased capacity | Azure showed B2s_v2 running; guest 2 CPUs and 7.7 GiB reported memory | Resize observed in Azure and guest |
| Data after resize | Mount present after start; fixture content intact; SHA-256 check OK | Persistence across the first deallocate/resize/start cycle |
| Restored size | Azure showed B2ts_v2 running; final guest 2 CPUs and 840 MiB reported memory | Original capacity restored; usable memory differs from nominal RAM |
| Data after restoration | Mount present at `/mnt/mrtg-data`; SHA-256 check OK | Persistence across the return cycle despite device-name change |
| VM data-role scope | Storage Blob Data Reader; ServicePrincipal; `lab19-readable` container scope in command | Workload grant separated from administrator setup role |
| Permitted read | `GET lab19-readable/proof.txt`: HTTP 200 with expected content | Positive control for the tested identity/network path |
| Write denial | `PUT lab19-readable/write-probe.txt`: HTTP 403, `AuthorizationPermissionMismatch` | Reader could not create the tested blob |
| Cross-container denial | `GET lab19-restricted/proof.txt`: HTTP 403, same error code | Reader could not read the known seeded blob outside its scope |
| Final positive control | Permitted GET again returned HTTP 200 after both denials | Tested permitted path still worked; denials accompanied by a successful control |
| Administrator setup-role removal | Exact bootstrap assignment deleted; matching role count 0 at storage-account scope | Removes that temporary data role; no claim that all administrator access was revoked |
| Azure/local cleanup | Group existence false; downloaded key `Test-Path` False | Group removed and specified local file absent; unrelated resources/copies not audited |

The disk fixture contained `MRTG Lab 19 data persistence test` followed by a newline. Its baseline SHA-256 was `db321eb71397a68148eced1a60d99c6a84497ff26387b6b0574291f7ff6feb4b`. The checksum manifest was `~/lab19-data-baseline.sha256` on the OS disk. This tested persistence through the observed lifecycle changes, not backup restoration, disk relocation or disaster recovery.

## Troubleshooting and lessons

**Keep failed paths separate from completed objectives.** Bastion Developer session requests failed before and after an operator-reported delete/recreate attempt. Refresh and an InPrivate retry also failed. The published post-recreate image shows the continuing error; a separate delete/recreate operation log was not retained. The corrected InPrivate capture is included with its account label redacted. Neither successful provisioning nor the generic session error identifies the root cause, and no Azure outage or NSG cause was established.

Network Watcher IP flow verification rejected the proposed platform source as restricted address space. That output is an unsupported check, not a deny decision from the NSG. The Copilot diagnostic stated that it did not execute, then offered generic guidance. Its two captures preserve the failed diagnostic attempt; the suggested gateway/subnet instructions are not verified remediation for this Developer deployment.

**Run commands in the right environment.** Azure resource commands ran in Cloud Shell; guest disk and filesystem commands ran through SSH. The initial attempt to use `az` inside the VM returned `command not found`. Installing Azure CLI in the guest was unnecessary for the lifecycle operations or the managed-identity REST tests.

**Verify the host and protect the local key.** The server fingerprint was checked through VM Agent Run Command before acceptance. Windows OpenSSH initially rejected the downloaded private key because its file permissions were too broad. The operator corrected the local ACL before successful key-based sign-in; the submitted package contains the fingerprint and successful-session captures, not the ACL error/repair captures. That local problem was not established as the cause of the Bastion failure.

**Persist by filesystem identity.** The data partition was initially `/dev/sdb1`, then appeared as `/dev/sda1` in the final check. The UUID-based fstab entry still mounted the intended filesystem and its hash passed. Device letters are observations from one boot, not persistent identifiers. `nofail` permits boot to continue if the data disk is unavailable; monitoring would still need to detect that condition in an operational workload.

**Prove the permission boundary with controls.** An existing restricted-container fixture avoids confusing a missing blob with a permission failure. Successful reads before and after the denied operations strengthen the scoped-role result. A 403 by itself would not establish the same conclusion. These tests did not remove the VM's Reader role to measure revocation enforcement.

## Cleanup and costs

The final resource inventory contained VNet, NSG, SSH public-key resource, NIC, VM, OS disk, Bastion host, temporary public IP, data disk and storage account. Deleting `rg-mrtg-lab19-vm` completed; `az group exists` returned `false`. No workload in that group was retained. The subscription/directory/budget baseline and any unrelated resource groups were not removed or re-audited. Local private-key removal verified absence of the specified Downloads path, not secure erasure or removal of every possible copy.

| November 14 portal estimate | Displayed monthly amount | Scope |
|---|---|---|
| Original B2ts_v2 compute | USD 8.61 | Predeployment estimate |
| OS disk | USD 2.40 | Predeployment estimate |
| Initial displayed total | USD 11.01 | Original VM form, before later resources |
| B2s_v2 resize target | USD 68.62 | Displayed compute estimate for the temporary larger size |

These are historical portal estimates, not session spending, posted usage or invoice totals. The original total excludes later data-disk, public-IP and storage usage; it does not establish the final cost of diagnostics or other meters. Credits and final billed charges were not verified. Deallocation was used between capacity changes; the group was deleted at completion. A November 15 posted-usage review is recorded below; final billing remains unverified. [Series cost record](../../docs/cost-ledger.md).

### Cost review — November 15, 2026

The [author-redacted cost capture](screenshots/lab19-cost-review-2026-11-15.png) shows November 2026 Actual cost of **USD 0.05**, at billing-account scope filtered to `rg-mrtg-lab19-vm`. The service breakdown displays Virtual Machines USD 0.03, Storage USD 0.01, Virtual Network below USD 0.01 and Bandwidth below USD 0.01. Location and subscription breakdowns each show USD 0.05. Rounded components need not sum exactly to the displayed total.

This is a dated posted-usage snapshot, not a final invoice or verified out-of-pocket payment. Credits and later charges remain unverified. The selected view shows Budget None; this does not establish removal or absence of the subscription budget configured in Lab 01. Billing-name redactions preserve the filter, period, amounts and service categories.

**Cost follow-up — November 22, 2026:** The [author-redacted November review](screenshots/lab19-cost-review-2026-11-22.png) shows: Actual cost USD 0.05; VMs USD 0.03, Storage USD 0.01, Virtual Network and Bandwidth each below USD 0.01. This dated review preserves the earlier captures; no final invoice, applied credits or cash cost is verified. The selected-view Budget None does not establish absence of the subscription budget, which was separately revalidated in Lab 26.

## Evidence and limits

[The chronological gallery](screenshots/README.md) publishes **51 reviewed PNGs**: the 50 execution images, including the author-supplied corrected InPrivate capture, plus the November 15 author-redacted cost review. Files are published as supplied; the gallery distinguishes setup selections, live readbacks, successful tests, failed attempts and cleanup.

The SSH rule image is a pre-save form with the source CIDR omitted. There is no independent final effective-rule readback or connection-denial test from another source. Successful SSH does not fill that evidence gap. Bastion root cause and remediation remain unverified; candidate rules and unexecuted diagnostic guidance are not recommended configuration baselines.

The role and REST captures establish the tested container read/write boundary, not all possible storage operations or administrator least privilege. Storage-account setup-role removal was checked by assignment count; enforcement under a fresh administrator token and VM role-revocation behavior were not tested. No production workload, Entra OS login, backup restore, regional recovery, private endpoint or final billing validation is claimed.

[← Lab 18](../lab-18-reproducible-mrtg-deployment/README.md) · [Lab 20 →](../lab-20-disk-recovery-and-relocation/README.md)
