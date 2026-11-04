# Database Design — Initial Identity Slice

## Tables authored

- `users`: unique normalized email, full name, Argon2 password hash, active flag, creation timestamp.
- `organizations`: display name, unique slug, creation timestamp.
- `organization_members`: user-to-organization membership, role label and unique organization/user pair.

UUID primary keys are used. Foreign keys cascade on membership deletion. Organization reads require a matching membership row.

## Planned entities

Document versions/chunks, ingestion jobs, conversations/messages/citations, agent runs/checkpoints/tool executions/approval requests, datasets/evaluation runs/results, model usage, audit logs and internal tasks.

## Required before production

- Generate and review Alembic migration against PostgreSQL.
- Add explicit role enum/check constraints and role authorization policy.
- Add organization/workspace ownership to every tenant-scoped record.
- Add PostgreSQL RLS policies and test using non-owner DB roles.
- Define retention/deletion and object-storage cleanup behavior.
- Add transactional outbox or another reliable mechanism for database-to-worker job dispatch.
- Add unique constraints/idempotency keys for ingestion and state-changing tools.
