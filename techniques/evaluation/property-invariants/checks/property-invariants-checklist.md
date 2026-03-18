# Property Invariants Checklist

Use this checklist to verify that an invariant-oriented check is expressing a meaningful property rather than random-data theater.

- The invariant names a real domain or system truth.
- The property would fail for a meaningfully broken implementation.
- The generator or repeated input strategy is bounded and understandable.
- The broader input space adds signal beyond a tiny fixed example list.
- The result states what the invariant constrains and what it still does not prove.
- Any companion example tests used for readability remain clearly distinct from the invariant itself.
