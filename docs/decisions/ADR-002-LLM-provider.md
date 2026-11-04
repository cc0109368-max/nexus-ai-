# ADR-002: Provider Adapter with Gemini as Initial Provider

- Status: Accepted as target design; live integration not yet implemented
- Context: The platform should avoid coupling product logic to one model vendor.
- Options: Gemini-only calls throughout the codebase; provider abstraction; multi-provider routing from day one.
- Decision: Define a provider contract and implement Gemini first. Add another provider only when tested requirements justify it.
- Justification: Keeps prompts/workflows portable while avoiding unnecessary provider complexity.
- Trade-offs: Provider capability differences must be represented explicitly; a lowest-common-denominator interface can hide useful features.
- Consequences: Chat, embeddings, tool calls and structured output capabilities require separate capability/configuration checks. No model ID is hardcoded until verified against current official docs.
