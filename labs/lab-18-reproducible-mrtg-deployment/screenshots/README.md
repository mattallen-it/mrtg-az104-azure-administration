# Lab 18 evidence gallery

**20 published screenshots.**

Original submitted PNG bytes, ordered by execution phase. Subscription and tracking identifiers were redacted in the submitted images. The expected priority error is preflight validation, not a partial-deployment rollback. Configuration readback does not establish workload traffic or data access.

| # | Capture | Observed evidence |
|---|---|---|
| 01 | [Cloud Shell context and Bicep installation](lab18-cloud-shell-context-and-bicep-version.png) | Enabled subscription and Bicep CLI 0.49.2 after installation. |
| 02 | [Bicep build](lab18-bicep-build-verified.png) | Build exit code 0 and source/compiled file listing; the screenshot contains only part of the source. |
| 03 | [Template resources and resource group](lab18-template-resources-and-resource-group.png) | Three ARM resource types; tagged Central US group creation succeeded. |
| 04 | [Initial NSG plan](lab18-initial-what-if-nsg.png) | NSG create, Deny-All-Inbound priority 1000; subscription identifier redacted. |
| 05 | [Initial network and storage plan](lab18-initial-what-if-network-storage-summary.png) | VNet/subnet/NSG association, storage controls and three-create summary; subscription identifiers redacted. |
| 06 | [Baseline deployment](lab18-baseline-deployment-succeeded.png) | Succeeded with four outputs and Environment Lab. |
| 07 | [Baseline inventory](lab18-baseline-resource-inventory.png) | Three resources in centralus, all tagged Lab. |
| 08 | [Storage security readback](lab18-storage-security-settings-verified.png) | HTTPS, TLS1_2, disabled public network/Shared Key/anonymous blob access. |
| 09 | [NSG and subnet readback](lab18-nsg-rule-and-subnet-association-verified.png) | Priority 1000 inbound deny and snet-app /24 associated with the intended NSG. |
| 10 | [Repeat baseline plan](lab18-baseline-repeat-what-if.png) | Three no change; scope identifier redacted. |
| 11 | [Environment override plan](lab18-environment-tag-change-what-if.png) | Three tag-only changes from Lab to Test; scope identifier redacted. |
| 12 | [Environment override applied](lab18-environment-tag-change-applied.png) | Succeeded with output Test and live resource tags Test. |
| 13 | [Expected invalid-priority rejection](lab18-invalid-nsg-priority-rejected.png) | Priority 99 rejected at provider preflight, allowed range 100–4096, CLI exit 1; subscription/tracking identifiers redacted. |
| 14 | [Valid rule and baseline restoration](lab18-valid-priority-and-baseline-restored.png) | Existing priority remained 1000; restored deployment Succeeded with Environment Lab. |
| 15 | [Baseline source preserved](lab18-source-integrity-before-rebuild.png) | Both source checksums OK; baseline outputs exported and archive downloaded. |
| 16 | [Deletion before rebuild](lab18-resource-group-removed-before-rebuild.png) | Named resource group deleted; existence returned false. |
| 17 | [Clean rebuild](lab18-clean-rebuild-succeeded.png) | Same group recreated and deployment Succeeded with matching names and Environment Lab. |
| 18 | [Output and source comparison](lab18-rebuild-outputs-and-source-match.png) | Output comparison exit 0; both source checksums OK. |
| 19 | [Rebuild consistency plan](lab18-rebuild-what-if-no-change.png) | Three no change after rebuild; scope identifier redacted. |
| 20 | [Final cleanup](lab18-final-resource-group-cleanup-verified.png) | Named group deleted again; existence returned false. |

[Lab results](../README.md) · [Deployment artifacts](../deployment/README.md)
