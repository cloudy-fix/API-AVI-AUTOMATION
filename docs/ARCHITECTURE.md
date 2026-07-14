# VMware AVI API Automation Architecture

## Purpose

Automates VMware AVI tenant API operations using environment-driven configuration.

## Stack

Python, Requests, Postman, VMware AVI Controller API

## System Context

```mermaid
flowchart LR
    User["Operator config and tenant request"] --> App["Python automation script and Postman collection"]
    App --> Data["AVI controller session and tenant payload"]
    App --> Output["Created/managed AVI tenant"]
    Data --> Output
```
## Runtime Workflow

```mermaid
flowchart TD
    S1["Load environment config"] --> S2["Authenticate to AVI controller"]
    S2["Authenticate to AVI controller"] --> S3["Prepare tenant payload"]
    S3["Prepare tenant payload"] --> S4["Call tenant API"]
    S4["Call tenant API"] --> S5["Report provisioning result"]
```
## Production Readiness Notes

- Keep secrets in environment variables and commit only .env.example templates.
- Keep generated files, dependency folders, caches, and local databases out of version control.
- Run the GitHub Actions workflow before presenting or deploying changes.
- Update this document when the source layout, dependencies, or deployment model changes.

## Review Checklist

- Architecture diagram matches current source files.
- Workflow diagram matches the main user or data path.
- README links to this architecture document.
- CI workflow validates the project on every push and pull request.

