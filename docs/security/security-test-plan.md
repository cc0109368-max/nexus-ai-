# Security Test Plan

- Authentication: wrong password, inactive user, malformed/expired token, duplicate registration, password hashing.
- Authorization: member can read own organization; non-member receives non-disclosing 404; role-based write denial.
- Tenant isolation: create two organizations and assert document/chunk/vector queries never cross boundaries using PostgreSQL RLS and app-level checks.
- Prompt injection: direct user prompt and malicious text embedded in PDF/DOCX; assert no privileged instruction override and no unauthorized tool invocation.
- Tool controls: invalid schema, missing permission, timeout, repeated idempotency key, approval denied and approval granted.
- Upload: extension/MIME mismatch, oversized file, malformed file, decompression bomb limits, empty/scanned PDF handling.
- Resource controls: request rate, token budget, max agent steps, max tool calls, worker concurrency.
- Output: malformed structured output, unsafe rendered HTML, fabricated/nonexistent citation rejection.
- Operations: ensure logs do not contain secrets or raw sensitive payloads; verify sanitized errors.
