# Lab 23 application source

Original Cloud Shell source and deployment ZIP, preserved byte for byte. All three SHA-256 values match the captured Cloud Shell output.

| File | Purpose |
|---|---|
| [app.py](app.py) | Flask application; `/` returns lab metadata and `LAB_ENVIRONMENT`, `/health` returns a static healthy response |
| [requirements.txt](requirements.txt) | Flask and Gunicorn version ranges used for the successful remote build |
| [lab23-app.zip](lab23-app.zip) | Original deployed source ZIP; both source files are at the archive root |
| [SHA256SUMS](SHA256SUMS) | Checksums for source files and deployment ZIP |

The archive does not include installed dependencies or infrastructure. Dependency ranges are not a lockfile. The health route is an application endpoint; it does not establish that App Service Health Check was configured.

The observed Linux Python 3.12 deployment used `SCM_DO_BUILD_DURING_DEPLOYMENT=true` and initially `LAB_ENVIRONMENT=Development`. Changing the latter to `Validation` was verified through the running application without redeploying code.

To verify the preserved files from this directory:

```bash
sha256sum --check SHA256SUMS
```
