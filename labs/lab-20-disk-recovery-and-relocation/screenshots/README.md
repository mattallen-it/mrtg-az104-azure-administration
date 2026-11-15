# Lab 20 evidence gallery

**36 published screenshots.**

All published PNGs preserve the supplied bytes: 34 images from the ZIP and two author-supplied redacted replacements for the upper VM-review and final resource-group cleanup-list captures. No private keys, tokens or connection credentials are included.

| Capture | What it establishes and limits |
|---|---|
| [lab20-baseline-snapshot-created.png](lab20-baseline-snapshot-created.png) | Live snapshot: Incremental, Standard_ZRS, completion 100, Succeeded, Available and DenyAll. Gen 1 is snapshot metadata for a data disk, not the VM generation. |
| [lab20-data-disk-attached.png](lab20-data-disk-attached.png) | Portal disk row: LUN 0, 4 GiB, Standard SSD LRS, caching None. Editing controls are visible; guest identification separately establishes attachment. Delete with VM is not visible. |
| [lab20-data-disk-device-identified.png](lab20-data-disk-device-identified.png) | Guest LUN 0 link points to sdb; 4 GiB disk separate from OS disk. |
| [lab20-data-disk-formatted-and-mounted.png](lab20-data-disk-formatted-and-mounted.png) | GPT/ext4 creation, mount, ownership and usable filesystem size. |
| [lab20-data-filesystem-unmounted.png](lab20-data-filesystem-unmounted.png) | Source data partition unmounted before snapshot creation. |
| [lab20-data-filesystems-unmounted-for-cleanup.png](lab20-data-filesystems-unmounted-for-cleanup.png) | Both data partitions have no mountpoint before final cleanup. |
| [lab20-files-and-checksum-baseline.png](lab20-files-and-checksum-baseline.png) | Three synthetic fixtures, original SHA-256 values and three OK checks; manifest saved on OS disk. |
| [lab20-local-private-key-removal-verified.png](lab20-local-private-key-removal-verified.png) | Specified Downloads path removed; Test-Path False. Does not prove secure erasure or absence of other copies. |
| [lab20-nsg-subnet-associated.png](lab20-nsg-subnet-associated.png) | Saved NSG association with snet-vm in vnet-mrtg-lab20. |
| [lab20-original-data-loss-and-change-detected.png](lab20-original-data-loss-and-change-detected.png) | Expected failure: proof missing, CSV OK, configuration hash mismatch after version 2 overwrite. |
| [lab20-post-relocation-integrity-verified.png](lab20-post-relocation-integrity-verified.png) | Read-only recovered mount after relocation/reattachment; three OK hashes, proof text and version=1. |
| [lab20-recovered-filesystem-unmounted-before-move.png](lab20-recovered-filesystem-unmounted-before-move.png) | Recovered partition unmounted before detachment; original remains mounted. |
| [lab20-relocated-disk-reattached-and-identified.png](lab20-relocated-disk-reattached-and-identified.png) | After move/reattachment: LUN 1 points to sdc, ext4 unmounted; duplicate UUID remains. |
| [lab20-resource-groups-created.png](lab20-resource-groups-created.png) | Source and recovery groups visible in Central US; no tag readback in this view. |
| [lab20-restored-disk-detached-before-move.png](lab20-restored-disk-detached-before-move.png) | Live Unattached disk in source group: Copy from baseline snapshot, 4 GiB Standard SSD LRS, completion 100, Succeeded and DenyAll. |
| [lab20-restored-disk-device-identified.png](lab20-restored-disk-device-identified.png) | Before move: LUN 0 original and LUN 1 restored devices; same filesystem UUID. |
| [lab20-restored-disk-resource-group-move-verified.png](lab20-restored-disk-resource-group-move-verified.png) | Live disk in recovery group, same name/location/type, Unattached and DenyAll. Separate move operation log not supplied. |
| [lab20-restored-disk-review-configuration.png](lab20-restored-disk-review-configuration.png) | Validated pre-create form: snapshot source, source group, 4 GiB Standard SSD LRS, no zone and DenyAll. Not deployment completion by itself. |
| [lab20-snapshot-recovery-integrity-verified.png](lab20-snapshot-recovery-integrity-verified.png) | Initial recovery: read-only mount; all three hashes OK, deleted proof restored and version=1. |
| [lab20-snapshot-review-configuration.png](lab20-snapshot-review-configuration.png) | Final pre-create form: Incremental, Standard_ZRS and DenyAll. Tags list Disk access and Snapshot targets; this does not prove a DiskAccess resource or private endpoint exists. |
| [lab20-ssh-rule-saved.png](lab20-ssh-rule-saved.png) | Saved Allow-SSH-MyIP, priority 100, TCP 22 to subnet /24. Source value redacted; no independent source-CIDR or external-denial proof. |
| [lab20-ssh-service-and-host-fingerprint.png](lab20-ssh-service-and-host-fingerprint.png) | VM Agent Run Command: expected hostname, active SSH and ED25519 SHA-256 fingerprint. Client comparison was operator-observed, not supplied in ZIP. |
| [lab20-ssh-session-verified.png](lab20-ssh-session-verified.png) | Successful guest whoami and hostname. Does not independently show ACL repair or source restriction. |
| [lab20-vm-advanced-configuration.png](lab20-vm-advanced-configuration.png) | Setup: no extensions/apps/custom data, SQL unchecked, no capacity reservation. |
| [lab20-vm-basics-configuration.png](lab20-vm-basics-configuration.png) | Setup: group/name/region, Ubuntu image, B2ts_v2, RSA SSH, inbound ports None; monthly estimate, not usage. |
| [lab20-vm-deployment-verified.png](lab20-vm-deployment-verified.png) | Live VM Running, agent Ready, Canonical Ubuntu, Gen2/x64, private IP, Trusted Launch/Secure Boot/vTPM and no data disks yet. Subscription/public IP values already redacted. |
| [lab20-vm-management-configuration.png](lab20-vm-management-configuration.png) | Setup: identity/Entra login/auto-shutdown/assessment/hibernation off; image-default patching. |
| [lab20-vm-monitoring-configuration.png](lab20-vm-monitoring-configuration.png) | Setup: managed boot diagnostics on, guest diagnostics/alerts/application health off. |
| [lab20-vm-networking-configuration.png](lab20-vm-networking-configuration.png) | Setup: expected subnet/public IP, no NIC NSG, subnet-NSG notice, accelerated networking required/on, no load balancing. Monthly estimate only. |
| [lab20-vm-os-disk-configuration.png](lab20-vm-os-disk-configuration.png) | Setup: image default 30 GiB, Standard SSD, platform-managed key; no data disks yet. Cost pane uses a billing tier, not a different guest disk size. |
| [lab20-vm-resource-tags.png](lab20-vm-resource-tags.png) | Setup tags applied to all selected deployment resources; live overview separately shows VM tags. |
| [lab20-vm-review-network-management-tags.png](lab20-vm-review-network-management-tags.png) | Final review: networking, identity off, backup/Site Recovery off, managed boot diagnostics on, SCSI and tags. |
| [lab20-vnet-address-space-and-subnet.png](lab20-vnet-address-space-and-subnet.png) | Pre-create form: /16 and single /24 subnet; no NAT shown. |
| [lab20-vnet-review-configuration.png](lab20-vnet-review-configuration.png) | Validated pre-create form: correct group/name/region, private subnet and tags; Bastion/Firewall/paid DDoS disabled. |

| [lab20-vm-review-basics-and-disk.png](lab20-vm-review-basics-and-disk.png) | Author-supplied email-redacted final review: Ubuntu, size, Trusted Launch, Secure Boot/vTPM, SSH and OS-disk settings; fictional MRTG account label retained. Setup and estimates, not live-state or billing evidence. |
| [lab20-resource-groups-cleanup-verified.png](lab20-resource-groups-cleanup-verified.png) | Author-supplied directory-redacted final portal list: no matching rg-mrtg-lab20 groups in selected subscription. Scope is the filter, not whole-subscription inventory. |

The client host-key comparison, private-key ACL correction, move activity log, final detach/deletion operations, data-disk Delete with VM setting and posted costs were not supplied as publishable captures. No effective-source or independent denied-source SSH test is claimed.

[Lab results](../README.md) · [Portfolio](../../../README.md)
