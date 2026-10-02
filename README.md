# Website Security Header Auditor

Read-only defensive tooling for reviewing HTTP response security headers. It consumes a saved JSON response and makes no network requests.

## Usage

```powershell
python auditor.py examples/response.json
```

Checks include Content-Security-Policy, HSTS, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, and server-version disclosure. Use it alongside a formal penetration test and application review.

Created 2026-10-02. Defensive use only.
