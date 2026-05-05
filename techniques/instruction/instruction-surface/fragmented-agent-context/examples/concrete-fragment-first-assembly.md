# Concrete Fragment-First Assembly

Scenario: a public repository wants agent context to stay reviewable in small source fragments while still being able to publish one consolidated view.

1. Write the context contract in small fragment files instead of one long hand-edited document.
2. Give each fragment one bounded responsibility, such as intent, contracts, or review notes.
3. Define a deterministic assembly order that combines the fragments without changing their meaning.
4. Keep a traceability marker or equivalent mapping so each assembled section can be traced back to its source fragment.
5. Treat the assembled view as a derived publication surface, not as the primary editable home.
6. When meaning changes, edit the fragments and regenerate the assembled view from them.

This stays inside the technique because the fragments own the meaning and assembly stays subordinate to fragment-first authorship.
