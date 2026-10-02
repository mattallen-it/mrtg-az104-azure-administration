# Lab 06 — Password reset and account recovery operations

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Status](https://img.shields.io/badge/Status-In_progress-orange)

## Business problem and scope

MRTG needs an administrator-assisted recovery workflow for a synthetic cloud-only user who has forgotten their password. The revised exercise will create a non-admin account, establish a sign-in baseline, perform an administrator reset, validate the forced password change and subsequent sign-in, review available audit evidence, and remove the account.

**Status: in progress — execution and validation pending.** The first user-creation review checkpoint has been provided; no completed checkpoint for the revised exercise has yet been reviewed. The earlier licensing assessment is retained below as background. It is not evidence that password recovery succeeded.

The exercise uses Entra Free with no paid user-license purchase or trial. Administrator-assisted reset is distinct from end-user self-service password reset (SSPR). No SSPR configuration, hybrid writeback, or MFA reset is included.

## Planned test identity

| Setting | Planned value |
|---|---|
| Username | `lab06.recovery` in the existing tenant domain |
| Display name | MRTG Lab06 Recovery User |
| Identity | Cloud-created internal Member; account enabled |
| Roles and groups | No added roles or group assignments |
| Credentials | Generated temporary password; stored privately |
| Operator | Existing lab administrator; actual authority and operation outcome to be recorded |

A role displayed in the directory does not itself validate a reset. The target must have its credentials managed in this tenant. Use separate browser sessions for administrator and test-user actions.

## Execution checkpoints — results pending

| Step | Planned validation | PNG filename |
|---|---|---|
| 1 | Review user configuration before creation; no password visible | `lab06-recovery-user-review.png` |
| 2 | Confirm created user and cloud-only Member properties | `lab06-recovery-user-created.png` |
| 3 | Complete initial password change and verify test-user sign-in to an available account page | `lab06-initial-signin-verified.png` |
| 4 | Perform administrator reset and capture confirmation with temporary password hidden | `lab06-admin-password-reset.png` |
| 5 | In a fresh sign-in session, verify the pre-reset password is rejected; stop after one controlled attempt | `lab06-old-password-rejected.png` |
| 6 | Sign in with reset temporary password and capture forced-change prompt with fields blank | `lab06-password-change-required.png` |
| 7 | Set a new private password and verify fresh sign-in with it | `lab06-recovered-signin-verified.png` |
| 8 | Inspect available audit records for the named target and reset event; record actual activity and result | `lab06-password-reset-audit.png` |
| 9 | Delete only the synthetic account and verify its absence from active users | `lab06-recovery-user-cleanup.png` |

These filenames are planned captures, not existing evidence links. Instructions will be given one checkpoint at a time. Do not capture passwords, QR codes, recovery codes or tokens. Follow any required authentication registration without weakening tenant security settings. A registration requirement or access failure must be documented separately from password failure.

## Validation and cleanup record

User creation, initial sign-in, administrator reset, old-password rejection, forced change, recovered sign-in, audit review and cleanup are all **pending**. No reset success, session revocation, application authorization, or completed cleanup is claimed. Deletion from active users may leave a recoverable object in Deleted users; record that state accurately.

## Previous readiness assessment — background

## Observed results

| Check | Observed result | Evidence boundary |
|---|---|---|
| Directory overview | Microsoft Entra ID Free; operator's card displayed Global Administrator | Screenshot reviewed during the exercise; not evidence of every API permission |
| Licenses → All products | “No account SKUs found” | Published inventory below; no eligible SKU shown at inspection |
| License usage | Feature reported a Premium license requirement | Applies to that feature; not an inventory result |
| Password reset → Properties | Page opened and displayed the end-user/admin distinction | Current saved selection was not confidently established from the capture |
| Password reset → Authentication methods | 403: “Read password reset policy forbidden” | Refresh returned the same error, reported by the operator; cause unresolved |
| Live end-user recovery | Not attempted | No successful reset, registration or sign-in validation claimed |

![All products inventory with no account SKUs found](screenshots/lab06-license-inventory.png)

The earlier consumer-account access error and the later 403 are access observations. Neither is proven to be caused by missing licensing. A license purchase must not be represented as a verified fix.

## Licensing assessment

Microsoft's scenario-specific SSPR guidance distinguishes changing a known password from resetting a forgotten password. Entra Free supports the former; cloud-only end-user recovery requires an eligible Microsoft 365 or Entra P1/P2 license. Hybrid writeback has additional requirements. Any user intended to benefit must be appropriately licensed.

A Global Administrator recovery experience would not validate the planned ordinary-user pilot. Azure subscription Owner, Entra directory roles and feature entitlement are separate checks.

The [series licensing review](../../docs/licensing-and-prerequisites.md) covers all 32 current scopes. No Premium purchase is required to continue after revising this lab; planned service tiers and the Lab 16 identity source still need deployment-specific review.


## Lessons to validate during execution

- Separate administrator assistance, known-password change and self-service recovery.
- Confirm account source and operator authority before attempting a reset.
- Establish fresh sign-in results rather than treating an existing browser session as proof.
- In production, verify the requester's identity and authorization before resetting credentials. This lab uses a synthetic account and does not validate a real identity-proofing process.
- Report observed password/audit behavior and unresolved blockers precisely.

## References

- [Create and delete users](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users)
- [Administrator password reset](https://learn.microsoft.com/en-us/entra/fundamentals/users-reset-password-azure-portal)
- [SSPR licensing](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing)
- [Series licensing and prerequisites](../../docs/licensing-and-prerequisites.md)

[All labs](../../docs/progress.md)
