# Public Safe Artifact Sanitization Checklist

Use this checklist when reviewing a shareable artifact that claims to have removed or generalized sensitive technical detail.

- [ ] Secrets, tokens, private paths, topology clues, and unsafe operational details were checked deliberately.
- [ ] The shared artifact preserves the technical lesson.
- [ ] The sanitization level matches the intended audience.
- [ ] Raw sensitive detail was not left behind by accident.
- [ ] Remaining uncertainty or limits of sanitization are named clearly.
- [ ] The artifact is still understandable after redaction or generalization.
- [ ] A reviewer can tell what was generalized or omitted without reading the raw source.
- [ ] The note does not turn into approval gating or execution planning.
- [ ] The sanitized artifact is not being used as proof that the underlying action is allowed or safe.
- [ ] The material is not already clearly public-safe and minimal.
- [ ] The main question is not whether the action is allowed.
- [ ] The main question is not how to preview or execute the underlying operational change.
- [ ] The work is not really incident response that belongs in a response workflow instead of share-prep.
