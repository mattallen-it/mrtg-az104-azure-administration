# Access-control matrix

**Status: subscription Owner inheritance observed; scoped Reader and Contributor tests validated in Lab 04.**

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

## Proposed data access

| Identity | Business need | Proposed role | Proposed scope | Expected allowed action | Expected denied action | Actual/evidence |
|---|---|---|---|---|---|---|
| MRTG-AZ104-Document-Readers | Read synthetic documents | Storage Blob Data Reader | One test container | Read a known blob | Upload or delete a blob | Pending |
| Test workload managed identity | Read required application data without stored credentials | Storage Blob Data Reader | One test container | Read the required blob | Write data or access another container | Pending |


These data-plane candidate permissions have not been assigned or tested in this series. Contributor is broad; its suitability depends on the workload operation. Future results must distinguish management-plane roles from storage data access.
