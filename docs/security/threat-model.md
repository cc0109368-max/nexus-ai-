# Threat Model — Initial

## Assets

Tenant documents, extracted text, embeddings, conversations, credentials, organization membership, tool credentials, approval records and usage/audit metadata.

## Adversaries and failure sources

Malicious tenant users, compromised accounts, malicious uploaded documents, poisoned source content, accidental developer misconfiguration, compromised dependencies and over-permissioned agent tools.

## High-priority threats

1. Cross-tenant retrieval or document access.
2. Direct/indirect prompt injection causing data disclosure or unauthorized tool calls.
3. Credential/session compromise.
4. Unbounded model/agent consumption.
5. Parser exploits or malicious file payloads.
6. Incorrect citations or confident unsupported answers.
7. Tool retries causing duplicate state changes.

## Required mitigations

Backend membership and resource authorization; RLS; safe parser isolation and file limits; untrusted-content boundaries; allowlisted tools; explicit approval for consequential writes; strict schema validation; bounded steps/timeouts/token budgets; idempotency; evidence validation; secret-safe logging; audit trails; dependency scanning; reproducible evaluation.

## Residual risks

Prompt injection cannot be eliminated by a single prompt. Model output may still be wrong. Retrieval filters, tool permissions, deterministic validators and human review reduce impact but require adversarial testing and operational monitoring.
