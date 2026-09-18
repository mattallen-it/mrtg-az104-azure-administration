# Access-control matrix

**Status: proposed test roles; access tests have not been performed.**

[Lab 01](../labs/lab-01-subscription-inventory-and-cost-baseline/README.md) verified the setup administrator’s Owner role on `MRTG-AZ104-Lab-Subscription`. That baseline does not validate the proposed least-privilege identities below.

| Identity | Business need | Proposed role | Proposed scope | Expected allowed action | Expected denied action | Actual/evidence |
|---|---|---|---|---|---|---|
| MRTG-AZ104-Readers | Inspect lab configuration | Reader | One lab resource group | Read resource properties | Modify resources | Pending |
| MRTG-AZ104-Operators | Operate a test workload | Contributor for broad lab operations; narrow when task permits | One lab resource group | Manage resources in scope | Assign Azure roles | Pending |
| MRTG-AZ104-Document-Readers | Read synthetic documents | Storage Blob Data Reader | One test container | Read a known blob | Upload or delete a blob | Pending |
| Test workload managed identity | Read required application data without stored credentials | Storage Blob Data Reader | One test container | Read the required blob | Write data or access another container | Pending |

These are candidate permissions, not automatic assignments. Confirm the minimum role needed for the actual task. Contributor is broader than a VM-specific operator role and requires justification.

For each test, record identity type, direct and inherited assignments, group memberships, control-plane versus data-plane access, test time, and sanitized evidence. Test using the intended identity, not the setup administrator. Check for inherited grants before interpreting an unexpected success.

For offboarding, record sign-in blocking, applicable session revocation, group/role removal, and retests with fresh authentication. Record propagation and token limitations. Do not assume deleting a resource group removes tenant identities.
