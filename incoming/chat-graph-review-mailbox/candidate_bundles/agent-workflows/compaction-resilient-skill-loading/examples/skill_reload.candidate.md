# minimal example seed

Before compaction:
- `skills = [checks, release-notes]`

After compaction:
- active context no longer includes the skill list

Recovery step:
- reload `checks` and `release-notes` from canonical skill references

The point of the example is that skill recovery is explicit and bounded after context loss.
