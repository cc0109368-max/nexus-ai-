# NEXUS AI

Enterprise Knowledge Intelligence and Agentic AI Platform.

> Engineering status: foundation scaffold. This repository is not yet a complete or production-ready enterprise platform. See [`docs/PROJECT_PROGRESS.md`](docs/PROJECT_PROGRESS.md) for verified scope and outstanding work.

## Current implementation

- Next.js / React / TypeScript enterprise workspace shell with explicit empty states (no fabricated metrics).
- FastAPI service with liveness/readiness endpoints.
- PostgreSQL-oriented SQLAlchemy models for users, organizations and memberships.
- Password hashing with Argon2 through `pwdlib`.
- Short-lived signed access tokens and membership-checked organization reads.
- Environment-based configuration and CORS allowlist.
- Docker Compose definitions for PostgreSQL + pgvector and Redis.
- Alembic migration environment.
- Initial security and architecture documentation.

Not implemented yet: document ingestion, embeddings, hybrid RAG, Gemini live calls, LangGraph workflows, approval execution, analytics, evaluation runner, observability dashboards, refresh-token rotation, complete RBAC, RLS policies and production deployment.

## Requirements

- Python 3.11+
- Node.js 20.9+
- Docker Engine + Docker Compose plugin (not available in the initial build environment)
- A Gemini API key for live model integration (not required for the current foundation)

## Local setup

1. Copy `.env.example` to `.env` and replace `SECRET_KEY` with a securely generated secret.
2. Start infrastructure: `docker compose up -d postgres redis`.
3. Create a Python virtual environment and install: `pip install -e '.[dev]'`.
4. Create migrations after reviewing the models: `alembic revision --autogenerate -m "identity foundation"`.
5. Review the generated migration, then run `alembic upgrade head`.
6. Start the API from `services/api`: `uvicorn app.main:app --reload --app-dir .`.
7. In `apps/web`, run `npm install` then `npm run dev`.

The frontend currently displays a truthful engineering preview. The UI does not imply that unimplemented backend features are available.

## API

- `GET /health/live`
- `GET /health/ready`
- `POST /v1/auth/register`
- `POST /v1/auth/login`
- `GET /v1/organizations/{organization_id}` (membership required)

OpenAPI docs are available at `/docs` in non-production environments.

## Security notes

- Never commit `.env` or credentials.
- The sample database password is local-development-only.
- Access tokens are short-lived; refresh-token rotation and revocation are not implemented yet.
- The initial membership check is application-level. PostgreSQL RLS and adversarial tenant-isolation tests remain mandatory before production use.
- The broad exception handler intentionally avoids returning internal exception details. A sanitized structured logging pipeline still needs to be added.

## Architecture and research

See `docs/architecture/`, `docs/research/`, `docs/security/` and `docs/decisions/`.
