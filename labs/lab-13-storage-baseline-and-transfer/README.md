# Lab 13 — Storage baseline and transfer

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

**Performed:** November 1, 2026. **Outcome:** Three synthetic files uploaded and downloaded with Microsoft Entra authentication; all final SHA-256 comparisons matched. One initial CSV mismatch was detected and resolved by a fresh download. The temporary resource group was removed. Posted costs were not captured.

## Business problem

MRTG needs an administrator to transfer a small synthetic document collection to Azure Blob Storage and verify that the retrieved files preserve the original bytes. This exercise combines a storage baseline, identity-based authorization, transfer validation and cleanup.

## Configuration and access decisions

| Item | Implemented value |
|---|---|
| Resource group | `rg-mrtg-lab13-storage-transfer` |
| Storage account | `stmrtglab131101` |
| Region and storage | Central US; Standard general-purpose v2, LRS, Hot tier |
| Container | `lab13-transfer`; Private anonymous access level |
| Authentication | Microsoft Entra user account; default Entra authorization in portal enabled |
| Administrator data role | MRTG Cloud Operations (Guest), Storage Blob Data Contributor at storage-account scope |
| Network | Public network access enabled from all networks for workstation transfers; Microsoft network routing; no private endpoint |
| Security | Secure transfer required, minimum TLS 1.2, anonymous blob access disabled, account-key access disabled |
| Protection | Blob/container/classic file-share soft delete enabled for seven days; versioning, change feed and point-in-time restore disabled |
| Encryption | Microsoft-managed keys; infrastructure encryption disabled |
| Other options | Hierarchical namespace, SFTP, NFS v3, cross-tenant replication and Defender for Storage disabled |
| Tags | Environment: Lab; Project: MRTG-AZ104-Administration; Lab: Lab-13; Owner: MRTG-Cloud-Operations |

The Private container setting concerns anonymous access. The storage endpoint remained publicly reachable and required authorization. This lab did not reproduce Lab 12's private endpoint architecture. The pre-cleanup inventory showed exactly one storage account; virtual-network/private-endpoint resource labels in the creation wizard's tag review do not establish that those resources were deployed.

The administrator received a storage data role for transfers. The assignment covered this disposable storage account; a container-only scope would narrow access for an identity needing only that container. Separate reader/write-denial and revocation tests were not performed here.

## Work performed

1. Created the tagged resource group and storage account with the baseline above; deployment completed successfully.
2. Reviewed Storage Blob Data Contributor for the administrator at storage-account scope and proceeded with the assignment workflow. A separate assignment-completion capture was not retained; subsequent successful data operations support effective access.
3. Created the private `lab13-transfer` container.
4. Created three synthetic files on the Windows workstation under `C:\Users\Public\MRTG-Lab13\originals`.
5. Uploaded all three through the Azure portal. The blob list explicitly showed **Authentication method: Microsoft Entra user account**.
6. Downloaded the blobs into a separate `downloaded` directory, compared SHA-256 hashes, investigated a CSV mismatch and repeated the comparison.
7. Captured the one-account inventory, deleted the resource group and verified no matching group in the refreshed filtered list.

## Synthetic files and results

| File | Size shown in uploaded blob list | Initial comparison | Final comparison |
|---|---|---|---|
| `data-handling-note.txt` | 58 B | PASS | True — hashes match |
| `sample-assets.csv` | 73 B | FAIL | True — hashes match after fresh download |
| `transfer-test.txt` | 48 B | PASS | True — hashes match |

The collection contained a lab transfer message, two fictional asset records and a note identifying the data as synthetic. No real employee or customer data was used.

## Troubleshooting: CSV mismatch

The first comparison showed two passes and one failure for `sample-assets.csv`. A mismatch establishes that the compared bytes differ; it does not identify which step changed them. The next instruction was to preserve the mismatching copy and download the CSV again without opening/resaving it in Excel. The fresh download's SHA-256 matched the original, and the final three-file comparison showed True for every file.

The root cause was **not established**. Application resaving, encoding, line endings or selection of a different local copy were possibilities, not verified findings. No corruption within Azure Storage is inferred from this evidence. The initial mismatch and successful retry are both preserved in the [evidence gallery](screenshots/README.md).

## PowerShell used

Create the original synthetic collection once, before upload. Keep the originals unchanged throughout validation. These commands do not require an elevated PowerShell session.

```powershell
$lab = "$env:PUBLIC\MRTG-Lab13"
New-Item -ItemType Directory -Force -Path "$lab\originals", "$lab\downloaded" | Out-Null

"MRTG Lab 13 - Storage transfer integrity test." |
    Set-Content "$lab\originals\transfer-test.txt"

@"
AssetId,Department,Status
LAB-001,IT,Active
LAB-002,Operations,Inactive
"@ | Set-Content "$lab\originals\sample-assets.csv"

"Lab data only. No real customer or employee information." |
    Set-Content "$lab\originals\data-handling-note.txt"
```

After uploading through the portal and downloading into the separate directory, the final comparison used:

```powershell
$lab = "$env:PUBLIC\MRTG-Lab13"
$results = foreach ($file in Get-ChildItem "$lab\originals" -File) {
    $download = Join-Path "$lab\downloaded" $file.Name
    [pscustomobject]@{
        File = $file.Name
        Match = if (Test-Path -LiteralPath $download) {
            (Get-FileHash $file.FullName -Algorithm SHA256).Hash -eq
            (Get-FileHash $download -Algorithm SHA256).Hash
        } else { $false }
    }
}
$results | Format-Table -AutoSize
```

This compares each original against its same-named download and reports False for a missing download. It does not reject extra files in the download directory. File creation defaults can differ across PowerShell versions; validation compares the actual original and downloaded bytes rather than assuming a universal expected hash.

## Validation and evidence limits

| Check | Observed evidence |
|---|---|
| Baseline and deployment | Creation settings, review panes and successful deployment capture |
| Container privacy | Container list showed Private |
| Identity-based data access | Data-role review and successful upload list showing Microsoft Entra user authentication |
| Integrity control detects a difference | Initial CSV comparison returned FAIL |
| Recovery and final integrity | Fresh CSV hash matched; all three final comparisons returned True |
| Cleanup | One storage account before deletion; no matching resource group afterward |
| Cost | No posted Lab 13 cost review captured; amount unverified |

No AzCopy/Storage Explorer transfer, anonymous-access denial, role-removal enforcement, cross-identity boundary, soft-delete recovery, version restore or replication test was performed. Protection settings were configured, not functionally tested. Matching SHA-256 hashes establish content equality for these local comparison pairs; they do not establish a production compliance posture or a signed chain of custody.

## Cleanup and cost

Deleted `rg-mrtg-lab13-storage-transfer` after validation. The sanitized cleanup screenshot shows no matching resource group under the selected subscription filter. All 19 reviewed screenshots, including the pre-cleanup inventory and post-deletion evidence, are published in the gallery. Local synthetic files and evidence were retained. This was not a subscription-wide resource audit.

One Standard LRS storage account was the only resource shown in the lab group. No paid Entra/Microsoft 365 user license or trial was used. Storage capacity, operations and transfer can incur Azure charges. No numeric final cost was supplied, and zero cost is not assumed; see the [cost ledger](../../docs/cost-ledger.md).

## Lessons learned

- Data authorization and network reachability are separate controls; a private container can use a public endpoint with authenticated access.
- A completed upload is not sufficient evidence of content integrity. Compare the retrieved bytes with the retained originals.
- Keep an initial failure and successful retest together. Record an unknown root cause honestly instead of turning a possible explanation into a finding.
- Preserve evidence and verify cleanup before moving to the next disposable deployment.

[Screenshot gallery](screenshots/README.md) · [All labs](../../docs/progress.md) · [Access matrix](../../docs/access-control-matrix.md)
