# Concrete API Contract Boundary

This example shows a more concrete consumer-visible boundary change handled through `contract-test-design`.

## Scenario

An API endpoint returns `422` validation errors consumed by a web client. The team wants to refactor internal validation code, but the response contract must keep the same public shape: `code`, `message`, and `field` for each validation failure.

## Flow

1. Name the real boundary explicitly: the HTTP response body returned to the web client, not the internal validator objects.
2. Describe the bounded contract in consumer terms: required error keys, expected status code, and the rule for missing-field failures.
3. Add or update a contract-oriented test around the endpoint response so the client-visible payload is the surface under validation.
4. Refactor the internal validation and mapping logic without widening or renaming the consumer-facing error shape.
5. Run the contract check and report what the boundary now guarantees, while leaving broader API versioning or authentication changes out of scope.

## Why this stays bounded

- The example is anchored to one observable consumer-facing payload contract.
- Internal refactor freedom remains available as long as the public response contract stays stable.
- The example does not broaden into general property coverage or a wider API redesign.
