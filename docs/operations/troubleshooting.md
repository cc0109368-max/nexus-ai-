# Troubleshooting

- API cannot connect to PostgreSQL: verify the database container is healthy, port 5432 is available and `DATABASE_URL` matches the local credentials.
- Readiness endpoint returns 500: inspect protected API logs and database availability; liveness alone does not imply readiness.
- Authentication token rejected: check the API `SECRET_KEY`, token expiry and whether the token was issued by this environment.
- Web app cannot reach API: confirm API origin, CORS allowlist and browser network response.
- Gemini integration unavailable: confirm backend key and a currently supported model identifier; do not fall back to fabricated model output.
