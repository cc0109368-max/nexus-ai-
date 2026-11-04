# ADR-001: Modular Monolith with Separate Worker

- Status: Accepted for initial implementation
- Context: The product has multiple domains but is being developed by a small team/individual. Premature microservices would add deployment, tracing and consistency costs.
- Options: (1) microservices from day one, (2) modular monolith plus worker, (3) single process for API and long jobs.
- Decision: Modular monolith for request/transaction boundaries; separately executable worker for long-running document and evaluation jobs.
- Justification: Clear module boundaries with simpler local development and transactional consistency.
- Trade-offs: Modules share a deployment unit and database; strict dependency boundaries and tests are needed.
- Consequences: Split a module into a service only when scaling, ownership or isolation requirements justify it.
