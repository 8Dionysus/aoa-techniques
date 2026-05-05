# recommendation-truth-vs-host-actionability checklist

- [ ] recommendation truth is computed before host-actionability filtering
- [ ] host inventory source and precedence are explicit
- [ ] `activate_now` contains only host-executable items
- [ ] router-only items remain visible in `must_confirm`, `suggest_next`, or `actionability_gaps`
- [ ] explicit host overrides beat auto-discovered inventory when both are present
- [ ] the report still explains why an item was recommended even when it is not executable
- [ ] the bundle stays smaller than discovery, marketplace, or registry doctrine
- [ ] the public wording stays reusable and sanitized
