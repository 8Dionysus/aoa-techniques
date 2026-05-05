# Summary Contract Checklist

Use this checklist to validate whether a smoke path really follows `contract-first-smoke-summary`.

- A summary file is produced for the smoke path.
- The summary is machine-readable JSON.
- The summary includes an explicit success or error status.
- The summary captures enough observed data for basic diagnosis.
- Exit code aligns with summary status.
- Downstream consumers can use the summary without scraping raw logs.
- Summary discovery is stable through a fixed path or a stable `--summary-json` flag.
