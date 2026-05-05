# Minimal Degraded Handoff

1. Retrieval succeeds on a bounded query surface.
2. A downstream KAG stage fails or returns no useful expansion.
3. The owner repo publishes a degraded retrieval-only result instead of pretending full hybrid grounding still happened.
4. The run emits one source-owned stressor receipt with:
   - what failed
   - what stayed bounded
   - what fallback was taken
5. Later improvement work cites that receipt in an explicit adaptation delta rather than inferring the history from memory.
