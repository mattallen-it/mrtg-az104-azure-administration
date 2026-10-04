# Lab 06 — Password reset and account recovery operations

![AZ-104](https://img.shields.io/badge/Exam-AZ--104-0078D4) ![Status](https://img.shields.io/badge/Status-Validated-2E7D32)

## Business problem and scope

MRTG needs an administrator-assisted recovery workflow for a synthetic cloud-only user who has forgotten their password. This exercise created a non-admin account, established a sign-in baseline, performed an administrator reset, tested password rejection and required password change, verified recovered sign-in, reviewed audit evidence, and removed the account from active users.

**Status: validated — administrator-assisted recovery and active-user cleanup.** Eleven execution screenshots were reviewed and support the revised workflow. Their GitHub publication is pending; filenames below identify reviewed captures, not repository image links. The earlier license inventory remains separate background evidence.

The exercise used Entra Free with no paid user-license purchase or trial. Administrator-assisted reset is distinct from end-user forgotten-password self-service password reset (SSPR). SSPR configuration, hybrid writeback, MFA reset, and application authorization were outside scope.

## Test identity and administration

| Setting | Observed value |
|---|---|
| Username | `lab06.recovery@mrtgcloudopsoutlook.onmicrosoft.com` |
| Display name | MRTG Lab06 Recovery User |
| Identity | Cloud-created internal Member; enabled at creation; on-premises sync No |
| Roles and groups | No added assignments shown on creation review |
| Credentials | Password values excluded from published evidence |
| Operator | Existing lab administrator; successful reset recorded in the portal and audit log |

Separate administrator and test-user browser sessions were used in the checkpoint procedure. A successful reset demonstrates that this operator could reset this target; it does not establish the least-privileged role required for every account type.

## Work performed and validation evidence

| Step | Reviewed result | Evidence |
|---|---|---|
| 1 | Reviewed enabled Member configuration; no added assignments shown | `lab06-recovery-user-review.png` |
| 2 | Created recovery user listed as Member with on-premises sync No | `lab06-recovery-user-created.png` |
| 3 | Initial My Account sign-in visible under the recovery identity | `lab06-initial-signin-verified.png` |
| 4 | Administrator reset confirmation; temporary password hidden | `lab06-admin-password-reset.png` |
| 5 | Controlled pre-reset-password test returned incorrect account/password error | `lab06-old-password-rejected.png` |
| 6 | Update your password prompt displayed with empty fields | `lab06-password-change-required.png` |
| 7 | My Account sign-in visible after the password-change and fresh-session procedure | `lab06-recovered-signin-verified.png` |
| 8a | Reset password (by admin): success; Successfully completed reset | `lab06-password-reset-audit.png` |
| 8b | Selected administrator reset targets the named recovery user and UPN | `lab06-password-reset-audit-target.png` |
| 8c | Change password (self-service): success; recovery user is the actor | `lab06-password-change-audit.png` |
| 9 | All users search for lab06.recovery returns 0 users | `lab06-recovery-user-cleanup.png` |

The source upload named `lab-06-password-recovery-and-licensing.png` contained the user-creation review; its intended repository filename is `lab06-recovery-user-review.png`. Duplicate download suffixes were removed from the intended repository filenames.

## Evidence boundaries

- Initial and recovered account-page screenshots establish signed-in identity. They do not independently reveal which password was entered or prove browser-session freshness. The checkpoint procedure required closing all test InPrivate windows and signing in again with the new password.
- The controlled old-password test produced an incorrect account/password message. The screenshot cannot independently prove the submitted secret; no password was captured.
- The required-change prompt and successful password-change audit event support the password-change stage. The initial account-page capture alone does not prove an initial password change.
- The administrator reset event at 2:32:09 PM local portal time on October 4, 2026 succeeded. Its Target(s) tab identifies the recovery user. A separate password-change event at 2:38:24 PM succeeded with that user as actor.
- “Change password (self-service)” is the audit activity label for the user's password change. It is not evidence of forgotten-password SSPR or a paid feature entitlement.
- Administrator identifiers and IP address were redacted from the redacted reset activity capture. Synthetic recovery-user identifiers remain visible to connect the evidence.
- No live session-revocation test, MFA reset, hybrid writeback, or application access test was performed.

## Cleanup

The synthetic account was deleted, and a refreshed All users search for `lab06.recovery` returned **0 users found / No results**. This validates absence from active users. Permanent deletion and the Deleted users state were not separately captured; recoverable deletion must not be described as permanent removal. The existing administrator, directory, subscription, and budget were retained.

No metered Azure workload was deployed for the recovery exercise. Billing was not independently verified. Private lab credentials should be removed after closing the test sessions.

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


## Lessons learned

- Separate administrator assistance, known-password change, and forgotten-password self-service recovery.
- Confirm the target account's source and identity before resetting credentials.
- Test recovery through a fresh sign-in procedure and preserve the limits of screenshot evidence.
- Review both the audit activity and its target; a successful event alone does not identify whose password changed.
- In production, verify the requester's identity and authorization before resetting credentials. This synthetic exercise does not validate a real identity-proofing process.
- Capture audit evidence before cleanup and distinguish active-user deletion from permanent removal.

## References

- [Create and delete users](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users)
- [Administrator password reset](https://learn.microsoft.com/en-us/entra/fundamentals/users-reset-password-azure-portal)
- [Audit log activities](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities)
- [SSPR licensing](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-licensing)
- [Series licensing and prerequisites](../../docs/licensing-and-prerequisites.md)

[All labs](../../docs/progress.md)
