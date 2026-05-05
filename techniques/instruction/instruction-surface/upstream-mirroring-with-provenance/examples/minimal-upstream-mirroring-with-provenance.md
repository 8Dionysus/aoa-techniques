# Minimal Upstream Mirroring With Provenance

Use one small source manifest entry plus one adjacent provenance file.

- source manifest entry:
  - names the upstream repository
  - names the upstream source path
  - names the local mirror destination
- mirrored local copy:
  - is refreshed from upstream
  - does not become the new canonical source
- provenance file:
  - preserves the upstream origin
  - stays adjacent to the mirrored copy

If the local collection now wants registry policy, installer behavior, or ranking logic, treat that as a separate technique.
