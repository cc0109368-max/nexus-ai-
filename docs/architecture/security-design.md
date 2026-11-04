# Security Design — Initial Baseline

## Implemented in the initial scaffold

- Passwords are hashed using the Argon2id via `argon2-cffi`.
- Access tokens are signed and short-lived (20-minute default).
- Organization read route checks membership in the backend and returns 404 for non-members to avoid confirming another tenant's organization ID.
- CORS uses an explicit origin allowlist.
- Basic response security headers are added.
- Production mode disables interactive API docs.
- Generic API exception responses do not expose exception details.

## Not yet implemented

Refresh-token rotation/revocation, email verification, password reset, MFA, session/device management, login throttling, complete RBAC, invitation flows, audit trail, PostgreSQL RLS, object storage isolation, malware scanning, prompt-injection tests, tool permission system, secret redaction and vulnerability scanning.

## Important caveat

The current code is an initial engineering scaffold, not a completed security control set. Do not expose it to public traffic until the missing controls and tests are implemented.
