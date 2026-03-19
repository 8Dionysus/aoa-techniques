# Section Lift Checklist

Use this checklist to confirm that a section-level lift still behaves like a derived markdown surface rather than a second authored source.

- The lifted sections come from one authoritative `TECHNIQUE.md` bundle.
- The lifted scope is explicit and limited to stable recurring headings.
- Section order in the derived output matches the source markdown order.
- Consumers can route from the lifted output back to the source bundle and heading.
- The workflow does not need section IDs, a new `kag` domain, or graph semantics to stay useful.
