# Access-control matrix

**Status: subscription Owner inheritance observed; scoped Reader and Contributor tests validated in Lab 04; manual least-privilege remediation validated in Lab 07.**

## Observed administration access

| Identity | Role | Assignment source | Observed scope | Evidence |
|---|---|---|---|---|
| MRTG Cloud Operations | Owner | Subscription | Lab 02 Operations and Security resource groups, inherited | [Lab 02](../labs/lab-02-resource-organization-and-management-hierarchy/README.md); retained IAM capture covers Operations |

Both temporary groups were subsequently deleted. Lab 02 created no role assignments. The administrator reported that the inherited Owner role remained visible while the Security group's `Owner` tag was removed; no separate comparison capture was retained. This metadata check does not validate least-privilege access or a denied operation.

## Observed directory lifecycle

[Lab 03](../labs/lab-03-employee-and-contractor-lifecycle/README.md) demonstrated assigned security-group membership changes without attaching Azure RBAC or application permissions.

| Identity | Initial groups | Transfer/offboarding result | Cleanup |
|---|---|---|---|
| MRTG Lab Employee | Employees, Operations | Employees, Security; Operations removed | Active identity removed; permanent deletion operator-confirmed |
| MRTG Lab Contractor | Contractors, Operations | Disabled; no group memberships before deletion | Recoverable deletion captured; permanent deletion operator-confirmed |

Groups used the `MRTG-AZ104-` prefix and were deleted afterward. Session revocation for both users was operator-confirmed, not tested against an active application session. No fresh sign-in denial, application authorization, or Azure RBAC test was captured.

## Lab 04 — Scoped administration

Two synthetic Member users each belonged to one assigned security group. [Lab 04](../labs/lab-04-scoped-administration/README.md) captured their Azure RBAC assignments **at the Operations resource-group scope**, along with allowed and denied operations. The separate Security resource group had no Lab 04 assignment; the Operator received a 401 there.

| Test identity via security group | Azure role | Scope | Allowed observation | Denied observation | Cleanup |
|---|---|---|---|---|---|
| MRTG Lab Reader via `MRTG-AZ104-Lab04-Readers` | Reader | Operations resource group | Tags visible | Saving changed `Environment` tag returned `AuthorizationFailed`; original value persisted | Group and resource group absent from filtered cleanup lists; user absent from active list; role removal operator-confirmed |
| MRTG Lab Operator via `MRTG-AZ104-Lab04-Operators` | Contributor | Operations resource group | `Environment` changed to `Test`, then restored to `Lab` | Security group overview returned 401; **Add role assignment** disabled in Operations IAM | Group and resource group absent from filtered cleanup lists; user absent from active list; role removal operator-confirmed |

The Reader rejection screenshot identifies `lab04.reader` in the portal header. The inherited subscription Owner entry belongs to the administrator, not either test group. Cleanup captures do not establish permanent user deletion or independently show removal of each role assignment.

## Lab 06 — Administrator-assisted recovery

| Identity | Observed operation | Evidence and boundary |
|---|---|---|
| Existing lab administrator | Reset the synthetic cloud-only Member's password successfully | [Lab 06](../labs/lab-06-password-recovery-and-licensing/README.md); reset confirmation and successful audit event with named target; minimum role not separately tested |
| MRTG Lab06 Recovery User | Initial sign-in, required password change, and recovered sign-in | Account-page captures and successful password-change audit event; screenshots do not independently prove the submitted secret or session freshness |

No added group or role assignments were shown at creation. The recovery account was removed from active users; permanent deletion was not verified. SSPR, MFA reset, session-revocation enforcement, and application authorization were not tested.

## Lab 07 — Manual access review

| Identity via group | Business need | Finding and correction | Validation | Cleanup |
|---|---|---|---|---|
| MRTG Lab07 Review User via `MRTG-Lab07-Reviewers` | Read the temporary review resource group | Contributor exceeded the need; removed and replaced with Reader at resource-group scope | Check access showed group-derived Reader; reviewer loaded Overview; tag save returned AuthorizationFailed | Group role removed before resource-group deletion; group absent from search and user absent from active list |

[Lab 07](../labs/lab-07-access-review-and-cost-review/README.md) distinguishes the group's administrator owner from its sole reviewer member. The existing subscription Owner remained inherited. No automated Entra Access Reviews, PIM, data-plane authorization, or post-removal session enforcement was tested.

## Lab 12 — Managed identity and network access

| Identity | Role and scope | Observed result | Evidence limit |
|---|---|---|---|
| MRTG Cloud Operations | Subscription Owner; Storage Blob Data Contributor at storage-account scope | Entra-authenticated blob upload/read baseline; home portal later returned 403 under network restrictions | Network rejection does not prove a missing RBAC permission |
| `vm-mrtg-lab12-client` system-assigned managed identity | Storage Blob Data Reader on `lab12-evidence` container | IMDS-issued token used for HTTP 200 blob reads through service endpoint and private endpoint | No write-denial, other-container or role-removal enforcement test |

[Lab 12](../labs/lab-12-private-access-and-administrator-entry/README.md) separated identity authorization from network reachability. The final read succeeded with public network access disabled and private DNS resolving to `10.120.20.4`. The lab resource group was deleted after validation.

## Lab 13 — Administrator storage transfers

| Identity | Role and scope | Observed result | Evidence limit |
|---|---|---|---|
| MRTG Cloud Operations (Guest) | Storage Blob Data Contributor at `stmrtglab131101` storage-account scope | Three synthetic blobs uploaded with portal authentication explicitly showing Microsoft Entra user account; downloaded files ultimately matched local SHA-256 hashes | Role review and successful operations captured; no separate post-assignment IAM capture, write-denial, revocation or other-identity test |

[Lab 13](../labs/lab-13-storage-baseline-and-transfer/README.md) used disabled account-key access and disabled anonymous blob access. The data role covered the temporary account rather than one container; this was an administrator transfer exercise, not a read-only boundary test. The resource group was removed.

## Proposed additional data access

| Identity | Business need | Proposed role | Proposed scope | Expected allowed action | Expected denied action | Actual/evidence |
|---|---|---|---|---|---|---|
| MRTG-AZ104-Document-Readers | Read synthetic documents | Storage Blob Data Reader | One test container | Read a known blob | Upload or delete a blob | Pending |


The proposed document-reader group above has not been assigned or tested. The workload managed-identity read was tested separately in Lab 12. Contributor is broad; its suitability depends on the workload operation. Future results must distinguish management-plane roles from storage data access.

## Lab 16 — Department file access validated

| Identity or path | Share-level permission | Folder permission | Observed operation |
|---|---|---|---|
| `MRTG\lab16.finance` via `GG-Lab16-Finance` | Default Storage File Data SMB Share Contributor | Root Read/Execute; Finance Modify | Finance seed read and file create/readback succeeded; HR seed read denied |
| `MRTG\lab16.hr` via `GG-Lab16-HR` | Same default permission | Root Read/Execute; HR Modify | HR seed read and file create/readback succeeded; Finance seed read denied |
| Administrator with storage key | Administrative bootstrap | Applied root and folder ACLs | Setup only; not used as explicit credentials in department tests |
| Initial portal access-key session | Administrative access | Not a per-user boundary test | Share-snapshot recovery and visual content check |

[Lab 16](../labs/lab-16-department-file-access-and-the-ad-bridge/README.md) rebuilt storage with AD DS registration in `mrtg.local`. Both users obtained AES-256 CIFS Kerberos tickets from MRTG-DC02 and reached the private endpoint at `10.160.1.4` over P2S VPN. Certificate-based VPN admission and domain-user file authentication are distinct controls. The department groups also received CLIENT01 local Remote Desktop Users membership for sign-in; this did not grant local administrator rights.

Default share permission applied to authenticated identities; Windows folder ACLs enforced the department boundary. No department-specific Azure RBAC assignment or Entra identity synchronization was tested. Cross-folder write/delete, ACL changes and permission-revocation enforcement were not separately tested. Azure resources, the temporary hosts entry and the storage AD computer object were removed. Local department identities/groups and client RDP memberships were retained.

## Lab 18 — Deployment management plane

| Identity or control | Observed operation | Evidence and boundary |
|---|---|---|
| Existing lab administrator in Cloud Shell | Created/deleted the lab group; deployed NSG, VNet and storage; read configuration and outputs | [Lab 18](../labs/lab-18-reproducible-mrtg-deployment/README.md); no new role assignment, deployment identity or minimum-role/denied-permission test |
| Storage security configuration | Public network, Shared Key and anonymous blob access disabled; HTTPS and TLS 1.2 read back | Configuration only; no private endpoint or data-plane authentication test |
| Resource-provider validation | NSG priority 99 rejected; existing priority 1000 read back | Input validation, not an identity authorization denial or partial-deployment rollback |

The subscription administrator role baseline was not independently re-audited for this exercise. The rebuild adds matching outputs, source checksums and a no-change plan; explicit security readbacks were captured before rebuild. The disposable group was removed. No Lab 18 least-privilege, credential rotation or revocation claim is made.
