# ADR-004: Defence-in-Depth Tenant Isolation

- Status: Accepted
- Context: A multi-tenant knowledge platform must prevent cross-organization document and vector leakage.
- Options: Frontend filtering; application query filters only; application authorization plus PostgreSQL RLS.
- Decision: Enforce membership/permissions in backend services and add PostgreSQL RLS as defence in depth. Apply filters before constructing LLM context.
- Justification: The browser and LLM are not trusted authorization boundaries.
- Trade-offs: RLS session context, connection pooling and background workers require careful design and tests.
- Consequences: Test using real PostgreSQL connections and non-owner roles; never treat HNSW/vector filtering as a security boundary.
