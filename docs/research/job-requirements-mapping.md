# Job Requirements Mapping

Snapshot date: 2026-11-05. Job descriptions are examples, not universal hiring requirements.

## Roles reviewed

- Wipro AI Engineer: https://careers.wipro.com/job/Hyderabad-AI-Engineer-IND-500032/202739-en_US/
- TMLC GenAI Engineer: https://careers.tmlc.in/jobs/genai-engineer
- Capgemini Python Gen AI Engineer: https://careers.capgemini.com/job/Navi-Mumbai-Python-Gen-AI-Engineer/1442613233/
- Wipro Agentic AI Engineer: https://careers.wipro.com/job/Bengaluru-Agentic-AI-Engineer-IND-560035/207412_en_US/
- Blue Yonder Software Engineer II (Python, LangGraph, RAG, LLM): https://jda.wd5.myworkdayjobs.com/en-US/JDA_Careers/job/Software-Engineer-II--Python--LangGraph-OpenAI-Agents-SDK--RAG-LLM_263104

## Recurring themes observed

| Skill area | Evidence in sampled postings | NEXUS implementation evidence required |
|---|---|---|
| Python backend | FastAPI, Python fundamentals, REST APIs | Typed FastAPI modules, validation, async DB, integration tests |
| RAG and retrieval | Chunking, embeddings, vector DBs, semantic search | Ingestion pipeline, hybrid retrieval, RRF, reranking experiments |
| Agentic workflows | LangGraph, routing, planning, tools, state | Graph definitions, checkpoint/resume, tool permission tests |
| Evaluation | Recall@K/MRR/nDCG, agent/tool evaluation | Reproducible labelled benchmark and machine-readable reports |
| Security | Authentication, authorization, tenant isolation, guardrails | Cross-tenant negative tests, RLS, least-privilege tools, audit trail |
| Data engineering | ETL, SQL, structured/unstructured processing | Versioned ingestion jobs and deterministic spreadsheet analytics |
| Operations | Docker, CI/CD, monitoring, cloud | Reproducible local compose, CI gates, traces, runbook |

## Portfolio evidence strategy

A feature checkbox is not sufficient. For each competency, preserve code, tests, architecture rationale and a reproducible demo. For example, demonstrate hybrid retrieval against a labelled dataset and publish Recall@K/MRR with corpus size, configuration and limitations. Demonstrate tenant isolation with a negative integration test against PostgreSQL rather than relying on frontend filters.

## Scope caution

Some postings are for experienced engineers. A portfolio project can demonstrate relevant skills but does not substitute for required years of production experience, system ownership or domain expertise.
