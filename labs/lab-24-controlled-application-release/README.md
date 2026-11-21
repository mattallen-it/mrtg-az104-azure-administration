# Lab 24 — Controlled application release

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Validated](https://img.shields.io/badge/Status-Validated-2E7D32)

[Portfolio](../../README.md) · [All labs](../../docs/progress.md) · [Evidence gallery](screenshots/README.md)

## Outcome

Validated an App Service release and rollback on November 21, 2026. Production initially served v1.0 and staging v2.0. A swap promoted v2.0; a second swap restored v1.0 without redeploying code. HTTPS application and static health samples returned 200. Slot-specific environment values were verified before deployment and in staging after each swap settled. Original release artifacts match the captured SHA-256 values. The lab group was deleted; attributable cost remains unconfirmed.

## Business problem

MRTG needs to validate a release outside production, promote it deliberately, and restore the previous version if the release decision changes. The exercise separates application version from environment configuration and records what was actually served after each operation.

## Environment and decisions

| Component | Configuration / observation |
|---|---|
| Group / region | rg-mrtg-lab24-release / East US 2 |
| Plan | asp-mrtg-lab24-s1; Linux S1 Standard; one instance |
| Application | app-mrtg-lab24-f3a07c66; Python 3.12 selected at creation |
| Slots | Production and staging; both Running and HTTPS-only true |
| Build | SCM_DO_BUILD_DURING_DEPLOYMENT=true on both slots |
| Sticky setting | LAB_ENVIRONMENT=Production or Staging; slotSetting=true verified on both before deployment |
| Code | Flask root JSON and static /health; versions 1.0 and 2.0 embedded in source |
| Tags | Environment=Lab, Project=MRTG-AZ104-Administration, Lab=Lab-24 supplied for group/app |

S1 was used for deployment-slot support. The quota check showed S1 usage 0 / limit 30 and regional usage 0 / limit 31. The retail API lookup returned USD 0.095 per hour for East US 2 Linux S1; this is a dated unit-price observation, not a measured session charge. Both slots used the same one-instance plan. No new Entra or Microsoft 365 license was introduced.

## Work performed

1. Checked S1 and regional quota, then queried the Microsoft retail pricing API before creating the paid plan.
2. Created the group, one-instance S1 plan, Python app and staging slot. Explicitly enabled HTTPS-only on staging as well as production.
3. Enabled remote build and set LAB_ENVIRONMENT as a deployment-slot setting on both slots. Read back Production/True and Staging/True.
4. Created separate v1 and v2 source directories and ZIP packages, with app.py and requirements.txt at each deployment ZIP root. Deployed v1 to production and v2 to staging.
5. Sampled both application and health endpoints over HTTPS before release.
6. Swapped staging into production, sampled both hostnames, then rechecked staging configuration and its live response after an initial temporary environment mismatch.
7. Swapped again to roll back, verified production v1.0 and staging v2.0, and rechecked staging after the same temporary mismatch.
8. Created a checksum manifest and source bundle, downloaded it, matched its captured hash and all six member hashes, and confirmed nested deployment ZIPs match their corresponding source files.
9. Deleted the lab group and checked existence. Searched Cost analysis for the group; no matching item was available.

## Validation results

| Phase | Production sample | Staging sample | Additional evidence |
|---|---|---|---|
| Before swap | v1.0 / Production / 200 | v2.0 / Staging / 200 | Both health routes 200 with matching versions |
| Promotion | v2.0 / Production / 200 | v1.0 / Production / 200 initially | Both health routes 200; staging environment needed recheck |
| Promotion follow-up | Earlier production sample retained | v1.0 / Staging / 200 | Saved Staging/True verified |
| Rollback | v1.0 / Production / 200 | v2.0 / Production / 200 initially | Both health routes 200; staging environment needed recheck |
| Rollback follow-up | Earlier production sample retained | v2.0 / Staging / 200 | Saved Staging/True verified |
| Artifact preservation | Original v1 source and ZIP match | Original v2 source and ZIP match | Bundle and six member SHA-256 matches |
| Cleanup | Group existence false | Slots removed with group | Group deletion capture retained |

The version transition was production **1.0 → 2.0 → 1.0**, with the previous production version available in staging after promotion. No code redeployment was performed between promotion and rollback.

## Troubleshooting and lessons

The production deployment returned RuntimeSuccessful, zero failed and one successful instance. Staging reported deployment completed but the selected status fields were null. That summary was not treated as runtime proof: subsequent v2.0 application and health requests established the staging result.

Immediately after each swap, staging briefly returned the Production environment value. Later reads showed its saved setting remained Staging with slotSetting=true and the live response returned Staging. The observations are consistent with the source slot completing its configuration transition; the lab did not instrument the internal restart sequence or establish an exact propagation interval. A completed swap command and one successful request are insufficient to prove all slot configuration has settled.

The screenshot archive reversed the initial-swap and follow-up-verification filenames. Their byte contents were preserved and assigned to the matching names before publication. No screenshot result was edited.

## Cleanup and costs

Source preservation preceded `az group delete --name rg-mrtg-lab24-release --yes`. The subsequent `az group exists` returned false on November 21. The paid plan, application and staging slot were within that group. Provider registration and subscription quota were retained; unrelated resources and budgets were not re-audited.

The November 21 cost-filter search for rg-mrtg-lab24-release returned **No items found**. USD 6.69 actual and USD 10.26 forecast on the background page are broader billing-scope totals, not Lab 24 usage. The USD 0.095/hour unit rate and illustrative USD 0.19/two-hour estimate do not establish actual runtime or billed cost. Attributable usage and final billing remain unconfirmed. See the [cost ledger](../../docs/cost-ledger.md).

## Evidence and limits

The [gallery](screenshots/README.md) contains 15 reviewed screenshots, including author-redacted cost evidence. The [release artifacts](source/README.md) preserve original source, deployment ZIPs, manifest and bundle with verified hashes.

Rollback was a deliberate exercise using two healthy releases, not recovery from an induced broken release. Sampled HTTPS 200 responses do not prove uninterrupted availability, zero dropped requests, load capacity or a recovery-time guarantee. The static /health route does not validate dependencies or configured App Service Health Check. There was no database/schema change, automated release pipeline, approval gate, traffic-percentage experiment, authentication, managed identity, private endpoint, access-denial test or independent infrastructure rebuild. Slot-specific environment values are configuration boundaries, not identity-security isolation; both slots shared compute.
