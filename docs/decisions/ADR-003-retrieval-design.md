# ADR-003: PostgreSQL Hybrid Retrieval

- Status: Proposed
- Context: Enterprise search needs semantic recall, exact term matching and strict metadata/tenant filters.
- Options: Dense-only vector search; external search cluster; PostgreSQL full-text + pgvector hybrid retrieval.
- Decision: Start with PostgreSQL full-text and pgvector, fuse rankings with RRF, and make reranking configurable.
- Justification: One primary datastore reduces operational burden while supporting a measurable hybrid baseline.
- Trade-offs: Search scale and specialized ranking needs may eventually justify a dedicated search service.
- Consequences: Benchmark exact versus approximate search, filter selectivity and index recall on representative data before choosing production index settings.
