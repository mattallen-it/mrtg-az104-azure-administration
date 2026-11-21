# Lab 24 release artifacts

Original uploaded release files are preserved byte for byte. The duplicate upload has the same bundle hash as the first upload and the captured Cloud Shell value.

| File | Purpose |
|---|---|
| [v1/app.py](v1/app.py) and [v1/requirements.txt](v1/requirements.txt) | Version 1.0 source, initially deployed to production |
| [v2/app.py](v2/app.py) and [v2/requirements.txt](v2/requirements.txt) | Version 2.0 source, initially deployed to staging |
| [v1.zip](v1.zip) and [v2.zip](v2.zip) | Original source ZIP deployments; member bytes match the respective source directories |
| [SHA256SUMS](SHA256SUMS) | Original manifest for all six release files |
| [lab24-release-artifacts.zip](lab24-release-artifacts.zip) | Original preservation bundle, including manifest |

Bundle SHA-256: `4395d173592df8ffb24dd1bd145f8c3b4aee02c1195bbe2e418fb7076a88611a`.

From this directory, verify the six original release files:

```bash
sha256sum --check SHA256SUMS
```

Both releases use Flask and Gunicorn version ranges, not locked dependency versions. Their VERSION value is embedded in code; LAB_ENVIRONMENT is read at runtime. The application returns JSON at `/` and a static healthy/version response at `/health`. There is no database or secret in this source bundle. It does not provision infrastructure or supply installed dependencies.

Observed deployments selected Python 3.12, enabled SCM_DO_BUILD_DURING_DEPLOYMENT=true on both slots and set LAB_ENVIRONMENT to Production or Staging as a deployment-slot setting. Both releases were healthy; rollback was a deliberate second swap. No independent infrastructure rebuild was tested.

[Lab results](../README.md)
