# API Contracts — Initial Slice

Base path: `/v1`. JSON errors use FastAPI's validation/error response conventions. OpenAPI is generated from typed route declarations in non-production mode.

## Health

- `GET /health/live` — process liveness; does not prove database readiness.
- `GET /health/ready` — executes `SELECT 1` against PostgreSQL and returns readiness only when the database connection succeeds.

## Authentication

### `POST /v1/auth/register`

Request: `{ "email": "person@example.com", "full_name": "Person Name", "password": "at-least-12-characters", "organization_name": "Example Org" }`

Success: `201` with `access_token`, `token_type`, `expires_in`, `user` and initial `organization`.

Failure: `409` when an account with the email already exists; `422` for schema/email/password validation failures.

### `POST /v1/auth/login`

Request: `{ "email": "person@example.com", "password": "..." }`

Success: `200` with a short-lived bearer token and the user's first organization membership.

Failure: `401` for invalid credentials; `403` when the user has no available organization membership.

## Organization

### `GET /v1/organizations/{organization_id}`

Requires `Authorization: Bearer <access_token>`. Returns organization metadata only if the authenticated user is a member. A non-member receives `404` to avoid disclosing organization existence.

## Known contract gaps

Refresh/logout, organization creation after registration, invitations, workspace routes, roles/permissions, pagination, standardized error envelope and audit event APIs are not implemented yet. The initial auth response returns the first membership and is not a multi-organization workspace selector.
