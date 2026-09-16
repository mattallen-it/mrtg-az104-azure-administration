# MRTG Azure Administrator Lab Series

Version 1.2 • September 15, 2026 • Curriculum and lab task cards

## Mission

Extend Monroe Redstone Technology Group (MRTG) into a simulated Azure operating environment. Learn to build, administer, troubleshoot, recover, and explain infrastructure while preparing for AZ-104. Existing AD DS, DNS, Windows Server 2022, Windows 11, GPO, and identity lifecycle work remains the on-premises foundation.

The scenario: MRTG needs a small cloud environment for internal operations, controlled document access, an application, monitoring, and recovery. You are the administrator implementing change requests and resolving incidents. This is a fictional commercial Azure lab with government-contractor-style documentation; it is not an Azure Government deployment or evidence of regulatory compliance.

This guide contains 32 sequenced lab briefs, completion criteria, a documentation template, and a runnable first-session checklist. It is not 32 portal click-through walkthroughs. Exact implementation steps must be checked against the current service documentation and the actual tenant before each build.

## Continuity with the existing MRTG portfolio

Reviewed the three repository READMEs, the AZ-900 cost-protection lab, the SC-900 RBAC lab, and the SC-900 documentation template on September 15, 2026.

| Existing project | Verified foundation | AZ-104 progression |
|---|---|---|
| [Enterprise IAM — 30 labs](https://github.com/mattallen-it/MRTG-Enterprise-IAM-Lab-Series) | AD lifecycle, delegation, file permissions, PowerShell, recovery, service accounts, and Splunk | Cloud lifecycle, scoped resource access, data authorization, reproducible deployment, and operational telemetry |
| [AZ-900: The Bridge — 13 labs](https://github.com/mattallen-it/mrtg-az900-the-bridge) | Azure discovery, resource organization, budget controls, and documentation | Build and troubleshoot the services previously explored |
| [SC-900 — 12 labs](https://github.com/mattallen-it/mrtg-sc900-security-compliance-identity) | Security and identity concepts, documented discovery, and scenario reasoning | Implement controls and prove expected access and denial |

The repository records 13 AZ-900 labs; use that count instead of older planning notes that describe 30. SC-900 lab 04 explicitly records no RBAC assignments or Conditional Access changes. Its completion therefore does not establish deployed access controls in the current tenant.

Confirmed on-premises architecture: Hyper-V on Windows 11 Pro; domain `mrtg.local`; `MRTG-DC01` and `MRTG-DC02` on Windows Server 2022; `MRTG-LOG01` for Splunk; and `MRTG-CLIENT-01` on Windows 11 Enterprise. These are documented assets, not a live health check. Preserve them while building disposable Azure workloads.

Your latest direction takes precedence over older README roadmaps: AZ-104 is next; AI-901 remains deferred. The earlier MRTG repositories are reference foundations for this series.

## Exam alignment

Microsoft's current study guide lists objectives effective April 17, 2026. Recheck before booking the exam. [1]

| Exam domain | Weight | Primary labs |
|---|---:|---|
| Identity and governance | 20–25% | 01–07 |
| Storage | 15–20% | 13–17 |
| Compute | 20–25% | 18–24 |
| Networking | 15–20% | 08–12 |
| Monitoring and maintenance | 10–15% | 25–29 |
| Integrated practice | All | 30–32 |

The original lab numbering groups related infrastructure work. The course-led study order below now determines when to perform each task, with short prerequisite exercises where needed. It does not imply that networking outweighs compute or that IAM alone is sufficient preparation. Use Microsoft's official lab collection as the implementation companion. [2]

## Course-led study order — Scott Duffy + Microsoft Learn + MRTG

The primary course is [AZ-104 Microsoft Azure Administrator — Complete Exam Prep](https://www.udemy.com/course/70533-azure/) by Scott Duffy. The public curriculum was checked September 15, 2026. It exposes ten opening sections and indicates sixteen further sections without exposing their detailed sequence. The opening mapping below is verified against those visible headings; later mappings are by topic, not invented lecture numbers. Your private progress and the title of the linked lecture were not available from the public page.

Use Udemy to set the topic order, Microsoft Learn to explain and verify behavior, and MRTG to practice and prove it. The official exam study guide remains the coverage checklist. When a lecture differs from current documentation or observed behavior, investigate and document the difference.

Lab numbers remain stable references. Use the study order here instead of completing labs strictly 01–32. This preserves earlier links and avoids rebuilding the whole curriculum around changing lecture numbers.

### Verified opening course sequence

The topic labels below are abbreviated from the visible curriculum. Lab actions and completion criteria are original MRTG adaptations.

| Course stage | MRTG lab work | Learn companion |
|---|---|---|
| 1. Introduction, account, budget | 01: validate existing account/subscription and cost controls | Prerequisites; identity/governance |
| 2. Azure concepts | Explain MRTG tenant, subscription, resources, and local AD boundary; preview 02 | Prerequisites |
| 3. PowerShell and CLI | 01 command exercise below; start the inventory portion of 07 | Prerequisites |
| 4. Entra introduction | 03 preparation: inspect current tenant, identity types, licensing | Identity/governance |
| 5. Users and groups | 03 lifecycle work, then 06 SSPR; licensing-dependent tasks remain gated | Identity/governance |
| 6. RBAC | 04 scoped access; 13 minimal account setup + 14 identity-access portion for the storage demos | Identity/governance; storage security |
| 7. Subscription governance | Complete 02, 05, and 07; reserve VM-specific move work for 20 | Identity/governance |
| 8. Storage access | 13–14; begin 15 protection tasks; defer private-network validation until 08–12 | Storage |
| 9. Storage data management | Finish 13 transfers and 15 lifecycle work; complete 17 replication | Storage |
| 10. Azure Files | 16 file shares, snapshots, and identity prerequisites | Storage |

A course demo can satisfy an MRTG build step when you use MRTG naming, verify the result, and capture evidence. Do not repeat identical deployments merely because Udemy and Learn both demonstrate them. Keep the distinctive MRTG access tests, troubleshooting, and cleanup.

### Later topic mapping — exact course order pending

Follow these topics when they appear in your course player. These rows are not asserted to be Udemy sections 11–26.

| Topic encountered | MRTG labs | Learn companion |
|---|---|---|
| Deployment templates and automation | 18 | Prerequisites; compute |
| VM creation, disks, moves, availability, scaling | 19–21; run 08 first if networking basics are needed | Compute |
| Container workloads | 22 | Compute |
| Web hosting, slots, TLS, scaling, backup | 23–24 | Compute |
| Networking and secure connectivity | 08–12; return to deferred storage network tests | Networking |
| Operational telemetry and alerts | 25–27 | Monitoring/backup; networking |
| Backup and regional recovery | 28–29 | Monitoring/backup |
| Integrated review and readiness | 30–32 | Official objectives and practice assessment |

To finalize exact later section/lecture alignment, use an expanded screenshot or copied section list from the enrolled course. Until then, match by topic name; all 32 lab briefs remain available.

### Microsoft Learn companions

- [Prerequisites for Azure administrators](https://learn.microsoft.com/en-us/training/paths/az-104-administrator-prerequisites/): command tools, resource management, and foundations. Use targeted review for familiar AZ-900 material.
- [Identity and governance](https://learn.microsoft.com/en-us/training/paths/az-104-manage-identities-governance/): directory administration, scoped permissions, and governance.
- [Storage](https://learn.microsoft.com/en-us/training/paths/az-104-manage-storage/): account configuration, Blob data, storage security, and file shares.
- [Compute](https://learn.microsoft.com/en-us/training/paths/az-104-manage-compute-resources/): workload administration and deployment.
- [Networking](https://learn.microsoft.com/en-us/training/paths/az-104-manage-virtual-networks/): addressing, connectivity, traffic controls, and diagnostics.
- [Monitoring and backup](https://learn.microsoft.com/en-us/training/paths/az-104-monitor-backup-resources/): operational visibility and recovery.

Read the matching module around the course topic. Use the official objectives to catch subjects that a course or learning-path module treats differently. Do not automatically expand the lab into every adjacent service mentioned by a learning path.

### Lab 01 command exercise — perform at the course's scripting stage

Use the authenticated shell/tool environment taught in the course. First inspect the current context; set the intended MRTG subscription explicitly before any later mutation. The following are read-only examples, not commands already executed against your Azure environment.

PowerShell:

```powershell
Get-AzContext
Get-AzSubscription
Get-AzResourceGroup | Select-Object ResourceGroupName, Location
```

Azure CLI:

```bash
az account show --query '{name:name,id:id,tenant:tenantId}' -o table
az account list --query '[].{name:name,id:id,isDefault:isDefault}' -o table
az group list --query '[].{name:name,location:location}' -o table
```

Pass: explain which tenant/subscription the session uses, identify the same resource groups visible in the portal, and explain an empty result if applicable. Sanitize account identifiers before publishing. Record shell prerequisites and any storage created by the chosen environment. Authentication/setup commands should follow the current course and official tool instructions for your environment.

### Session format

1. Watch a small course topic and write its key decision in one sentence.
2. Read the matching Learn material and resolve one unclear point.
3. Perform the mapped MRTG task, splitting a larger lab as needed.
4. Predict and test an allowed action and a failure where applicable.
5. Capture brief evidence, explain your result, and complete cleanup.
6. Answer knowledge checks independently; use explanations afterward to repair gaps.

A reasonable 75–90 minute session allocates about 15–20 minutes to video, 10–15 to Learn, 35–40 to practice, and 10–15 to evidence and cleanup. This is flexible; reserve cleanup time even when the build takes longer. Documentation polishing can happen after the paid resources are removed.

### Track the three learning activities separately

| Topic | Udemy section/lecture | Learn module | MRTG lab/task | Video completed | Learn completed | Build tested | Fault resolved | Cleanup verified | Next action |
|---|---|---|---|---|---|---|---|---|---|
| Environment and cost baseline | Opening account/budget lessons | Prerequisites + governance | 01 | Pending | Pending | Pending | N/A until applicable | Pending | Inspect the existing subscription |

Add rows as you progress. A watched demonstration is not a completed build. Preserve design-only labels for licensing/cost-gated work and track what remains untested. Keep all initial progress pending until you report the actual result.

### Course-specific boundaries

- Reuse MRTG's existing tenant and subscription after validation. Watching account/tenant creation does not require creating another one.
- Premium-license purchase or trial demonstrations are information, not a requirement to buy or activate anything. Inspect eligibility and cost first.
- Do a minimal disposable storage setup when the early RBAC demos need it; return for the full storage labs later.
- For early storage networking lessons, complete the concept comparison now and the full private-path test after the network prerequisites. A basic authenticated storage exercise does not require anonymous access.
- Use a small temporary network for early VM practice if needed, then revisit its design in the networking labs. Defer advanced configuration rather than pretending prerequisites are complete.
- When revisiting a cleaned-up workload, rebuild from saved configuration. Logical continuity across labs does not require keeping everything running.

## Operating standards

- Reuse the dedicated MRTG account and existing subscription after checking their current state. The recorded subscription name is `MRTG-AZ900-Lab-Subscription`; no rename or new account is required.
- Default region: `Central US`. Validate service availability, quotas, and price before each deployment; document any alternate region.
- Resource naming: `<resource-type>-mrtg-az104-labNN-<region>-<instance>`. Example: `rg-mrtg-az104-lab01-centralus-001`. Shorten names where a service's length/character rules require it; storage accounts need a globally unique compliant variant.
- Required tags: `Project`, `Lab`, `Environment`, `Owner`, `CostCenter`, `ManagedBy`, `DeleteAfter`. Use synthetic values and UTC cleanup dates. Tags are metadata; `DeleteAfter` does not delete anything.
- Use proposed cloud groups such as `MRTG-AZ104-Readers` and `MRTG-AZ104-Operators`. These proposed additions follow the existing organization/function/purpose identity pattern. Reuse established groups only after inspecting their membership and scope.
- Start with cloud-only test identities in the existing tenant domain. Do not assume that AD identities already synchronize to Entra or introduce synchronization as an unplanned prerequisite.
- Keep resource groups disposable. Preserve reusable configuration and evidence in GitHub, MRTG's documentation system of record.
- Retain admin recovery access. Test permissions using separate test accounts, never by removing the only administrator's access.
- Work only with synthetic files, accounts, and business records. Sanitize screenshots and exclude secrets, SAS strings, credentials, and customer information.

## Cost plan

Treat $100 additional cash spending as the maximum tolerance for the series, not a target or guaranteed Azure spending cap. Do not assume promotional credits remain available.

Keep the existing $10 monthly alert guardrail initially. Before a paid lab, estimate the entire session and residual resources, record remaining total cash allowance, and adjust the monthly plan deliberately if needed. Track cumulative costs across months separately: a resetting monthly budget does not track the series total.

Budgets notify; they do not stop resources. Cost reporting and budget evaluation have delays. [3] At $70 cumulative cash spending, reassess remaining work; at $85, stop new paid deployments and reserve the balance for delayed charges and cleanup. These are proposed operating thresholds, not automated enforcement.

| Mode | Meaning |
|---|---|
| A | Administration or local exercise; usually no new metered workload, but inspect dependencies. |
| B | Short metered session; estimate and remove resources after validation. |
| C | Licensing, paid SKU, extra environment, or recovery prerequisite; inspect first. Use a documented design exercise when unavailable and record the practical gap. |

Prefer small datasets and the smallest suitable available resources. Do not retain a running cloud estate between sessions. Stopping an operating system is not the same as deallocating its Azure VM; disks and other retained services can still cost money after VM deallocation. [4]

For every paid lab: record resource inventory, planned runtime, cost estimate, cleanup method, and actual cost when reported. Check beyond the VM: disks, snapshots, IPs, App Service plans, registries, private endpoints, monitoring, and backup data. Never weaken unrelated retention or security settings to make cleanup easier.

## Learning rhythm

Plan two 60–90 minute sessions plus a short review each week. Split longer labs across sessions, cleaning up metered resources between them. About 16–20 weeks is a planning range, not a deadline; recovery and capstone work may need longer.

Each lab follows **Learn → Build → Document → Explain → Map**:

1. Explain the concept and predict the result before deployment.
2. Implement a small MRTG business request.
3. Prove an expected success and an expected denial or failure.
4. Introduce one controlled fault, diagnose it, and restore service.
5. Save evidence, explain the security/business consequence, and clean up.

Use the portal first when learning a service. Repeat selected operations with PowerShell or CLI; use both across the series. Begin reusable Bicep/ARM work in lab 18. Do not try to implement every lab in every interface.

## Lab task cards

### Phase 1 — Establish MRTG governance

**01 — Subscription inventory and cost baseline [A]**  
Request: establish a controlled place for MRTG cloud work. Inspect tenant, subscription, access, billing, credits, and existing resources. Create the series inventory and budget alerts; create and delete an empty tagged test resource group. Pass: explain tenant versus subscription, identify the billing scope, and prove that only the test group was removed. Detailed checklist below.

**02 — Resource organization and management hierarchy [A]**  
Request: separate experiments from shared controls. Create two empty lab groups; model a management-group hierarchy and create a disposable management group only if permissions allow. Compare inheritance and organize tags. Fault: omit a required tag and detect the inconsistency. Pass: produce a scope diagram and inventory. Remove empty experimental groups; do not move the existing subscription casually.

**03 — Employee and contractor lifecycle [A/C]**  
Request: onboard two fictional employees and a contractor. Create users, assigned groups, and properties; use an owned secondary identity for a guest exercise if available. Inspect license availability and practice assignment/removal only with an eligible unused license. Fault: incorrect group membership. Pass: document corrected access and a tested offboarding sequence. Remove lab identities and memberships; never invite an unrelated person.

**04 — Scoped administration [A]**  
Request: let an operator manage one lab group and let an auditor inspect it. Apply built-in roles, then inspect direct and inherited assignments. Fault: an assignment at the wrong scope. Pass: test what each identity can do in both groups, including a denied write. Explain Entra directory roles versus Azure resource roles. Remove test assignments.

**05 — Guardrails with policy and locks [A/B]**  
Request: enforce an MRTG lab region/tag rule. Begin with an audit policy, then test a narrowly scoped deny policy. Apply a delete lock to a disposable group. Fault: a noncompliant deployment. Pass: distinguish policy denial, RBAC denial, and lock protection using evidence. Remove the test lock and policy before cleanup; avoid subscription-wide experimental denial.

**06 — Password recovery and licensing [C]**  
Request: reduce password-reset tickets. Inspect SSPR entitlements, configure an eligible pilot group, register a test user's methods, and test recovery. Fault: a user outside the pilot. Pass: explain eligibility, reset versus change, and the boundary between cloud recovery and AD writeback. If unlicensed, produce a configuration/test plan and mark it design-only. Do not buy licenses merely to complete the exercise. [5]

**07 — Access review and cost review [A]**  
Request: review MRTG's first operating period. Export role assignments, group membership, resource tags, and costs using CLI or PowerShell. Fault: seed an excessive lab assignment. Pass: identify and remove it, explain inherited access, and document an Advisor finding if one exists. If Advisor has no finding, record that rather than inventing one. Preserve a sanitized review report.

### Phase 2 — Connect and isolate workloads

**08 — Address plan and subnets [B]**  
Request: separate MRTG application and administration traffic. Check existing local address ranges, then choose nonoverlapping Azure ranges and deploy subnets. Fault: attempt an overlapping subnet definition. Pass: explain why it fails and document a corrected address plan. Keep configurations for later rebuilds, not idle paid test machines.

**09 — Traffic permissions [B]**  
Request: permit the intended application flow while restricting administration. Use NSGs and application security groups with small test workloads; inspect effective rules. Fault: a higher-priority deny. Pass: prove one allowed and one blocked connection and identify the responsible rule. Remove workloads and ancillary resources. Do not expose administrative ports broadly.

**10 — Peering and route investigation [B]**  
Request: connect two MRTG segments. Create nonoverlapping networks, peer them, inspect effective routes, and test traffic. Introduce a blackhole route limited to a disposable test destination. Pass: diagnose and reverse it; explain why peering is not automatically transitive. Remove peerings and test resources.

**11 — Name resolution and application availability [B/C]**  
Request: provide a stable name and distribute application requests. Test private DNS and configure a small load-balanced service. Fault: unhealthy probe or wrong DNS record. Pass: identify which layer fails and restore service. Model public DNS delegation if no domain is owned. Remove backend VMs, load balancer, IPs, and zones created for this session.

**12 — Private access and administrator entry [B/C]**  
Request: restrict a small storage workload to an approved path. Compare a service-endpoint setup with a private-endpoint setup and its DNS results. Inspect Bastion availability, SKU cost, and prerequisites; implement a short session if feasible, otherwise document the workflow gap. Pass: prove an intended connection succeeds and an unapproved path fails. Remove endpoints and any Bastion deployment after use.

### Phase 3 — Protect MRTG data

**13 — Storage baseline and transfer [B]**  
Request: store a tiny synthetic MRTG document collection. Choose redundancy and encryption settings; transfer and verify files using Storage Explorer and AzCopy. Fault: wrong destination or missing data permission. Pass: compare file counts/checksums and justify redundancy. Delete the disposable dataset/account after evidence capture.

**14 — Data access boundaries [B]**  
Request: let an auditor read documents without administering storage. Compare management-plane permission with data-plane access. Test a narrowly scoped, short-lived SAS and a separate stored-access-policy exercise using a compatible SAS type. Fault: expired or revoked access. Pass: explain identity, key, and token tradeoffs; test key rotation only on this disposable account. Never save token values in evidence.

**15 — Recover an accidental document deletion [B]**  
Request: restore a fictional operations document. Configure protection, create versions, delete test data, and recover it. Add a lifecycle rule and explain when it should act. Fault: overwrite the test document. Pass: restore the correct content; distinguish rule configuration from observing a scheduled lifecycle action. Clear billable data according to the chosen retention settings.

**16 — Department file access and the AD bridge [B/C]**  
Request: give an MRTG test group shared file access. Create a tiny file share and test snapshot recovery. For identity-based SMB, first document the chosen supported identity source, client state, DNS, connectivity, and permissions. Implement only after those prerequisites are met. Pass: explain and test share-level versus file-level authorization; if blocked, preserve a design-only gap. A storage-key mount is not proof of identity-based access. Reuse existing AD knowledge without assuming hybrid identity is already configured. [6]

**17 — Replication and storage incident drill [B]**  
Request: protect a small document flow between two accounts. Configure a compatible object-replication setup, including its prerequisites, and verify a new test object reaches the destination. Fault: break a narrowly scoped network/access setting and restore it. Pass: distinguish replication, redundancy, and recovery. Remove both accounts and their data after the exercise.

### Phase 4 — Deploy and operate applications

**18 — Reproducible MRTG deployment [A/B]**  
Request: rebuild a small tagged environment consistently. Read and modify ARM JSON and Bicep, parameterize names/region, inspect a what-if result, and deploy. Export a small deployment or decompile an ARM template; inspect the output rather than assuming it is production-ready. Fault: invalid parameter or omitted dependency. Pass: repair it and redeploy from saved configuration. Delete the deployment's resources, not just deployment history.

**19 — VM lifecycle [B]**  
Request: run a small administration workload. Deploy a suitable VM, connect securely, inspect disks, and practice resize and deallocation. As an MRTG IAM extension, enable a managed identity and test scoped access to a disposable Blob container; compare this credential-free workload identity with your on-premises service-account lab. Review encryption-at-host compatibility before selecting an eligible configuration. Fault: connection fails because of a scoped NSG rule. Pass: diagnose it and demonstrate the final power state. Remove disks and IPs when deleting the VM.

**20 — Disk recovery and relocation [B/C]**  
Request: add a test data volume, recover its content, and reorganize ownership. Attach/initialize a disk, place a test file, and recover via a supported snapshot workflow. Perform a supported resource-group move after dependency validation. Compare subscription and regional relocation requirements as a design exercise if a second subscription/region is unavailable. Pass: verify the file after recovery and explain why not all moves use the same operation.

**21 — Availability and scale [B/C]**  
Request: sustain a small web workload through instance loss. Compare availability-set and zonal designs; deploy a minimal suitable scale set and test scaling within a strict maximum. Fault: stop one test instance. Pass: explain observed application behavior and distinguish resilience from backup. Delete all instances, network dependencies, and balancing resources after testing.

**22 — Container delivery [B/C]**  
Request: run a tiny MRTG status application. Use a disposable registry and test deployments through Container Instances and Container Apps, choosing compatible images and networking. Fault: wrong image reference or container port. Pass: use logs to fix startup and explain sizing/scaling differences. Remove registry, container resources, and any created logging dependencies.

**23 — Managed web application [B/C]**  
Request: host an MRTG internal-tools demonstration. Deploy a tiny App Service app, inspect plan capacity, HTTPS/TLS, and networking. Fault: incorrect configuration prevents the expected response. Pass: restore the endpoint and explain the hosting plan's role. Model custom-domain mapping if no domain is owned. Delete the paid plan along with the app when finished.

**24 — Controlled application release [C]**  
Request: release and roll back a small application change. Check plan support/cost for slots, scaling, backup, and required networking. Perform supported operations in a brief paid session or write the exact release/recovery test plan as a documented gap. Fault: deliberately deploy a visibly incorrect version. Pass: validate rollback, not merely deployment success. Remove paid plans and backup storage created for the exercise.

### Phase 5 — Observe and recover

**25 — Logs and operational questions [B]**  
Request: show what changed and whether the service is healthy. Configure a minimal workspace and selected diagnostics; collect only useful test telemetry. Write KQL queries that answer specific incident questions. Fault: missing log category or wrong time range. Pass: locate the cause and distinguish an empty result from proof that nothing happened. Review ingestion/retention and remove unnecessary sources.

**26 — Actionable alerts [B]**  
Request: detect one MRTG service symptom. Create an alert, an action group directed to your own address, and an alert-processing rule. Trigger and resolve a controlled condition. Pass: prove notification delivery and explain suppression versus resolution. Inspect available VM/storage/network Insights; record any instrumentation prerequisites. Remove test alerts, receivers, and paid telemetry resources when finished.

**27 — Network incident response [B]**  
Request: investigate an unreachable application. Use Network Watcher and a suitable Connection Monitor setup with disposable endpoints. Introduce one routing or security-rule error at a time. Pass: show source, destination, protocol, relevant rule/route, and post-fix evidence. Remove monitoring tests, agents/workloads, and dependencies.

**28 — Backup with a proven restore [B/C]**  
Request: recover a synthetic MRTG workload. Compare Recovery Services vault and Backup vault support; select a suitable small workload, policy, and retention design. Inspect soft-delete/immutability implications before enabling protection. Run backup, change/delete test content, then restore and verify it. Pass: recover the actual data and inspect job status/reporting/alerts. Document protected-item removal, retained data, and any continuing cost; do not assume deleting a resource group clears retained backups.

**29 — Regional recovery exercise [C]**  
Request: rehearse a regional outage. Define MRTG recovery time and data-loss targets as fictional business requirements, then map a Site Recovery workflow. A live path requires feasible supported source/target resources and a priced replication/test-failover session. Use an isolated test network, verify recovery, clean up the test failover, and review replication cleanup. Budget path: a tabletop runbook and troubleshooting exercise. Pass: label live versus simulated results accurately; never claim failover was performed from a design alone.

### Phase 6 — Demonstrate independent administration

**30 — Joiner, mover, leaver across services [A/B]**  
Request: onboard a fictional operator, change their job duties, and offboard them. Combine Entra groups, scoped RBAC, and one data-access path. Test with fresh sign-ins/tokens after changes and account for propagation. Fault: a lingering direct assignment bypasses the intended group removal. Pass: discover it and prove final denial. Explain which actions would also be required in MRTG's separate AD environment.

**31 — MRTG Azure operations capstone [B]**  
Request: build a small document-processing/support environment from your own requirements. Include named/tagged resources, least-privilege identities, a network boundary, protected data, one compute option, telemetry, a tested recovery method, and reproducible deployment. Reuse earlier templates. Inject three faults: access denied, application unreachable, and missing data. Pass: resolve them with evidence, give a five-minute architecture explanation, and complete a cost/cleanup review. A tested file restore is acceptable; an expensive live regional recovery estate is unnecessary.

**32 — Rebuild, review, and exam readiness [A/B]**  
Request: hand MRTG operations to another administrator. Rebuild one workload without a click-by-click guide, fix two unfamiliar variations, and finish the operations handover. Take Microsoft's practice assessment and classify misses by domain. Pass: explain both the correct answer and why alternatives fail, then repeat weak labs. Record exam completion separately from lab completion. Assessment scores are practice signals, not a guarantee of passing.

## Lab 01 — First-session checklist

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

## Reusable lab record

Copy this structure for each lab into the MRTG repository:

```markdown
# Lab NN — Title
Status: Not started / In progress / Validated / Design-only / Needs repeat
Date:
AZ-104 domain:
Udemy section and lecture title:
Microsoft Learn module/unit:
Course demo reused or extended:
MRTG request or incident:
Business outcome:
Prerequisites and dependencies:
Permissions and licenses required:
Resources, region, and runtime:
Cost estimate / cumulative cash spend / remaining allowance:

## Learn
Concept in my own words; expected result; official references.
## Build
Actions taken; commands/templates; relevant configuration decisions.
## Validate
Test | Expected | Actual | Evidence
Include an allowed action and a denied/failed action where applicable.
## Troubleshoot
Symptom; hypotheses; evidence; root cause; correction; retest.
## Explain and map
Why this control matters; IAM/security relevance; exam connection.
## Cleanup
Objects removed; retained resources/data and why; continuing costs;
verification timestamp; follow-up cost review.
## Knowledge check
Three questions answered without looking at instructions.
## Gaps and next action
Unperformed features; reason; what must be repeated hands-on.
```

Repository: [mrtg-az104-azure-administration](https://github.com/mattallen-it/mrtg-az104-azure-administration). Preserve the established cloud-series structure: root `README.md`, `docs/lab-template.md`, and `labs/lab-NN-descriptive-title/README.md` with a `screenshots/` directory per lab. Add `templates/` for ARM/Bicep, `scripts/` for automation, and `runbooks/` for recovery/handover when needed.

The short lab record above is the working worksheet. For polished portfolio documentation, adapt the existing SC-900 template: change the exam mapping to AZ-104, preserve business scenario, prerequisites, required permissions, starting state, change control, steps, evidence, validation, troubleshooting, exam distinctions, IAM relevance, production considerations, cost/licensing, cleanup, and screenshot review. Omit inapplicable sections. Start every new checklist unchecked and every validation result as pending; never carry the old template's prechecked completion items into unfinished work.

Preserve the AI-use disclosure accurately: AI supports planning, explanation, and documentation; the author performs and validates Azure work. Do not copy past-tense success statements into a planned lab. A diagram must distinguish deployed connections from proposed hybrid links.

## Completion and readiness rules

Screenshots alone do not finish a lab. Completion requires a working result, proof, an explanation, and cleanup. A design-only exercise is valid learning but remains a hands-on gap. Keep a simple tracker with one row per lab and the statuses above.

Before booking: revisit the official objective list, close significant practical gaps, complete the capstone without a walkthrough, and review unfamiliar scenarios across all five domains. Do not substitute additional certifications or optional hybrid projects for the Azure administration work here.

After this core series, optional MRTG extensions include scoped AD-to-Entra synchronization, Conditional Access, PIM, and homelab connectivity. These are future enhancements, not prerequisites silently added to AZ-104.

## Official references

Checked September 15, 2026. These are implementation references; validate current SKU, licensing, region, and cleanup behavior before execution.

1. [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
2. [Microsoft Learning AZ-104 lab collection](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/)
3. [Create and manage Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
4. [VM states and billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing)
5. [SSPR licensing](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing)
6. [Azure Files identity-based authentication](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)
