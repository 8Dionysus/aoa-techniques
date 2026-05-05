# Skill Vs Command Boundary Checklist

- [ ] One reusable skill artifact is named separately from one user-facing command artifact.
- [ ] The skill still makes sense without reading a specific command first.
- [ ] The command owns invocation name, arguments, numbered steps, or structured output.
- [ ] The command references or invokes the skill instead of copying its full meaning.
- [ ] Another agent or command can reuse the same skill without changing its core contract.
- [ ] Command-specific constraints do not silently redefine the skill boundary.
- [ ] The draft includes one explicit overlap sentence against `AOA-T-0013` and `AOA-T-0027`.
- [ ] The draft stays out of upstream mirroring, marketplace curation, routing policy, and shell-command doctrine.
- [ ] The wording remains public-safe and does not depend on donor-specific plugin mechanics.
