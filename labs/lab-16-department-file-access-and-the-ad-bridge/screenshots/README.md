# Lab 16 evidence gallery

**71 published screenshots.** Evidence covers two disposable deployments. The initial November 7 recovery/connectivity phase is distinct from the November 10–12 rebuild and successful department access tests. An old unconfigured identity page or failed public SMB probe does not describe the final rebuilt state.

## Initial deployment — recovery and public SMB investigation

| Screenshot | Observation and limit |
|---|---|
| [lab16-azure-files-smb-connectivity-failed.png](lab16-azure-files-smb-connectivity-failed.png) | CLIENT01 TCP 445 failure; not a permissions-denial test. |
| [lab16-cleanup-complete.png](lab16-cleanup-complete.png) | Successful Azure resource-group deletion and remaining NetworkWatcherRG. |
| [lab16-client-domain-trust-verified.png](lab16-client-domain-trust-verified.png) | Secure-channel test returned True. |
| [lab16-client-network-and-domain-verified.png](lab16-client-network-and-domain-verified.png) | Domain DNS, TCP 443 baseline, and secure-channel health. |
| [lab16-client01-domain-membership.png](lab16-client01-domain-membership.png) | CLIENT01.mrtg.local domain membership. |
| [lab16-cost-review-2026-11-08.png](lab16-cost-review-2026-11-08.png) | November 2026 filtered to the Lab 16 group: breakdown tiles <0.01; Actual cost unavailable; chart reports no cost; currency not visible. |
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

## Rebuild — domain repair, private access and department tests

| Screenshot | Observation and limit |
|---|---|
| [lab16-client-domain-trust-repaired.png](lab16-client-domain-trust-repaired.png) | CLIENT01 secure-channel repair returned True. |
| [lab16-client-trust-verified-both-dcs.png](lab16-client-trust-verified-both-dcs.png) | Trust checks against both DCs returned True; secure-channel query succeeded. |
| [lab16-finance-domain-signin-verified.png](lab16-finance-domain-signin-verified.png) | Finance domain identity, logon server and group token verified. |
| [lab16-hr-domain-signin-verified.png](lab16-hr-domain-signin-verified.png) | HR domain identity, logon server and group token verified. |
| [lab16-rebuild-resource-group-review.png](lab16-rebuild-resource-group-review.png) | Rebuild resource-group review; configuration evidence. |
| [lab16-vnet-address-space-and-subnets.png](lab16-vnet-address-space-and-subnets.png) | Rebuild address-space and subnet review. |
| [lab16-vnet-subnets-deployed.png](lab16-vnet-subnets-deployed.png) | Private-endpoint and gateway subnets visible after deployment. |
| [lab16-vpn-gateway-settings.png](lab16-vpn-gateway-settings.png) | VPN gateway setup settings; configuration review. |
| [lab16-vpn-gateway-review.png](lab16-vpn-gateway-review.png) | VPN gateway creation review, including SKU and public IP. |
| [lab16-vpn-gateway-deployment-complete.png](lab16-vpn-gateway-deployment-complete.png) | Gateway deployment completion; not a user-access test. |
| [lab16-vpn-root-certificate-created.png](lab16-vpn-root-certificate-created.png) | Root certificate creation and public metadata; no private key shown. |
| [lab16-point-to-site-configured.png](lab16-point-to-site-configured.png) | P2S pool, OpenVPN and certificate authentication configured; root Valid. |
| [lab16-vpn-client-certificates-created.png](lab16-vpn-client-certificates-created.png) | Admin/Finance/HR PFX export names and lengths only; no passwords or private-key bytes. |
| [lab16-azure-vpn-client-installed.png](lab16-azure-vpn-client-installed.png) | Azure VPN Client installation succeeded. |
| [lab16-client01-admin-vpn-connected.png](lab16-client01-admin-vpn-connected.png) | Administrator VPN session Connected. |
| [lab16-vpn-address-route-and-dc-connectivity.png](lab16-vpn-address-route-and-dc-connectivity.png) | VPN address/routes captured; DC LDAP probe used the local Ethernet path, not Azure VPN. |
| [lab16-rebuild-storage-account-basics.png](lab16-rebuild-storage-account-basics.png) | Rebuild Azure Files storage basics; intended configuration. |
| [lab16-rebuild-storage-review.png](lab16-rebuild-storage-review.png) | Rebuild storage review, including disabled public network access. |
| [lab16-rebuild-storage-security-tags-review.png](lab16-rebuild-storage-security-tags-review.png) | Rebuild security, encryption and tags review. |
| [lab16-file-private-endpoint-review.png](lab16-file-private-endpoint-review.png) | File endpoint, VNet/subnet and private DNS integration review; subscription ID removed. |
| [lab16-file-private-endpoint-dns.png](lab16-file-private-endpoint-dns.png) | Endpoint IP 10.160.1.4 and Azure private DNS association visible; not proof of client DNS forwarding. |
| [lab16-private-endpoint-smb-connectivity-success.png](lab16-private-endpoint-smb-connectivity-success.png) | Normal storage name resolves to 10.160.1.4 with client hosts override; TCP 445 succeeds over VPN. |
| [lab16-azfileshybrid-installed.png](lab16-azfileshybrid-installed.png) | AzFilesHybrid 0.3.2 imported; Join-AzStorageAccount available. |
| [lab16-ad-domain-and-share-permission-verified.png](lab16-ad-domain-and-share-permission-verified.png) | Final AD domain mrtg.local, NetBIOS MRTG and default SMB Share Contributor readback. |
| [lab16-department-folder-acls.png](lab16-department-folder-acls.png) | Finance/HR respective groups have Modify; inherited administrative/system entries retained. |
| [lab16-share-root-acl-verified.png](lab16-share-root-acl-verified.png) | Root department entries are Read/Execute; broad user grants absent in captured ACL. |
| [lab16-finance-vpn-connected.png](lab16-finance-vpn-connected.png) | Finance-session VPN connected, certificate authentication, address and routes; certificate subject not displayed. |
| [lab16-finance-vpn-smb-connectivity.png](lab16-finance-vpn-smb-connectivity.png) | Finance identity and successful private TCP 445 test via VPN in one capture. |
| [lab16-finance-access-validation.png](lab16-finance-access-validation.png) | Finance read/create/readback succeed; HR known-file read denied. |
| [lab16-finance-kerberos-aes256-ticket.png](lab16-finance-kerberos-aes256-ticket.png) | Finance CIFS service ticket uses AES-256; KDC MRTG-DC02. |
| [lab16-hr-vpn-smb-connectivity.png](lab16-hr-vpn-smb-connectivity.png) | HR identity and successful private TCP 445 test via VPN. |
| [lab16-hr-access-validation.png](lab16-hr-access-validation.png) | HR read/create/readback succeed; Finance known-file read denied. |
| [lab16-hr-kerberos-aes256-ticket.png](lab16-hr-kerberos-aes256-ticket.png) | HR CIFS service ticket uses AES-256; KDC MRTG-DC02. |
| [lab16-azure-resource-group-cleanup-verified.png](lab16-azure-resource-group-cleanup-verified.png) | After rebuild deletion, no matching lab group in selected subscription. |
| [lab16-client-hosts-cleanup-verified.png](lab16-client-hosts-cleanup-verified.png) | DNS flush succeeds and hosts search for rebuilt storage name returns nothing. |
| [lab16-storage-ad-object-cleanup-verified.png](lab16-storage-ad-object-cleanup-verified.png) | Storage AD computer deletion confirmed; remaining matching computer count zero. |

## Interpretation and publication boundaries

Setup forms show proposed settings. Final domain/share readback, ACL output, two user sessions, permitted file operations, denied cross-department reads and CIFS ticket metadata establish the tested results. No PFX, password, private key, storage key or VPN profile is included. Submitted sanitized images are used without altering test output.

The client used a temporary hosts override; Azure private DNS association is not evidence of hybrid DNS forwarding. The November 8 cost screenshot belongs to the first deployment only. Final rebuild costs, local installed-certificate removal, PFX deletion and VM shutdown are not independently verified. Cross-department write/delete and revocation were not separately tested. Root-certificate public data and certificate/ticket metadata are not private-key or exported-ticket material.

[Lab results](../README.md)
