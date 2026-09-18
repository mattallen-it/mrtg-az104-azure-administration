# MRTG Azure Administrator Lab Series

## Mission

Extend Monroe Redstone Technology Group (MRTG) into a simulated Azure operating environment. Learn to build, administer, troubleshoot, recover, and explain infrastructure while preparing for AZ-104. Existing AD DS, DNS, Windows Server 2022, Windows 11, GPO, and identity lifecycle work remains the on-premises foundation.

The scenario: MRTG needs a small cloud environment for internal operations, controlled document access, an application, monitoring, and recovery. You are the administrator implementing change requests and resolving incidents. This is a fictional commercial Azure lab with government-contractor-style documentation; it is not an Azure Government deployment or evidence of regulatory compliance.

This guide maps the course to MRTG practice and defines operating standards. Use the [lab index](progress.md) for assignments and status, and the [lab template](lab-template.md) to document performed work. Check current service documentation and tenant prerequisites before each build.

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

The primary course is [AZ-104 Microsoft Azure Administrator — Complete Exam Prep](https://www.udemy.com/course/70533-azure/) by Scott Duffy. The mapping below covers all 26 sections and lectures 1–187, the practice test, and both role plays, based on enrolled-course screenshots supplied September 16, 2026. These establish curriculum order, not course completion.

Use Udemy to set the topic order, Microsoft Learn to explain and verify behavior, and MRTG to practice and prove it. The official exam study guide remains the coverage checklist. When a lecture differs from current documentation or observed behavior, investigate and document the difference.

Lab numbers remain stable references. Use the study order here instead of completing labs strictly 01–32. This preserves earlier links and avoids rebuilding the whole curriculum around changing lecture numbers.

### Enrolled-course alignment — sections 1–5 confirmed

| Section / lectures | Course activity | MRTG action and completion checkpoint |
|---|---|---|
| 1 / 1 | Welcome | Understand the series workflow; no Azure build required. |
| 1 / 2–3 | Account options; sign-in assignment | Start Lab 01: sign in to the existing dedicated MRTG account, identify the actual subscription, status, and role. Do not create another account just to follow the demonstration. |
| 1 / 4–5 | Budget lesson and assignment | Continue Lab 01: inspect costs, verify available credits rather than assuming them, and review/create the budget. Finish the empty tagged resource-group and cleanup exercise from the lab checklist. |
| 1 / 6–10 | Player guidance, study guide, study plan, FAQ, resources | Use for orientation. Download course resources privately; do not redistribute course PDFs or screenshots into this public repository. The course's 30-day plan is optional, not a deadline. |
| 2 / 11–14 | Azure services, compute, storage, networking overview | Review familiar fundamentals. Explain where MRTG's tenant, subscription, workload, data, and network fit; preview Lab 02. No extra paid deployment required. |
| 3 / 15–17 | Scripting expectations, command patterns, management tools | Complete Lab 01's read-only command exercise; begin Lab 07 inventory. Explain the commands rather than running unexplained copied scripts. |
| 3 / 18 | PowerShell Core and Az module installation demo | Follow the demonstrated setup if using local PowerShell; record the actual environment/tool versions. Validate authentication and resource-group listing. |
| 3 / 19 | Subscription switching | Inspect and explicitly select the intended MRTG subscription; verify context before any mutation. One subscription is sufficient—do not create a second solely for this exercise. |
| 4 / 20–22 | Entra purpose, editions, multiple directories | Prepare Lab 03: inspect the existing tenant, identity types, permissions, and available licenses. Explain AD DS versus Entra ID. |
| 4 / 23–25 | Tenant-creation changes, creation, switching | Study the workflow and verify the intended existing tenant. A new tenant is not a prerequisite for this series. |
| 4 / 26–27 | Premium P2 trial and purchase demonstrations | Review only by default. Neither activation nor purchase is required; record licensing-dependent practical gaps. |
| 4 / 28 | Custom domains | Review the process. Use the existing tenant domain for core labs; domain purchase is not required. |
| 5 / 29 | Exam-change note | Check the current official objective list against the course note. |
| 5 / 30–32 | Users, groups, licenses | Perform Lab 03 using synthetic users and assigned groups. Perform license changes only when a suitable unused entitlement exists. Validate membership and document cleanup. |
| 5 / 33–34 | Administrative units and devices | Review and inspect available information; optional MRTG context, not new core labs or a reason to enroll personal devices. |
| 5 / 35 | Bulk operations | Extend Lab 03 with a tiny synthetic CSV operation if supported. Record successes and errors; remove test objects afterward. |
| 5 / 36 | External users | Continue Lab 03 using an owned secondary identity if available; record the practical gap otherwise. |
| 5 / 37 | Self-service password reset | Perform Lab 06 if appropriately licensed; otherwise document the configuration and validation plan as Design-only. |

**Next study step:** Lab 01’s portal baseline is validated. Review section 2, then complete the read-only CLI/PowerShell exercise at section 3. Record course and Learn completion separately in [progress](progress.md).

### Enrolled-course alignment — sections 6–15 confirmed

| Section / lectures | Topic | MRTG action and checkpoint |
|---|---|---|
| 6 / 38–39 | RBAC and administrative roles | Lab 04: distinguish directory administration from Azure resource permissions and define test identities/scopes. |
| 6 / 40–42 | Storage identity access | Do the minimum Lab 13 account/container setup, then Lab 14 identity authorization tests. Record allowed and denied data actions separately from management access. |
| 6 / 43 | Custom roles | Optional Lab 04 extension: inspect/modify a narrowly scoped test role if required; understand built-in roles first. Remove test assignments and custom definitions afterward. |
| 6 / 44–45 | Resource-group scope and assignment interpretation | Finish Lab 04: compare direct/inherited access across two disposable groups. Update the access matrix with observed results. |
| 7 / 46–48 | Hierarchy, subscription, cost tools | Labs 02 and 07; revisit Lab 01 cost baseline without repeating account creation. |
| 7 / 49–52 | Locks and policies | Lab 05: test audit/deny and deletion protection on disposable targets. Record distinct causes of failure. |
| 7 / 53 | Tags | Lab 02: apply MRTG metadata and verify resources as well as resource groups. |
| 7 / 54 | Resource moves | Inspect supported moves now; reserve VM move validation for Lab 20 once its dependencies exist. |
| 7 / 55–56 | Policy scripting and management groups | Labs 05 and 02: scoped automation and hierarchy review; do not relocate the existing subscription merely to mirror the demo. |
| 7 / 57–58 | Subscription/policy exercises | Reuse course work for Labs 02/05/07 when the validation and cleanup requirements are met. |
| 8 / 59–61 | Account creation and redundancy | Lab 13: choose a small appropriate account configuration and explain the redundancy tradeoff. |
| 8 / 62 | Access tiers | Labs 13/15: compare tier suitability for the tiny synthetic dataset; estimate retrieval/retention implications before changes. |
| 8 / 63 | Public/private networking | Review now; perform full private-path validation after Labs 08–12. Record the pending practical dependency. |
| 8 / 64 | Data protection | Lab 15: create test versions/deletions and verify recovery. |
| 8 / 65–67 | Encryption, account completion, storage services | Lab 13: inspect selected settings; do not create every storage service simply because it is listed. |
| 8 / 68–70 | Keys, SAS, stored policies, Entra authorization | Lab 14: test scoped access, expiry/revocation, and credential boundaries on disposable data. Keep credentials out of evidence. |
| 8 / 71–72 | Storage hands-on exercises | Reuse validated Lab 13/14 work; supplement with MRTG denial tests and cleanup. |
| 9 / 73 | Lifecycle management | Lab 15: configure the rule and distinguish configuration evidence from observing a later scheduled action. |
| 9 / 74 | Object replication | Lab 17: satisfy prerequisites, copy a small object, verify the destination, and clean up both sides. |
| 9 / 75–76 | AzCopy and storage browser | Lab 13: transfer synthetic files and verify contents/counts. |
| 10 / 77–78 | File shares and snapshots | Lab 16: create a small share and verify recovery; track identity-based SMB prerequisites separately. |
| 11 / 79–83 | VM creation, disks, networking, management, connection | Lab 19 with a minimal Lab 08 network prerequisite. Inspect costs and access before deployment; verify an actual connection. |
| 11 / 84 | VM availability | Lab 21: compare availability design choices and validate only the feasible lab configuration. |
| 11 / 85–86 | Resize and extra disks | Labs 19–20: inspect constraints, perform supported changes, and verify test data. |
| 11 / 87 | Bastion | Lab 12 administration-access portion; check prerequisites and price before a short deployment. Do not require all later networking labs first. |
| 11 / 88–90 | Scale sets and scaling | Lab 21: set a small maximum instance count, validate scaling, and delete the test estate. |
| 11 / 91 | PowerShell VM deployment | Repeat a selected Lab 19 operation through reviewed commands; explain parameters and scope. |
| 11 / 92–93 | VM and scale-set exercises | Consolidate Labs 19–21; account for image resources and supporting disks in cleanup. |
| 12 / 94–98 | ARM reading, modification, and deployment | Lab 18: parameterize a small workload, inspect the proposed change, deploy, and validate. |
| 12 / 99–103 | Exports, extensions, VHD use, and practice | Lab 18: examine exported templates and dependencies. Treat extensions/VHD examples as selected exercises, not a requirement to deploy every variant. |
| 13 / 104–107 | Bicep, editing/deployment, ARM decompilation | Complete Lab 18: modify and rebuild a small configuration; inspect decompiled output and validate it. |
| 14 / 108–109 | SSE and Azure Disk Encryption | Labs 19–20: compare encryption layers and follow the current guidance below. ADE is conceptual/legacy review by default. |
| 15 / 110–114 | App Service deployment, settings, GitHub integration | Lab 23: deploy a tiny application and verify its response. Repository deployment automation is optional until the basic app works. |
| 15 / 115–116 | App scaling | Lab 24: compare scale up/out, choose supported settings, cap test capacity, and verify observed behavior. |
| 15 / 117–118 | Backup and networking | Labs 23–24: inspect plan support and prerequisites; test recovery/network behavior only within the priced session. |
| 15 / 119–120 | Custom DNS and TLS | Lab 23: validate applicable HTTPS settings; document domain/certificate mapping as design-only if prerequisites are unavailable. |
| 15 / 121 | App Service practice | Consolidate Labs 23–24. Include explicit staging/slot-swap and rollback exercises where supported, even if a lecture title does not name slots. |

**Dependency order:** The course teaches VM deployment before ARM/Bicep. Build the first small VM through the portal, then use Lab 18 to reproduce selected configuration when sections 12–13 arrive. Lab numbering does not force templates before the initial VM. Repeat only enough to demonstrate reproducibility.

**Encryption update:** Lecture 109 covers ADE. Microsoft's current [managed disk encryption guidance](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) recommends encryption at host for new VMs and schedules ADE retirement for September 15, 2028. Study the distinctions, but use an eligible encryption-at-host configuration for the new MRTG workload rather than making ADE deployment a core requirement. Verify supported VM/disk combinations before deploying.

### Enrolled-course alignment — sections 16–20 confirmed

| Section / lectures | Topic | MRTG action and checkpoint |
|---|---|---|
| 16 / 122–125 | Containers, ACI, sizing/scaling, container groups | Lab 22: deploy a small test container, inspect configuration and logs, and explain container-group resource choices. Diagnose one controlled startup or port error. |
| 16 / 126 | Container Apps | Continue Lab 22: compare the deployment model with ACI and test a small suitable configuration within the session budget. Record actual scaling behavior rather than claiming it from settings alone. |
| 16 / 127–129 | Registry and image push/pull | Lab 22: use a disposable registry and suitable image; verify push/pull and deployment. If earlier lessons need an image before this registry exists, use an appropriate public sample first. Remove the registry, containers, and supporting resources after validation. |
| 17 / 130–132 | VNets, workload placement, subnet changes | Lab 08: validate an address plan against the existing MRTG ranges, deploy subnets, and explain workload placement. Revisit any temporary network used in the earlier VM labs. |
| 17 / 133–134 | Public IP and NIC association | Labs 08/19: inspect IP/NIC relationships and implement only the access path needed for the disposable workload. Include retained public IPs in cleanup. |
| 17 / 135 | RDP access | Labs 09/19: review the access rule, justify its source and destination, and test from the intended client. Do not copy a broadly exposed administrative-port rule into MRTG; use a narrowly scoped temporary path or the planned Bastion exercise. |
| 18 / 136–137 | Peering and global peering | Lab 10: validate connectivity and route reasoning. Cross-region deployment is a priced optional variation; do not add a second region simply to mirror the demonstration. |
| 18 / 138–139 | VNet gateway and gateway connection | Optional Lab 10 extension: document topology, prerequisites, routing, and a cost/cleanup estimate first. A live VPN gateway deployment is not required for the core peering exercise. If reviewed only, label it Design-only. |
| 18 / 140 | Networking practice | Consolidate Lab 10 with allowed/failed connectivity evidence and correction of a controlled route fault. |
| 19 / 141–143 | DNS, private zones, public zones | Lab 11: verify private name resolution; compare public-zone records and delegation. Distinguish creating a zone from proving that a public domain delegates to it. |
| 19 / 144 | App Service custom domain | Revisit Lab 23 only if a domain is available. Reuse earlier domain/TLS evidence rather than duplicating the exercise; otherwise retain the design-only gap. |
| 19 / 145 | DNS practice | Complete Lab 11's DNS portion with a wrong-record or resolution fault and a verified correction. Load-balancer work remains a separate portion of Lab 11. |
| 20 / 146–148 | NSGs, effective rules, application security groups | Lab 09: inspect effective rules, test permitted and denied traffic, and identify the rule responsible. Record the traffic direction, source, destination, and protocol. |
| 20 / 149–150 | Network troubleshooting and practice | Finish Lab 09 and introduce Lab 27 diagnostics when needed. Use evidence to distinguish DNS, routing, security-rule, and application failures; do not change multiple layers at once. |

**Deferred work to close after these sections:** Return to Lab 12 and the storage networking tests in Labs 13–14 when ready to validate the private access path. The shown titles do not explicitly establish coverage of every service/private-endpoint objective, so those MRTG tasks remain on the checklist. Load balancing and monitoring/backup are mapped in the confirmed sections 21–24 below.

**Study order:** containers (Lab 22) now follow App Service (Labs 23–24) in this course. Keep stable lab IDs and follow the actual course order. Documentation/evidence from earlier prerequisite exercises can be reused when it demonstrates the same behavior.

### Enrolled-course alignment — sections 21–24 confirmed

| Section / lectures | Topic | MRTG action and checkpoint |
|---|---|---|
| 21 / 151–153 | Load balancing, configuration, backend VMs | Complete Lab 11's load-balancer portion with a small disposable backend. Verify intended application responses and inspect health before introducing a fault. Reuse Lab 19 VM knowledge and Lab 09 traffic controls. |
| 21 / 154 | Quickly deploying a test environment from GitHub | Apply Lab 18 skills: inspect the referenced repository/template, resources, permissions, and cost before deployment. Keep MRTG parameters and cleanup boundaries. Do not treat a third-party deployment as reviewed merely because it is on GitHub. |
| 21 / 155 | Load-balancer troubleshooting | Lab 11: break one probe/backend/rule setting on the test workload, investigate the evidence, correct it, and retest. Record an incident report. |
| 21 / 156 | Application Gateway | Optional Lab 11 comparison/extension. Compare the business purpose with the load balancer; price the deployment and dependencies first. A conceptual review can remain Design-only rather than adding an expensive mandatory deployment. |
| 21 / 157 | Load-balancing practice | Consolidate Lab 11's evidence and cleanup; include backend VMs, disks, IPs, and balancing resources. |
| 22 / 158–160 | Network Watcher, diagnostic logs, practice | Lab 27: investigate a scoped network fault and record the source, destination, protocol, evidence, correction, and retest. Check current collection prerequisites and remove test diagnostics/workloads after use. |
| 23 / 161–162 | Monitor and resource diagnostics | Lab 25: answer a specific operational question using appropriate metrics/logs and a small amount of telemetry. Verify that the expected data actually arrives. |
| 23 / 163 | Monitor and VM Insights | Labs 25–26: inspect supported instrumentation and its prerequisites before enabling it. Do not assume resource diagnostic settings alone collect all guest OS logs or performance data. |
| 23 / 164 | Basic KQL queries | Lab 25: query a real test signal, explain each clause, and distinguish wrong time range/missing collection from an actual absence of events. |
| 23 / 165 | Traffic-management lab | The displayed title is a load-balancer/Application Gateway lab despite its location in the Monitor section. Map it primarily to Lab 11, reusing prior evidence. Add monitoring validation only if actually performed; do not assume this lecture covers alerts. |
| 24 / 166–169 | Backup, on-demand backup, file and full-VM recovery | Lab 28: select a small supported workload, inspect retention and cost, execute backup, and verify recovered content. A recovery point or successful job status alone is insufficient restore evidence. Perform only the feasible restore variants and label remaining gaps. |
| 24 / 170 | On-premises backup | Optional Lab 28 MRTG extension after confirming the current local environment and applicable agent/vault prerequisites. Do not install agents on existing domain controllers merely to mirror the lecture. |
| 24 / 171–173 | Backup reports, logs, and soft delete | Lab 28: inspect jobs/reporting, record protection and retention settings, and plan cleanup before enabling protection. Retained backup data may outlive the test workload. |
| 24 / 174–175 | Site Recovery and test failover | Lab 29: plan source/target support, replication, isolated test networking, recovery objectives, and cost. Execute a live test only when feasible, or document a tabletop as Design-only. Record test-failover cleanup and remaining protected resources. |
| 24 / 176–177 | Recovery practice | Consolidate Labs 28–29. Document observed restore results, elapsed time if measured, limitations, and cleanup. Keep simulated and executed recovery distinct. |

**Explicit completion tasks not established by these titles:** Keep Lab 26's alert rule, action group, alert-processing rule, and actual notification tests; Lab 27's Connection Monitor work; Lab 28's comparison of Recovery Services vault and Backup vault; and Lab 12's endpoint exercises. A title-only mapping cannot establish whether these are covered inside the videos. Perform or document each applicable lab task and use the official objective list for the final coverage review.

**After technical study:** Labs 30–32 remain the MRTG lifecycle scenario, capstone, and independent readiness review. They integrate course learning rather than requiring an additional course. Sections 25–26 below supply the final review and role-play mapping.

### Enrolled-course alignment — sections 25–26 confirmed; mapping complete

| Section / item | Topic | MRTG action and checkpoint |
|---|---|---|
| 25 / 178 | Identity/governance review | Lab 32: answer unfamiliar scenarios, inspect the access matrix, and repeat weak tasks from Labs 01–07 and 30. |
| 25 / 179 | Storage review | Lab 32: revisit Labs 13–17 where knowledge checks or practical evidence show gaps. Explain permissions, redundancy, and recovery tradeoffs. |
| 25 / 180 | Compute review | Lab 32: revisit Labs 18–24. Explain deployment dependencies and demonstrate a selected rebuild without a walkthrough. |
| 25 / 181 | Networking review | Lab 32: revisit Labs 08–12 and 27. Trace an actual allowed and failed connection and explain the relevant layer. |
| 25 / 182 | Monitoring/maintenance review | Lab 32: revisit Labs 25–29. Explain the alert signal, response, and verified recovery result; distinguish simulated work from live tests. |
| 26 / 183 | Congratulations | Course wrap-up only. Do not mark AZ-104 passed or labs validated based on reaching this lecture. |
| 26 / 184 | Certification renewal | Record a future maintenance action after certification is earned; verify current Microsoft renewal rules at that time. |
| 26 / 185 | AI-supported exam preparation | Use AI for explanations and practice review. Complete readiness assessments independently first; verify technical suggestions against documentation and observed behavior. AI assistance is not part of the real exam workflow. |
| 26 / 186 | Study guide | Use the supplied material privately as a review aid. Do not republish course files in the public repository. Check remaining coverage against the official objective list. |
| 26 / Practice Test 1 | Azure administrator practice test | Lab 32: take an independent attempt, record score/date and topic-level weaknesses, then investigate mistakes. Do not publish proprietary questions, answer keys, or screenshots of test items. |
| 26 / Role Play 1 | Critical VM outage: restore and report | Labs 28/31: rehearse incident triage, recovery choices, and a concise handover using the incident template. Label the role play simulated; it does not replace an actual restore test. |
| 26 / Role Play 2 | Cost optimization strategy | Labs 07/31: explain the actual cost ledger, propose justified changes, and discuss tradeoffs. If using hypothetical figures, label them synthetic. Do not claim savings that were not measured. |
| 26 / 187 | Further practice-test resources | Lab 32: use additional practice only to resolve readiness gaps. No additional purchase is required merely because a bonus lesson links to it. |

**Final study sequence:** finish the technical topics, perform Labs 30–31, and use section 25 plus section 26's test/role plays within Lab 32. Revisit weak tasks selectively. Keep course completion, lab validation, and passing the certification exam as three separate milestones.

**Readiness record:** date; domain; independent assessment result; reason for each error; corrective lab/task; retest result; remaining design-only gaps. Store topic summaries and original explanations, not proprietary test questions.

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

### Course-specific boundaries

- Reuse MRTG's existing tenant and subscription after validation. Watching account/tenant creation does not require creating another one.
- Premium-license purchase or trial demonstrations are information, not a requirement to buy or activate anything. Inspect eligibility and cost first.
- Do a minimal disposable storage setup when the early RBAC demos need it; return for the full storage labs later.
- For early storage networking lessons, complete the concept comparison now and the full private-path test after the network prerequisites. A basic authenticated storage exercise does not require anonymous access.
- Use a small temporary network for early VM practice if needed, then revisit its design in the networking labs. Defer advanced configuration rather than pretending prerequisites are complete.
- When revisiting a cleaned-up workload, rebuild from saved configuration. Logical continuity across labs does not require keeping everything running.

## Operating standards

- Use the dedicated MRTG account and `MRTG-AZ104-Lab-Subscription`, established in [Lab 01](../labs/lab-01-subscription-inventory-and-cost-baseline/README.md). The previous AZ-900 subscription was confirmed deleted. Verify the current directory, subscription, and permissions at each session.
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

## Lab records

Use the [32-lab index](progress.md) to open each assignment. Follow the course order above; lab numbering groups related work rather than prescribing session order.

Expand a planned assignment with the [lab template](lab-template.md) as work begins. [Lab 01](../labs/lab-01-subscription-inventory-and-cost-baseline/README.md) is the completed portal-baseline example. Keep evidence beside the step it supports, and follow the [evidence standard](evidence-standard.md). Reuse a course demonstration when it meets the MRTG validation requirements; do not repeat identical deployments for documentation.

AI supports planning, explanation, and documentation; the author performs and validates Azure work. Diagrams must distinguish deployed resources from proposed connections.

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
