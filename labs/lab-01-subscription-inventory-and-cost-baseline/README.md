# Lab 01 — Subscription inventory and cost baseline

**Status: Planned — not performed or validated.**

## MRTG assignment

Request: establish a controlled place for MRTG cloud work. Inspect tenant, subscription, access, billing, credits, and existing resources. Create the series inventory and budget alerts; create and delete an empty tagged test resource group. Pass: explain tenant versus subscription, identify the billing scope, and prove that only the test group was removed. Detailed checklist below.

## Study alignment

- Udemy section/lecture: Pending
- Microsoft Learn module: Pending
- Follow the course mapping in [the series guide](../../docs/series-guide.md).

## Starting state and permissions

Record before executing. Confirm tenant, subscription, required roles, dependencies, and licensing.

## Cost and cleanup plan

Mode: A. Record estimated runtime/cost and exact resources to remove before deploying.

## Steps performed

Not started. Use the [lab template](../../docs/lab-template.md) to document actual work.

## Validation

| Test | Expected | Actual | Evidence |
|---|---|---|---|
| Intended behavior | Define before build | Pending | Pending |
| Failure or denied action | Define before build | Pending | Pending |
| Cleanup | Lab resources removed or retained with justification | Pending | Pending |

## Troubleshooting and lessons

Pending.

## Execution checklist


Timebox: 60–90 minutes. New infrastructure: one empty resource group only. No VM required.

1. Open the Azure portal using the dedicated MRTG account. Check the directory and subscription selector. Record the actual tenant/subscription locally; sanitize identifiers in public evidence.
2. Open Subscriptions and inspect `MRTG-AZ900-Lab-Subscription`, or the actual MRTG subscription if its name changed. Confirm status and your assigned access. Stop configuration changes if this is an employer/client subscription.
3. Inspect All resources and resource groups filtered to that subscription. Record existing resources and their purpose. Do not delete leftovers until ownership is understood.
4. Open Cost Management at the subscription scope. Record month-to-date cost, currency, billing arrangement, and any verified remaining credit/expiration. Do not treat a remembered credit offer as active credit.
5. Inspect the existing $10 monthly budget; create it if absent and supported. Add actual-cost notifications at 50%, 80%, and 100%, plus a forecast notification if available, to your own address. Record if permissions or a newly created subscription prevent budget creation; resolve this before paid deployment.
6. Create `rg-mrtg-az104-lab01-centralus-001` in Central US. Apply `Project=MRTG-AZ104-Administration`, `Lab=Lab-01`, `Environment=Lab`, `Owner=MRTG-Cloud-Operations`, `CostCenter=Training`, `ManagedBy=Azure-Portal`, and `DeleteAfter=<today's UTC date>`.
7. Inspect the resource group's tags and confirm it contains no resources. Record its purpose in the inventory.
8. Explain aloud: Where do identities live? What scope holds resources and consumption? What does a budget do? What does it not do?
9. Delete only this named empty test group, then verify it is absent. Keep the budget and inventory.
10. Save sanitized before/after evidence and a short README. Record any cost-reporting delay and revisit reported charges at the next session.

Completion evidence: correct subscription identified; baseline inventory; budget configuration or documented blocker; tagged test group; verified deletion; explanations in your own words.

