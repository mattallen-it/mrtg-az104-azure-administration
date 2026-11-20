# Lab 22 evidence gallery

**16 published screenshots.** PNG bytes are preserved; the fault filename typo is corrected. The author hid billing identity in the cost capture. Historical disposable lab endpoints remain; no credentials are present.

| Capture | Observation and limit |
|---|---|
| [lab22-resource-providers-registered.png](lab22-resource-providers-registered.png) | Four requested providers Registered; identity provider was checked earlier. |
| [lab22-registry-created.png](lab22-registry-created.png) | Registry Succeeded, Basic and AdminEnabled False; creation command specifies RBAC mode. |
| [lab22-image-import-verified.png](lab22-image-import-verified.png) | mrtg-web tag v1 and its SHA-256 digest; no build or digest-pinned deployment claim. |
| [lab22-registry-pull-role-verified.png](lab22-registry-pull-role-verified.png) | Role list shows AcrPull / ServicePrincipal for the selected identity at registry scope. |
| [lab22-aci-deployed.png](lab22-aci-deployed.png) | ACI creation with identity attachment and registry identity; Succeeded and public IP. |
| [lab22-aci-running-http-200.png](lab22-aci-running-http-200.png) | ACI Running, zero restarts, private-registry image reference; HTTP 200 and sample HTML. |
| [lab22-aci-tagged-and-stopped.png](lab22-aci-tagged-and-stopped.png) | Three tags read back; ACI group Stopped before pause. |
| [lab22-containerapp-environment-api-version-error.png](lab22-containerapp-environment-api-version-error.png) | Extension requested unsupported 2025-10-02-preview; failed intermediate state. |
| [lab22-containerapp-environment-deployed.png](lab22-containerapp-environment-deployed.png) | Removed appLogsConfiguration; validation followed by ARM deployment Succeeded. |
| [lab22-containerapp-environment-verified.png](lab22-containerapp-environment-verified.png) | Live environment Succeeded, Consumption profile, null logging destination/configuration. |
| [lab22-containerapp-deployed.png](lab22-containerapp-deployed.png) | App template deployment Succeeded; screenshot is partial, full uploaded JSON preserved separately. |
| [lab22-containerapp-https-200.png](lab22-containerapp-https-200.png) | Latest and ready revisions match; HTTPS 200 with sample HTML. |
| [lab22-containerapp-ingress-fault-503.png](lab22-containerapp-ingress-fault-503.png) | Wrong target port 8081 applied successfully; request returned 503. |
| [lab22-containerapp-ingress-recovered-200.png](lab22-containerapp-ingress-recovered-200.png) | Port 80 restored; HTTPS returned 200. |
| [lab22-resource-group-deleted.png](lab22-resource-group-deleted.png) | Delete attempt found group absent; existence check false; deletion timing not established. |
| [lab22-cost-review-2026-11-19.png](lab22-cost-review-2026-11-19.png) | Author-redacted monthly lab-group cost: USD 0.28 total/registry, ACI <0.01; snapshot, not invoice. |

[Lab results](../README.md) · [Templates](../templates/README.md)
