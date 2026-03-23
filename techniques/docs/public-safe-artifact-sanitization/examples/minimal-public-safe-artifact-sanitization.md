# Scenario

A support summary needs to share a command failure, but the raw output includes hostnames, private paths, and internal IDs.

## Raw excerpt

```text
ssh admin@ops-int.internal
cat /srv/private/customer-a/run-4821/error.log
job_id=INT-4821 service=payments-shadow-eu-west
```

## Shareable version

```text
ssh <redacted-user>@<generalized-host>
cat /srv/<generalized-path>/error.log
job_id=<generalized-id> service=<generalized-service>
```

## Sanitization note

- user, hostname, path segment, job ID, and service name were generalized
- the lesson preserved is that the failure surfaced through remote shell plus log inspection
- this artifact is safe to review as a sharing example only; it does not authorize the underlying action

## Boundary notes

- if the material is already public-safe, do not add unnecessary redaction
- if the main task is deciding whether the underlying action should proceed, use the approval-gate workflow first
- if the main task is to preview or execute the action, use the preview or safe-change workflow first
