# Security References

Research date: 2026-11-05.

## Primary reference

**OWASP GenAI LLM Top 10 2026** — published August 4, 2026.

Canonical repository: https://github.com/GenAI-Security-Project/GenAI-LLM-Top10

The 2026 categories include prompt injection, sensitive information disclosure, excessive agency, supply chain, data/model poisoning, unbounded consumption, misinformation, hidden context exposure, vector/embedding weaknesses and improper output handling.

## Application security baseline

- OWASP Top 10 Web Application Security Risks 2025: https://owasp.org/Top10/2025/
- FastAPI security documentation: https://fastapi.tiangolo.com/tutorial/security/
- PostgreSQL Row Security Policies: https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- pgvector project and filtering/index notes: https://github.com/pgvector/pgvector

## NEXUS threat controls to implement and test

| Threat | Required control | Verification evidence |
|---|---|---|
| Direct/indirect prompt injection | Treat retrieved content as untrusted data; separate instructions and evidence; restrict tools | Malicious document test cases and tool-denial assertions |
| Cross-tenant leakage | Tenant scoping in every query; RLS as defence in depth | PostgreSQL integration tests using distinct DB roles/tenant IDs |
| Excessive agency | Allowlisted tools, per-tool authorization, human approval for writes | Unauthorized action and approval-interrupt tests |
| Sensitive data disclosure | Secret redaction, least privilege, bounded logs and output review | Log scanning and authorization tests |
| Vector/embedding weaknesses | Validate source ownership before context construction; test index filtering behavior | Cross-tenant vector retrieval adversarial tests |
| Unbounded consumption | Upload, token, step, timeout, concurrency and rate limits | Boundary and load tests |
| Improper output handling | Validate structured model output and escape rendered content | Schema-failure and XSS regression tests |
| Supply-chain risk | Lock dependencies, scan vulnerabilities, review image provenance | CI dependency and container scans |

A prompt-level instruction is not an authorization boundary. Backend policy enforcement is mandatory.
