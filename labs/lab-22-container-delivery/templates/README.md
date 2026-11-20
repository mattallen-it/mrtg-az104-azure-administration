# Lab 22 deployment artifacts

These are the original uploaded working ARM templates, preserved byte for byte. Their SHA-256 values matched the Cloud Shell capture. Duplicate uploads had the same hashes.

| File | Purpose |
|---|---|
| [lab22-environment.json](lab22-environment.json) | Central US Consumption-profile environment; API 2024-03-01; appLogsConfiguration omitted |
| [lab22-app.json](lab22-app.json) | Container App with user-assigned identity registry pull, HTTPS ingress to port 80, 0.25 vCPU / 0.5 GiB, replica bounds 0–1 |
| [SHA256SUMS](SHA256SUMS) | SHA-256 checksums of both original JSON files |

## Prerequisites and execution limits

These templates do not create the resource group, Basic registry, imported mrtg-web:v1 image, id-mrtg-lab22-pull identity or registry-scoped AcrPull assignment. Supply those first, then deploy environment before app. Registry server is an app parameter; resource IDs resolve within the deployment subscription/group. Names and region are lab-specific. Running these commands creates billable Azure resources.

```bash
az deployment group create \
  --resource-group rg-mrtg-lab22-containers \
  --name lab22-environment \
  --template-file lab22-environment.json

az deployment group create \
  --resource-group rg-mrtg-lab22-containers \
  --name lab22-containerapp \
  --template-file lab22-app.json \
  --parameters registryServer="$LAB22_LOGIN_SERVER"

sha256sum --check SHA256SUMS
```

Set LAB22_LOGIN_SERVER to the existing registry's loginServer first. Deployments use a mutable v1 tag; no full independent rebuild or digest-pinned deployment was tested. Original templates intentionally retain the successful configuration, not the temporary target-port fault.

[Lab results](../README.md)
