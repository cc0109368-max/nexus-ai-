# Local Deployment Runbook (Target)

1. Install Docker Engine/Desktop and Compose plugin.
2. Copy `.env.example` to `.env`; replace the development secret.
3. Start PostgreSQL and Redis with `docker compose up -d postgres redis`.
4. Install Python dependencies and apply reviewed Alembic migrations.
5. Start API and web app in separate terminals.
6. Verify `/health/live`, `/health/ready`, OpenAPI and frontend.
7. Configure Gemini credentials only in the backend environment when provider integration is implemented.

This runbook is a target workflow. Docker and application startup have not been verified in the initial build environment.
