# Lab 18 deployment artifacts

These six files are preserved byte for byte from the submitted Cloud Shell download. They document the tested deployment; publishing this folder does not execute a deployment.

| File | Purpose |
|---|---|
| [main.bicep](main.bicep) | Tested resource-group Bicep source: NSG, VNet with inline subnet, storage account |
| [main.json](main.json) | Compiled ARM artifact from the captured successful Bicep build |
| [baseline.parameters.json](baseline.parameters.json) | Environment Lab and inbound priority 1000 |
| [baseline-source.sha256](baseline-source.sha256) | SHA-256 manifest for main.bicep and baseline.parameters.json |
| [baseline-outputs.json](baseline-outputs.json) | Four outputs exported from lab18-baseline-restored |
| [rebuild-outputs.json](rebuild-outputs.json) | Four outputs exported from lab18-rebuild; byte-identical to baseline |

## Verify downloaded files

Run from this folder in Bash:

```bash
sha256sum -c baseline-source.sha256
diff -u baseline-outputs.json rebuild-outputs.json
```

Both source checksums pass. The output diff is empty with exit code 0. These checks cover the listed files and four exported output values, not every live resource property. The compiled JSON is included as build evidence; it is not covered by the submitted source manifest.

## Replay the baseline

The original environment used Azure Cloud Shell Bash and Bicep CLI 0.49.2. Choose and verify your intended lab subscription before running commands. Review current cost, permissions and region prerequisites. The following commands create Azure resources; they are a replay guide and were not executed during publication.

```bash
az account set --subscription "MRTG-AZ104-Lab-Subscription"
az account show --query '{Subscription:name,State:state}' --output table
az bicep version
# If Bicep is missing: az bicep install
sha256sum -c baseline-source.sha256

lab18Rg="rg-mrtg-lab18-iac"
az group create --name "$lab18Rg" --location centralus \
  --tags Environment=Lab Project=MRTG-AZ104-Administration Lab=Lab-18 Owner=MRTG-Cloud-Operations

az deployment group what-if --resource-group "$lab18Rg" \
  --template-file main.bicep --parameters @baseline.parameters.json

az deployment group create --name lab18-baseline \
  --resource-group "$lab18Rg" --template-file main.bicep \
  --parameters @baseline.parameters.json
```

The storage name depends on the resource-group ID. The observed name was `stl185rfhirowkw57g`; do not hard-code it for another subscription or scope. The template disables public storage access without creating a private endpoint, so this guide alone does not provide a data-access path. No new Azure RBAC assignment is included.

## Controlled change and rejection

Append `environment=Test` after `@baseline.parameters.json` to preview and apply the tag override. The captured plan showed only three Environment tag changes; the applied inventory showed all three as Test.

The deliberate rejection command was:

```bash
az deployment group create --name lab18-invalid-priority \
  --resource-group "$lab18Rg" --template-file main.bicep \
  --parameters @baseline.parameters.json environment=Test inboundRulePriority=99 \
  --output none
echo "Deployment exit code: $?"
```

Azure rejected priority 99 during provider preflight validation with `SecurityRuleInvalidPriority` and exit 1. The unchanged original source leaves the integer unbounded to permit that provider test. This does not demonstrate rollback. The operator checked that priority 1000 remained and applied baseline parameters as `lab18-baseline-restored`.

## Clean rebuild and comparison

The captured test exported outputs, verified source hashes and downloaded the baseline before deleting the original group. Group absence returned false from `az group exists`. Recreating the same group and deploying the same source/parameters as `lab18-rebuild` succeeded. To reproduce the saved output comparison, export `properties.outputs` from each successful deployment before deleting its group:

```bash
az deployment group show --resource-group "$lab18Rg" \
  --name lab18-baseline-restored --query properties.outputs \
  --output json > baseline-outputs.json
# After deleting/recreating the group and deploying lab18-rebuild:
az deployment group show --resource-group "$lab18Rg" \
  --name lab18-rebuild --query properties.outputs \
  --output json > rebuild-outputs.json
diff -u baseline-outputs.json rebuild-outputs.json
sha256sum -c baseline-source.sha256
az deployment group what-if --resource-group "$lab18Rg" \
  --template-file main.bicep --parameters @baseline.parameters.json
```

Rebuild validation showed an empty output diff, passing source hashes and three no-change resources. It did not independently repeat every initial security readback or test traffic. Download your files before ending an ephemeral Cloud Shell session.

## Cleanup

After retaining the desired evidence, the operator deleted only the disposable Lab 18 group:

```bash
az group delete --name "$lab18Rg" --yes
az group exists --name "$lab18Rg"
```

The captured final result was `false`. Deletion removes the group and its deployment history; retain the evidence first. No final cost capture was supplied.

[Lab results](../README.md) · [Evidence gallery](../screenshots/README.md)
