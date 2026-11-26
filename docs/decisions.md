# Architecture and operations decisions

Decisions distinguish accepted plans from configurations demonstrated in the lab.

| ID | Decision | Reason | Tradeoff | Status |
|---|---|---|---|---|
| ADR-001 | Use disposable workloads and preserve configuration/evidence | Control lab cost and enable rebuilds | Rebuild effort between sessions | Accepted plan |
| ADR-003 | Validate cloud-only identities before optional hybrid work | Avoid introducing unverified synchronization dependencies | Entra synchronization remains deferred; local AD DS/private VPN file access demonstrated separately in Lab 16 | Plan extended by Lab 16 |
| ADR-004 | Separate Operations and Security into tagged resource groups | Make departmental ownership and resource scope explicit | Tags identify responsibility but do not enforce permissions; subscription Owner still inherited | Demonstrated and cleaned up in [Lab 02](../labs/lab-02-resource-organization-and-management-hierarchy/README.md) |
| ADR-006 | Use Entra Free and administrator-assisted recovery for Lab 06; retain premium identity features as study/design topics | Complete a practical recovery workflow without buying user licenses or activating trials | Forgotten-password SSPR is excluded from live validation; Azure resource charges remain separate | Recovery demonstrated and active-user cleanup verified in [Lab 06](../labs/lab-06-password-recovery-and-licensing/README.md); [series baseline](licensing-and-prerequisites.md) accepted |
| ADR-007 | Review assigned memberships and scoped Azure RBAC manually; replace excessive Contributor with Reader | Match access to the reviewer's read-only business need without premium identity licensing | Manual review requires recorded findings and separate access tests; automated Entra Access Reviews remain untested | Demonstrated and cleaned up in [Lab 07](../labs/lab-07-access-review-and-cost-review/README.md) |
| ADR-008 | Establish an address plan using two private /24 subnets within a /16 VNet; validate an overlapping /25 before deploying workloads | Demonstrate configuration validation and preserve explicit address ownership | Separate subnet ranges do not demonstrate traffic isolation; no workload connectivity was tested | Demonstrated and cleaned up in [Lab 08](../labs/lab-08-address-plan-and-subnets/README.md) |
| ADR-010 | Use two disposable private-IP VMs and a narrowly scoped /24 drop route to investigate peering connectivity | Compare successful traffic, effective route selection, failure, and recovery while changing one routing variable | Default outbound access was temporarily enabled and NSGs were absent for this isolated exercise; no production hardening or SSH authentication claim | Demonstrated and cleaned up in [Lab 10](../labs/lab-10-peering-and-route-investigation/README.md) |
| ADR-012 | Combine container-scoped managed identity with a Blob private endpoint and Bastion Developer entry | Read data without stored account keys and administer a VM without a public IP | Private DNS and data roles both matter; Developer access has SKU limitations, and metered endpoint/compute usage still requires cost review | Demonstrated and cleaned up in [Lab 12](../labs/lab-12-private-access-and-administrator-entry/README.md) |
| ADR-013 | Use Entra-authenticated portal transfers and local SHA-256 comparisons for three synthetic files | Demonstrate data authorization and verify transferred bytes without stored account keys | Public network reachability was enabled for the workstation; account-scoped Contributor is broader than container-only access; a retry resolved a CSV mismatch but did not establish its cause | Demonstrated and cleaned up in [Lab 13](../labs/lab-13-storage-baseline-and-transfer/README.md) |
| ADR-016 | Preserve initial Lab 16 failure/recovery evidence, then rebuild with P2S VPN and a file private endpoint | Direct public TCP 445 failed; private path enabled domain-user testing | Metered gateway ran across an overnight pause; final rebuild cost unverified | Initial deferral superseded by successful November 12 tests and cleanup in [Lab 16](../labs/lab-16-department-file-access-and-the-ad-bridge/README.md) |
| ADR-016A | Use local AD DS, default SMB Share Contributor permission and group-based folder ACLs | Test existing domain users without introducing Entra synchronization | Share-level eligibility is broad; department separation depends on Windows ACLs; no per-group Azure RBAC claim | Finance/HR own-folder read/write and cross-read denial validated; AES-256 Kerberos captured |
| ADR-016B | Use a temporary CLIENT01 hosts override for the normal storage hostname | Resolve the private endpoint while preserving the CIFS service name | Lab workaround; production hybrid DNS forwarding not validated | Private SMB tests passed; override removed and DNS cache flushed |
| ADR-016C | Grant department groups CLIENT01 Remote Desktop Users membership | Permit separate test-user sessions without granting local administrator rights | Additional local sign-in access retained; independent of file ACLs | Group addition observed during session; no dedicated capture in final package |
| ADR-018 | Preserve Bicep and baseline parameter bytes with SHA-256; inspect overrides using what-if, then test a delete/recreate rebuild | Make intended changes and reconstruction reviewable from source and saved outputs | Provider rejection of priority 99 is preflight, not rollback; output equality and a no-change prediction do not compare every live property; generated storage name is scope-dependent | Demonstrated and cleaned up in [Lab 18](../labs/lab-18-reproducible-mrtg-deployment/README.md); 20 screenshots and six original deployment artifacts published |
| ADR-019A | Preserve unresolved Bastion failure and use a temporary direct-SSH fallback to complete lifecycle tests | Separate access-path troubleshooting from the VM and storage objectives; verify server fingerprint before sign-in | Public entry added temporarily; My IP rule capture is pre-save and no independent effective-source or external-denial proof was retained; no confirmed Bastion root cause | Lifecycle validated through fallback and group deleted in [Lab 19](../labs/lab-19-vm-lifecycle/README.md); Bastion entry remains unsuccessful |
| ADR-019B | Persist the data filesystem by UUID and compare a saved SHA-256 after resize and return | Identify the intended filesystem across device-name changes and check retained bytes | Hash fixture is a narrow persistence test, not backup/restore; nofail allows boot to continue if the disk is missing | Automatic mount and checksum passed after both size changes; original size restored |
| ADR-019C | Give the VM container-scoped Blob Data Reader and remove the administrator setup data role before tests | Separate workload read access, administrator bootstrap and subnet network admission | Service endpoint uses the public storage hostname; no private endpoint or VM role-revocation test | GET 200, PUT/cross-container GET 403 with permission-mismatch codes, then GET 200; group removed |
| ADR-020A | Snapshot an unmounted ext4 data disk and retain the original SHA-256 manifest on the OS disk | Compare recovery with a baseline outside the incident data | Manual quiescing and three fixtures do not prove application-consistent or scheduled backup | Snapshot recovery passed after controlled deletion/overwrite in [Lab 20](../labs/lab-20-disk-recovery-and-relocation/README.md) |
| ADR-020B | Identify restored copies by LUN and mount read-only with journal replay disabled | Original and restored filesystems share a UUID; avoid selecting the wrong copy or modifying recovery evidence | Explicit device identification required after attachment; no persistent boot-mount test | Three hashes passed before and after relocation |
| ADR-020C | Detach and move the restored disk between groups in the same region, then reattach and retest | Separate resource-group placement from recovered data integrity | Resource scope changes; regional migration and RBAC effects not tested | Before/after group views and post-move hashes captured; groups removed, final billing unverified |

## Lab 21 availability and capacity decisions

| Decision | Reason | Demonstrated result and limit |
|---|---|---|
| Flexible VMSS initially in zones 1 and 2, public Standard LB, private backend NICs | Separate application entry from individual guest administration | Zonal placement and service-failure routing observed; no zone outage or production SLA test |
| Cloud-init/systemd bootstrap in scale-set model | New capacity must arrive with the application | Manually added instance bootstrap verified; automatically added backend later served traffic; full original custom data not exported |
| Automatic repairs off during controlled service fault | Observe routing while failed guest service stays stopped | Surviving backend served sampled requests; repair behavior untested |
| Autoscale min/default 2, max 3; CPU >70%/5 min out and <30%/10 min in | Retain two backends and stay within 6-vCPU family quota | Successful 2 → 3 → 2 events; quota is not a spending cap or allocation guarantee |
| Short-lived systemd CPU load with 1200-second runtime bound | Exercise autoscale with bounded load duration | Both units active, later inactive; exact termination timing not measured |

## Lab 22 container delivery decisions

| Decision | Reason | Demonstrated result and limit |
|---|---|---|
| Basic registry, admin disabled, registry-scoped AcrPull identity | Deliver images without registry passwords | Role verified; ACI and Container Apps served the imported image; no push/revocation denial test |
| Import sample image and retain its observed digest | Focus on delivery and runtime operation | v1/digest captured; no image build, source modification or digest-pinned deployment |
| Stable API ARM templates after extension rejection | Make API selection explicit and retain successful artifacts | Environment/app deployments passed; original JSON hashes match; external prerequisites remain |
| Consumption profile, 0–1 replicas, no persistent log destination | Bound configured capacity and avoid a lab Log Analytics workspace | Configuration verified, not scale execution or production observability |
| Wrong ingress target port, then restore | Separate successful configuration from application reachability | 80/200 → 8081/503 → 80/200 sampled; no measured recovery-time guarantee |

## Lab 23 — Managed web application

| Decision | Reason | Observed evidence and limit |
|---|---|---|
| Keep Linux F1 and escalate quota | Complete the managed-app exercise without a paid-tier workaround | Central US and East US 2 attempts failed; support resolution preceded successful East US 2 plan creation |
| Use Python 3.12 and original source ZIP | Keep the app small and retain deployment inputs | Build/runtime success and matching SHA-256 values; version ranges are not a lockfile |
| Change LAB_ENVIRONMENT without code deployment | Separate configuration from source | Saved Validation and live Validation/200; immediate stale response was not counted as success |
| Test HTTPS redirect and temporary IPv4 deny | Verify exposure through actual requests | HTTP 301, HTTPS 403 under restriction, then 200 after explicit Deny removal |
| Preserve missing-cost evidence | Avoid attributing broader billing totals to one lab | No matching group in November 21 filter; no verified zero or final charge |

[Lab 23 results](../labs/lab-23-managed-web-application/README.md). Source was preserved before group deletion; provider registration and regional quota were retained.

## Lab 24 — Controlled application release

| Decision | Reason | Evidence and limit |
|---|---|---|
| One Linux S1 instance after quota and unit-price checks | Enable deployment slots for a disposable exercise | S1 0/30, regional 0/31; retail lookup USD 0.095/hour; actual usage not confirmed |
| Embed release versions in separate source ZIPs | Distinguish code movement from environment settings | Production 1.0 → 2.0 → 1.0 through two swaps, without redeploying between them |
| Mark LAB_ENVIRONMENT slot-specific | Keep environment labels attached to slots | Initial flags verified; staging saved/live Staging rechecked after both temporary mismatches |
| Deliberately swap back from a healthy release | Exercise rollback mechanics with a known-good version | Rollback verified, not recovery from an injected defect or database change |
| Retain original artifacts and remove paid plan | Preserve evidence before ending the deployment | Bundle and six member hashes matched; group existence=false; no-match cost capture retained |

[Lab 24 results](../labs/lab-24-controlled-application-release/README.md). Request samples do not establish zero downtime, automatic rollback or a recovery-time guarantee.

## Lab 25 — Logs and operational questions

| Decision | Reason | Evidence and limit |
|---|---|---|
| Administrative category to a disposable workspace | Investigate resource-management operations | Destination compared; category export is subscription-wide, target scope is in KQL |
| Separate empty target group and delete lock | Generate a controlled failure without workload data | ScopeLocked/Conflict recorded; pasted Bash guard also emitted an EOF error |
| Check source log and older workspace events | Separate source operation from ingestion delay | Target events appeared later; no ingestion SLA measured |
| Compare token object claim after Caller mismatch | Attribute the failed request using observed identity evidence | Signed-in object fingerprint matched; raw Caller mismatch unexplained |
| Preserve five queries/results before cleanup | Retain failure, chronology and successful retry | Original 12-file manifest verified; relative windows need adjustment for historical replay |
| Remove export and both groups | End disposable collection and resources | Empty export list and group absence; no permanent-purge or final-cost claim |

[Lab 25 results](../labs/lab-25-logs-and-operational-questions/README.md). Twelve-character fingerprints are pseudonymized comparisons. Alert notification and response automation remain outside this exercise.

## Lab 26 — Actionable alerts

| Decision | Reason | Result and limit |
|---|---|---|
| Native Activity Log alert and empty locked group | Generate a real management failure without compute/workspace | ScopeLocked and real fired alerts; not a workload outage or RBAC test |
| Test action group before live condition | Isolate email delivery from rule matching | Synthetic sample Success/email, then independent real email |
| Exact-name processing-rule filter at target scope | Limit suppression to the intended lab alert | Fired/Suppressed observed; no reliance on inbox absence alone |
| Re-enable detection after wrong-rule disable | Separate detection from notification suppression | Enabled readback and new unsuppressed alert/email verify recovery |
| Planned propagation waits | Avoid treating configuration saves as immediate enforcement | New outcomes observed; exact change timestamps and propagation duration not exported |
| Preserve final false checks with cleanup errors | Report observed state honestly | Groups absent; already-absent errors do not identify earlier deletion timing |

[Lab 26 results](../labs/lab-26-actionable-alerts/README.md). USD 10 budget thresholds rechecked; budget email delivery and attributable lab cost unverified.

## Cost follow-up reconciliation before Lab 27

Publish the reviewed November 22 cost package and November 23 group-filter searches while retaining previous dated observations. Record displayed service USD 0.00 separately from an unavailable Actual headline; record no-match searches as unavailable attribution. Repeated cost snapshots describe the same accumulated usage and are not additive. Lab 24 now has an attributable USD 0.06 posted snapshot; final invoices, credit application and cash spending remain unverified. The subscription budget and notification thresholds were revalidated in Lab 26, without claiming budget email delivery or a spending stop. [Cost ledger](cost-ledger.md).

## Lab 27 — Diagnose the enforcing network rule

| Decision | Reason | Result and limit |
|---|---|---|
| Check SKU restrictions after quota | Available family quota does not guarantee size availability | B2s restricted; B2s_v2 restrictions empty and deployment succeeded |
| Separate client/app subnets and a narrow /32 TCP 80 deny | Reproduce a specific application-path incident | Client failed while localhost app stayed healthy |
| Use IP flow verify plus real HTTP requests | Separate policy evaluation from actual reachability | Named deny rule; actual 200 → timeout → 200 |
| Individual VM endpoints and dedicated workspace | Keep monitor scope and destination explicit | Corrected portal configuration retained; no endpoint JSON export |
| Keep mixed fault window and narrow recovery window labeled | Avoid treating an aggregate rate as continuous loss | Red/53.5% over last hour, then green/0% in 8:05–8:07 PM window; no detection SLA |
| Delete monitor separately from lab group | Monitor stored in shared NetworkWatcherRG | Named regional monitor count=0 and group exists=false; shared watcher retained |

[Lab 27 results](../labs/lab-27-network-incident-response/README.md). No identity-license purchase, alert rule, automated remediation or final cost claim. Portal USD 0 banner and USD 0.3/month row were inconsistent estimates; combined session cost was not captured.
