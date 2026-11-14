# Lab 18 — Reproducible MRTG deployment

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

[Portfolio](../../README.md) · [All labs](../../docs/progress.md) · [Evidence gallery](screenshots/README.md) · [Deployment files](deployment/README.md)

## Outcome

**Validated:** deployed a parameterized Bicep baseline, inspected and applied a tag change, rejected an invalid NSG priority at provider preflight validation, restored the baseline, then deleted and rebuilt the resource group from unchanged source. The saved deployment outputs matched byte for byte, both source checksums passed, and the final what-if reported **3 no change**. Final deletion was verified with `az group exists` returning `false`.

Executed November 13, 2026 local time (November 14 UTC). Twenty reviewed screenshots and all six submitted deployment artifacts are published. This is infrastructure configuration and rebuild evidence; workload traffic and storage data access were not tested.

## Business problem

MRTG needs infrastructure that another administrator can review and recreate without reconstructing portal clicks. The exercise separates intended changes, live configuration readback, invalid-input rejection and a clean rebuild. Preserving the source and parameter hashes makes the tested baseline reviewable for an operations handover.

## Environment and decisions

| Item | Tested configuration |
|---|---|
| Execution | Azure Cloud Shell Bash, ephemeral session; existing lab administrator and enabled `MRTG-AZ104-Lab-Subscription` |
| Tooling | Bicep CLI 0.49.2 installed after the initial missing-CLI message; successful Bicep build captured |
| Scope | Resource-group deployment into `rg-mrtg-lab18-iac`, `centralus` |
| Network | `vnet-mrtg-lab18`, `10.180.0.0/16`; inline `snet-app`, `10.180.10.0/24` |
| NSG | `nsg-mrtg-lab18-app`, associated with `snet-app`; custom `Deny-All-Inbound`, priority 1000, all protocols/ports/addresses |
| Storage | Generated `stl18${uniqueString(resourceGroup().id)}` name; observed `stl185rfhirowkw57g`; StorageV2, Standard_LRS, Hot |
| Storage controls | HTTPS required, minimum TLS 1.2; public network access disabled, anonymous blob access disabled, Shared Key access disabled |
| Parameters | `location=centralus`, `environment=Lab` (allowed: Lab/Test), `inboundRulePriority=1000` |
| Tags | Environment from parameter; Project `MRTG-AZ104-Administration`, Lab `Lab-18`, Owner `MRTG-Cloud-Operations` |

The template declares an NSG, VNet with an inline subnet and storage account. The compiled ARM template includes the VNet dependency on the NSG. No VM, VPN gateway, Bastion, private endpoint, new identity or role assignment was deployed. Disabling storage public access without a private endpoint was intentional for this configuration exercise; a usable private data path was not demonstrated.

## Work performed

1. Selected and checked the subscription; installed Bicep; created `~/mrtg-lab18` and compiled `main.bicep` to `main.json` with build exit code 0. Inspected the three resource types.
2. Created the tagged resource group. Initial what-if predicted three creates. Deployed `lab18-baseline` successfully with `environment=Lab` and priority 1000.
3. Read back the resource inventory, storage security settings, NSG rule and subnet association. Saved the baseline parameter file and SHA-256 manifest.
4. Repeated what-if using `@baseline.parameters.json`: three resources showed no change.
5. Overrode `environment=Test` on the CLI. What-if predicted only the three Environment tag changes; `lab18-environment-test` succeeded and all three live resource tags read back as Test.
6. Submitted `lab18-invalid-priority` with priority 99. Azure returned `InvalidTemplateDeployment` with inner `SecurityRuleInvalidPriority`; CLI exit code was 1. Readback still showed the existing rule at priority 1000.
7. Deployed `lab18-baseline-restored` from the baseline parameters successfully, with output Environment Lab. Verified both source hashes and exported `baseline-outputs.json`.
8. Downloaded the baseline source archive before destructive testing. Deleted the resource group and verified absence with `az group exists=false`.
9. Recreated the same resource group in the same subscription and location. Deployed `lab18-rebuild` from unchanged Bicep and baseline parameters; deployment succeeded with the same four output values.
10. Exported `rebuild-outputs.json`; `diff -u` returned exit code 0, and both source hashes passed again. Final what-if reported three resources with no change.
11. Downloaded the six-file deployment package, deleted the resource group again and verified `false`.

The [deployment guide](deployment/README.md) provides the preserved files, replay commands and the boundaries of the comparison. Publication did not deploy anything to Azure.

## Validation results

| Check | Observed result | Evidence |
|---|---|---|
| Build and intended resources | Build exit 0; NSG, VNet and storage resource types | [Build](screenshots/lab18-bicep-build-verified.png), [types and group](screenshots/lab18-template-resources-and-resource-group.png) |
| Initial plan and deployment | Three creates; baseline Succeeded, Environment Lab | [NSG plan](screenshots/lab18-initial-what-if-nsg.png), [network/storage plan](screenshots/lab18-initial-what-if-network-storage-summary.png), [baseline](screenshots/lab18-baseline-deployment-succeeded.png) |
| Live baseline configuration | Three Central US resources tagged Lab; storage controls and NSG/subnet association read back | [Inventory](screenshots/lab18-baseline-resource-inventory.png), [storage](screenshots/lab18-storage-security-settings-verified.png), [NSG/subnet](screenshots/lab18-nsg-rule-and-subnet-association-verified.png) |
| Repeat plan | Three no change | [Baseline what-if](screenshots/lab18-baseline-repeat-what-if.png) |
| Parameter override | Three tag-only modifications predicted; deployment Succeeded and all three live tags Test | [Change plan](screenshots/lab18-environment-tag-change-what-if.png), [applied change](screenshots/lab18-environment-tag-change-applied.png) |
| Invalid input | Priority 99 rejected at preflight; allowed range 100–4096; exit 1 | [Expected rejection](screenshots/lab18-invalid-nsg-priority-rejected.png) |
| Restore | Existing priority 1000 readback; baseline restoration Succeeded with Environment Lab | [Rule and restoration](screenshots/lab18-valid-priority-and-baseline-restored.png) |
| Clean rebuild | Original group absent; recreated group and `lab18-rebuild` Succeeded | [Pre-rebuild deletion](screenshots/lab18-resource-group-removed-before-rebuild.png), [rebuild](screenshots/lab18-clean-rebuild-succeeded.png) |
| Reproducibility checks | Output diff exit 0; main.bicep and baseline.parameters.json hashes OK; final plan three no change | [Comparison](screenshots/lab18-rebuild-outputs-and-source-match.png), [final plan](screenshots/lab18-rebuild-what-if-no-change.png) |
| Final cleanup | Resource group existence returned false | [Final deletion](screenshots/lab18-final-resource-group-cleanup-verified.png) |

The submitted source files independently match their SHA-256 manifest, and the two submitted output JSON files are byte-identical. The compiled JSON was parsed and reviewed during publication; no new local Bicep compilation or Azure execution was performed for the repository update.

## Troubleshooting and lessons

- **Missing Bicep CLI:** `az bicep install` resolved the initial error; version 0.49.2 was then verified. Ephemeral Cloud Shell requires downloading work before the session is lost.
- **Expected invalid priority:** the original source deliberately accepts an integer so Azure can demonstrate provider validation. Priority 99 was rejected before deployment. This is not a partially applied deployment or an automatic rollback test. Production templates could add `@minValue(100)` and `@maxValue(4096)` to catch bad input earlier; the published tested source is preserved unchanged.
- **Restore versus rebuild:** reapplying baseline parameters restored the intended environment value. The later delete/recreate cycle tested reconstruction from source; it did not restore workload data.
- **Evidence strength:** matching outputs establishes equality of the four exported values. Checksums establish unchanged Bicep and parameter bytes. A no-change what-if is a prediction for the template, not a comparison of every resource property or proof of application availability.

## Cleanup and costs

The resource group was deleted before the clean rebuild and again after final validation. Both checks returned `false`. No Lab 18 workload was retained at the end of the captured session. The subscription, existing directory and any unrelated/shared resources were outside this cleanup check; budget alerts were not revalidated.

The deployment contained an empty Standard LRS Hot storage account and network configuration, without compute, a gateway or a private endpoint. **No numeric session estimate or posted Lab 18 cost capture was supplied.** Credits, invoiced cash cost and final charges remain unverified; removal does not establish zero cost. See the [cost ledger](../../docs/cost-ledger.md).

## Evidence and limits

[Twenty-screenshot gallery](screenshots/README.md) · [Original deployment artifacts and replay guide](deployment/README.md)

- Submitted screenshots were reviewed with subscription/tracking identifiers redacted; the original submitted image bytes are preserved. The source contains no account keys, credentials or literal subscription identifier.
- Rebuild was tested in the same subscription with the same resource-group name. A different scope changes the generated storage name; global name availability and cross-subscription portability were not tested.
- Storage controls, NSG priority and subnet association were explicitly read back before the rebuild. The rebuild evidence adds deployment success, output equality and what-if consistency; those individual security readbacks were not repeated afterward.
- No workload traffic, data-plane authentication, least-privilege deployment role, RBAC denial, permission revocation, partial-deployment recovery or data restore was tested. The priority rejection is a resource-provider validation result, not an authorization denial.
- Final cleanup is scoped to the named group. No final billing, remaining-credit or whole-subscription inventory claim is made.

[← Lab 17](../lab-17-replication-and-storage-incident-drill/README.md) · [Lab 19 →](../lab-19-vm-lifecycle/README.md)
