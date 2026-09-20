# Access-control matrix

**Status: administrator inheritance observed; least-privilege test roles remain proposed.**

## Observed administration access

| Identity | Role | Assignment source | Observed scope | Evidence |
|---|---|---|---|---|
| MRTG Cloud Operations | Owner | Subscription | Lab 02 Operations and Security resource groups, inherited | [Lab 02](../labs/lab-02-resource-organization-and-management-hierarchy/README.md); retained IAM capture covers Operations |

Both temporary groups were subsequently deleted. Lab 02 created no role assignments. The administrator reported that the inherited Owner role remained visible while the Security group's `Owner` tag was removed; no separate comparison capture was retained. This metadata check does not validate least-privilege access or a denied operation.

## Proposed workload access

| Identity | Business need | Proposed role | Proposed scope | Expected allowed action | Expected denied action | Actual/evidence |
|---|---|---|---|---|---|---|
| MRTG-AZ104-Readers | Inspect lab configuration | Reader | One lab resource group | Read resource properties | Modify resources | Pending |
| MRTG-AZ104-Operators | Operate a test workload | Contributor for broad lab operations; narrow when task permits | One lab resource group | Manage resources in scope | Assign Azure roles | Pending |
| MRTG-AZ104-Document-Readers | Read synthetic documents | Storage Blob Data Reader | One test container | Read a known blob | Upload or delete a blob | Pending |
| Test workload managed identity | Read required application data without stored credentials | Storage Blob Data Reader | One test container | Read the required blob | Write data or access another container | Pending |


These candidate permissions have not been assigned or tested in this series. Contributor is broad; its suitability depends on the workload operation. Future results will need to distinguish direct and inherited grants, management and data access, and actual allowed and denied operations under the intended identity.
