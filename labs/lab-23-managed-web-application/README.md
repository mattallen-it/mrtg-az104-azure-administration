# Lab 23 — Managed web application

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

[Portfolio](../../README.md) · [All labs](../../docs/progress.md) · [Evidence gallery](screenshots/README.md)

## Outcome

Deployed a Python 3.12 Flask application to a Linux Free F1 App Service plan in East US 2 after resolving a subscription quota blocker. Verified application and health responses over HTTPS, a runtime setting change without code redeployment, HTTP-to-HTTPS redirection, an IPv4 access denial and recovery. Preserved the original source ZIP with matching hashes and verified resource-group deletion. Execution spanned November 20–21, 2026, local time; attributable cost remains unconfirmed.

## Business problem

MRTG needs a small managed web workload whose configuration and network exposure can be changed and tested independently of its code. The administrator must distinguish resource provisioning from application availability and prove both denied access and recovery.

## Environment and decisions

| Component | Observed configuration |
|---|---|
| Resource group | rg-mrtg-lab23-web; group metadata location Central US |
| App Service plan | asp-mrtg-lab23-free; deployed in East US 2; F1 / Free; Linux enabled |
| Web app | app-mrtg-lab23-9617a22e; default azurewebsites.net hostname; HTTPS-only true |
| Runtime | Python 3.12; minimum TLS 1.2 configured; Always On false |
| Source | Flask app.py and requirements.txt; remote build enabled; original [source and ZIP](source/README.md) retained |
| Application setting | LAB_ENVIRONMENT initially Development, changed to Validation |
| Tags | Environment=Lab, Project=MRTG-AZ104-Administration, Lab=Lab-23 supplied on group/app creation |

The resource group's metadata location did not select the plan's deployment region. F1 was retained throughout the exercise; no paid-tier workaround was used. No application authentication or managed identity was configured for this workload.

## Work performed

1. Registered Microsoft.Web and listed supported F1 Linux regions and Python runtimes.
2. Created the tagged group. Plan creation failed with a zero F1 quota in Central US and again in East US 2.
3. Investigated the discrepancy: East US 2 individual SKU quota appeared as 30 while Total Regional VMs showed zero. A small F1 increase request failed; a support request was created. Microsoft later reported fulfillment. These intermediate portal/support observations were reviewed during execution but are not all in the public gallery. The successful plan creation is the deployment proof.
4. Created the East US 2 F1 Linux plan and Python web app with HTTPS-only enabled.
5. Created the Flask application, enabled SCM_DO_BUILD_DURING_DEPLOYMENT, set LAB_ENVIRONMENT=Development and deployed the source ZIP. Build and runtime success were captured.
6. Tested `/` and `/health`, then changed LAB_ENVIRONMENT to Validation without redeploying source. Re-read the saved setting and tested the live response.
7. Requested HTTP without following redirects. Added Lab23-Temporary-Deny for 0.0.0.0/0, priority 100, and tested HTTPS using IPv4. Removed the rule with explicit `--action Deny` and tested recovery.
8. Captured final runtime configuration and SHA-256 values, downloaded the original ZIP, verified all hashes and deleted the lab group.

## Validation results

| Test | Observed result | Meaning |
|---|---|---|
| Plan and app provisioning | Plan Succeeded, F1 Free Linux; app Running, HTTPS-only true | Resources provisioned after quota resolution |
| Initial application | HTTPS 200, environment Development, version 1.0 | Deployed code served the configured value |
| Health route | HTTPS 200, status healthy | Static application endpoint responded |
| Configuration change | Saved value Validation and live response Validation / 200 | Configuration affected runtime without source redeployment |
| HTTP request | 301, Location points to HTTPS hostname | HTTP redirect observed |
| Access denial | Named Deny rule saved; IPv4 HTTPS 403 | Network restriction blocked the sampled request |
| Recovery | Temporary rule absent, Allow all displayed; Validation / 200 | Public application access restored |
| Artifact preservation | app.py, requirements.txt and ZIP SHA-256 match Cloud Shell capture | Uploaded artifacts match captured bytes |
| Cleanup | az group exists returned false | Lab resource group no longer existed |

## Troubleshooting and lessons

Region support is not proof of usable subscription quota. The initial recommendation to deploy in East US 2 overlooked its zero regional-total row; that attempt also failed. The quota investigation and support escalation preceded successful deployment. The support email used generic VM/vCPU terminology; it does not mean 31 running instances were created.

The immediate response after changing LAB_ENVIRONMENT still showed Development. A later read of the saved setting and application response verified Validation. Similarly, the first request after adding the deny rule returned 200; a later query showed the saved rule and a request returned 403. These observations establish eventual behavior, not a measured propagation-time guarantee.

The first removal command omitted `--action Deny`; the CLI reported no matching rule, the rule remained present and HTTPS stayed 403. Adding that argument removed it and restored 200. Verify both configuration and actual traffic after changes.

## Cleanup and costs

After source preservation, `az group delete --name rg-mrtg-lab23-web --yes` completed and `az group exists` returned false on November 21. Microsoft.Web registration and the approved regional quota were retained; unrelated resources, support-case closure and subscription budgets were not re-audited.

The November 21 Cost analysis search for rg-mrtg-lab23-web returned **No items found**. The displayed USD 6.69 actual total and USD 10.26 forecast belong to the broader billing scope, not Lab 23. No attributable cost or final invoice was established; missing filter data is not proof of zero charge. See the [cost ledger](../../docs/cost-ledger.md).

## Evidence and limits

The [gallery](screenshots/README.md) contains 15 reviewed screenshots, including author-redacted deployment and billing captures. The support-request notification is withheld because it contains a case number. Intermediate quota views, fulfillment email, stale responses and failed removal are described as troubleshooting history rather than added to this gallery.

The [original source files and ZIP](source/README.md) are preserved byte for byte with checksums. Dependency ranges are not a dependency lockfile, and the archive does not provision infrastructure. `/health` is a static route, not proof of configured App Service Health Check or downstream dependency monitoring. TLS 1.2 is a configuration observation; protocol negotiation below that version was not tested. The network 403 is not an identity-authorization denial. No authentication, managed-identity resource access, private networking, custom domain, deployment slot, scaling, load test or independent infrastructure rebuild was validated.
