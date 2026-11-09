# HTTP Security Headers & Web Exposure Auditor

<p align="center">
  <img src="https://img.shields.io/badge/Security-Defensive_Auditor-blue?style=flat" alt="Type">
  <img src="https://img.shields.io/badge/Status-Architectural_Showcase-success?style=flat" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
</p>

> 🔒 **Technical Showcase & Architecture Specification**  
> *This repository provides public architectural documentation, system specifications, and implementation summaries. Full production source code, internal test suites, and proprietary algorithms are maintained in a secure private repository.*

---

## 📌 Executive Summary

**Category**: Application Security & Web Defense  
**Tech Stack**: `Python 3.10+ · HTTP Protocol · Web Security Standards · OWASP Secure Headers`  

Defensive HTTP auditor evaluating web server responses for security headers, TLS configuration, and information-disclosure vulnerabilities.

---

## 🎯 The Problem It Solves

Missing HTTP security headers leave web applications vulnerable to Clickjacking, Cross-Site Scripting (XSS), and MIME-sniffing attacks. Server disclosure headers leak technical stack versions to attackers.

---

## ⚙️ How the Engine Works

1. **HTTP Response Parsing**: Analyzes HTTP response header dictionaries from web application endpoints.
2. **Defensive Header Verification**: Evaluates the presence, syntax, and strength of essential defensive headers:
   - `Content-Security-Policy` (CSP): Validates policy directives, flagging `unsafe-inline` or missing object restrictions
   - `Strict-Transport-Security` (HSTS): Checks `max-age` duration and `includeSubDomains` directives
   - `X-Frame-Options` / `frame-ancestors`: Verifies protection against clickjacking
   - `X-Content-Type-Options`: Enforces `nosniff`
   - `Referrer-Policy`: Verifies sensitive URL query parameter privacy
3. **Information Disclosure Detection**: Flags verbose server headers (`Server`, `X-Powered-By`, `X-AspNet-Version`) that leak underlying technology stacks and version numbers.
4. **Grade Calculation**: Assigns an overall security grade (A+ through F) with exact configuration fixes.

---

## 🚀 Key Capabilities

- Audits CSP, HSTS, X-Frame-Options, and defensive header configurations
- Detects technology stack information disclosure headers
- Computes standardized web security posture grades
- Generates copy-paste Nginx / Apache / Cloudflare header configurations

---

## 🏗️ System Data Flow & Architecture

```
+-----------------------------------+
|  Target Input / Configuration    |
|  (JSON Snapshots / Policies)      |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  1. Schema Normalization Engine   |
|  Validates types & formats        |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  2. Core Analytical Pipeline      |
|  Heuristic rule evaluation,       |
|  invariant checks & drift diffs   |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  3. Risk Classification           |
|  Assigns severity: INFO / HIGH    |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  4. Structured Findings & Report  |
|  Root cause, evidence &           |
|  actionable remediation steps     |
+-----------------------------------+
```

---

## 📄 Findings Output Structure

The engine generates structured, machine-parsable JSON reports adhering to this standard audit schema:

```json
{
  "results": [
    {
      "resource": "resource-identifier",
      "severity": "HIGH",
      "check": "CHECK_IDENTIFIER",
      "detail": "Descriptive analysis of the identified security posture issue.",
      "remediation": "Actionable step-by-step guidance to restore compliant state.",
      "evidence": {
        "observed_field": "value",
        "required_policy": "enforced_policy"
      }
    }
  ],
  "count": 1,
  "scope": "Comprehensive defensive security audit"
}
```

---

## 🔒 Source Code & Enterprise Inquiries

To protect proprietary intellectual property and client operational security:
* **Public Repository**: Contains comprehensive architecture specifications, schemas, and design overviews.
* **Private Repository**: Contains the complete production implementation, continuous integration pipelines, and full regression test suites.

For architectural questions or enterprise inquiries, connect via [LinkedIn](https://www.linkedin.com/in/karthikeyansubramaniam04/) or visit the [Portfolio Site](https://karthikeyansubramaniyam.github.io).
