# Lab 16 — Screenshot evidence

**35 published screenshots.**

| Screenshot | Evidence and qualification |
|---|---|
| [lab16-azure-files-smb-connectivity-failed.png](lab16-azure-files-smb-connectivity-failed.png) | CLIENT01 TCP 445 failure; not a permissions-denial test. |
| [lab16-cost-review-2026-11-08.png](lab16-cost-review-2026-11-08.png) | November 2026 filtered to the Lab 16 group: breakdown tiles <0.01; Actual cost unavailable; chart reports no cost; currency not visible. |
| [lab16-cleanup-complete.png](lab16-cleanup-complete.png) | Successful Azure resource-group deletion and remaining NetworkWatcherRG. |
| [lab16-client-domain-trust-verified.png](lab16-client-domain-trust-verified.png) | Secure-channel test returned True. |
| [lab16-client-network-and-domain-verified.png](lab16-client-network-and-domain-verified.png) | Domain DNS, TCP 443 baseline, and secure-channel health. |
| [lab16-client01-domain-membership.png](lab16-client01-domain-membership.png) | CLIENT01.mrtg.local domain membership. |
| [lab16-department-folders-created.png](lab16-department-folders-created.png) | Finance and HR directories; access-key authentication. |
| [lab16-department-group-membership-and-replication-verified.png](lab16-department-group-membership-and-replication-verified.png) | AD group members and zero-failure replication summary. |
| [lab16-department-users-and-groups.png](lab16-department-users-and-groups.png) | Synthetic local AD users and groups. |
| [lab16-file-restored-to-live-share.png](lab16-file-restored-to-live-share.png) | Live share listing after restoration; Finance document is 60 B. |
| [lab16-file-share-review.png](lab16-file-share-review.png) | Share creation review: departments, SMB, Transaction optimized; setup evidence. |
| [lab16-finance-test-file-deleted.png](lab16-finance-test-file-deleted.png) | Live file absent after deletion. |
| [lab16-finance-test-file-restored.png](lab16-finance-test-file-restored.png) | Finance file returned after snapshot restoration. |
| [lab16-finance-test-file-uploaded.png](lab16-finance-test-file-uploaded.png) | Original Finance file uploaded; 60 B. |
| [lab16-finance-user-signin-verified.png](lab16-finance-user-signin-verified.png) | whoami and Finance group token; not Azure authorization. |
| [lab16-host-azure-files-smb-connectivity-failed.png](lab16-host-azure-files-smb-connectivity-failed.png) | Physical host TCP 445 failure. |
| [lab16-host-smb-connectivity-failed.png](lab16-host-smb-connectivity-failed.png) | Repeated physical-host TCP 445 failure. |
| [lab16-host-storage-https-connectivity-verified.png](lab16-host-storage-https-connectivity-verified.png) | Physical-host TCP 443 succeeds to storage endpoint. |
| [lab16-hr-user-signin-verified.png](lab16-hr-user-signin-verified.png) | whoami and HR group token; not Azure authorization. |
| [lab16-identity-based-access-not-configured.png](lab16-identity-based-access-not-configured.png) | All three Azure Files identity sources disabled. |
| [lab16-resource-group-review.png](lab16-resource-group-review.png) | Proposed resource group and tags; creation review. |
| [lab16-resources-before-cleanup.png](lab16-resources-before-cleanup.png) | Pre-cleanup single-account inventory; subscription ID redacted. |
| [lab16-restored-file-content-verified.png](lab16-restored-file-content-verified.png) | Original text readable after restoration; no hash check or visible SAS query. |
| [lab16-share-snapshot-created.png](lab16-share-snapshot-created.png) | Share snapshot listed before deletion/recovery. |
| [lab16-storage-account-advanced.png](lab16-storage-account-advanced.png) | Storage account advanced; configuration/creation evidence, not a department access test. |
| [lab16-storage-account-basics.png](lab16-storage-account-basics.png) | Storage account basics; configuration/creation evidence, not a department access test. |
| [lab16-storage-account-data-protection.png](lab16-storage-account-data-protection.png) | Storage account data protection; configuration/creation evidence, not a department access test. |
| [lab16-storage-account-deployment-complete.png](lab16-storage-account-deployment-complete.png) | Storage account deployment complete; configuration/creation evidence, not a department access test. |
| [lab16-storage-account-encryption.png](lab16-storage-account-encryption.png) | Storage account encryption; configuration/creation evidence, not a department access test. |
| [lab16-storage-account-networking.png](lab16-storage-account-networking.png) | Storage account networking; configuration/creation evidence, not a department access test. |
| [lab16-storage-account-review-security.png](lab16-storage-account-review-security.png) | Storage account review security; configuration/creation evidence, not a department access test. |
| [lab16-storage-account-review.png](lab16-storage-account-review.png) | Storage account review; configuration/creation evidence, not a department access test. |
| [lab16-storage-account-security.png](lab16-storage-account-security.png) | Storage account security; configuration/creation evidence, not a department access test. |
| [lab16-storage-account-tags.png](lab16-storage-account-tags.png) | Storage account tags; configuration/creation evidence, not a department access test. |
| [lab16-storage-https-connectivity-passed.png](lab16-storage-https-connectivity-passed.png) | Physical-host TCP 443 retest succeeds. |

All 35 screenshots are indexed. Updated sanitized copies replace the affected originals; subscription ID, physical host name, and correlation ID are removed where applicable.

Storage setup pages do not independently establish final settings. Duplicate connectivity and restoration captures preserve intermediate observations. No TCP failure is presented as an authorization denial. The restored text was visually verified, without a captured hash comparison.

[Lab results](../README.md)
