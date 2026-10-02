"""Offline website security header auditor. It reads a saved response JSON."""
import argparse, json

REQUIRED = {"content-security-policy": "high", "strict-transport-security": "high", "x-content-type-options": "medium", "referrer-policy": "medium", "permissions-policy": "medium"}

def audit(headers: dict[str, str]) -> list[dict]:
    normalized = {k.lower(): v for k, v in headers.items()}
    findings = []
    for name, severity in REQUIRED.items():
        if name not in normalized:
            findings.append({"rule": "WSA001", "severity": severity, "header": name, "message": f"Missing {name} response header."})
    if normalized.get("server", "").lower().startswith(("apache/", "nginx/", "iis/")):
        findings.append({"rule": "WSA002", "severity": "low", "header": "server", "message": "Server header exposes product details."})
    return findings

def main():
    parser = argparse.ArgumentParser(description="Audit saved website response headers without making network requests.")
    parser.add_argument("response_json", help="JSON object containing response headers")
    args = parser.parse_args()
    with open(args.response_json, encoding="utf-8") as handle:
        payload = json.load(handle)
    headers = payload.get("headers", payload)
    findings = audit(headers)
    print(json.dumps({"findings": findings, "finding_count": len(findings)}, indent=2))
    raise SystemExit(1 if findings else 0)

if __name__ == "__main__":
    main()
