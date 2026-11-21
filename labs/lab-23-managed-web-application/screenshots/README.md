# Lab 23 evidence gallery

**15 published screenshots.**

November 20–21, 2026 local execution. Setup, observed requests and cleanup are distinguished below.

## web provider registered

Microsoft.Web registration completed.

![Microsoft.Web registration completed.](lab23-web-provider-registered.png)

## plan regions and runtimes

F1 Linux region and Python runtime discovery; support does not establish subscription quota.

![F1 Linux region and Python runtime discovery; support does not establish subscription quota.](lab23-plan-regions-and-runtimes.png)

## free plan quota blocked

Central US group created; F1 deployment rejected with a zero limit.

![Central US group created; F1 deployment rejected with a zero limit.](lab23-free-plan-quota-blocked.png)

## eastus2 free plan quota blocked

East US 2 F1 deployment also rejected before support resolution.

![East US 2 F1 deployment also rejected before support resolution.](lab23-eastus2-free-plan-quota-blocked.png)

## linux free plan created

Post-resolution plan creation: East US 2, F1 Free, Linux true.

![Post-resolution plan creation: East US 2, F1 Free, Linux true.](lab23-linux-free-plan-created.png)

## python webapp created https only

Python web app Running with HTTPS-only true.

![Python web app Running with HTTPS-only true.](lab23-python-webapp-created-https-only.png)

## python zip deployment succeeded

Source creation and remote ZIP deployment; build/runtime success; subscription ID redacted by author.

![Source creation and remote ZIP deployment; build/runtime success; subscription ID redacted by author.](lab23-python-zip-deployment-succeeded.png)

## development https health 200

Initial Development application and static health route both return 200.

![Initial Development application and static health route both return 200.](lab23-development-https-health-200.png)

## app setting validation https 200

Saved setting and live response both Validation; HTTPS 200.

![Saved setting and live response both Validation; HTTPS 200.](lab23-app-setting-validation-https-200.png)

## http redirects to https 301

HTTP 301 with HTTPS Location header.

![HTTP 301 with HTTPS Location header.](lab23-http-redirects-to-https-301.png)

## access restriction denied 403

Saved IPv4 deny rule and observed 403.

![Saved IPv4 deny rule and observed 403.](lab23-access-restriction-denied-403.png)

## access restriction removed recovery 200

Explicit Deny removal; Allow all restored and application 200.

![Explicit Deny removal; Allow all restored and application 200.](lab23-access-restriction-removed-recovery-200.png)

## final runtime and source hashes

Python 3.12, TLS minimum 1.2, Always On false, source/ZIP hashes.

![Python 3.12, TLS minimum 1.2, Always On false, source/ZIP hashes.](lab23-final-runtime-and-source-hashes.png)

## resource group deleted

Deletion followed by az group exists=false.

![Deletion followed by az group exists=false.](lab23-resource-group-deleted.png)

## cost filter no match

November 21 cost-filter search returns No items found; billing name redacted; broader totals are not Lab 23 cost.

![November 21 cost-filter search returns No items found; billing name redacted; broader totals are not Lab 23 cost.](lab23-cost-filter-no-match.png)

[Lab results](../README.md)
