# Callback URL validation

**Risk:** High. Server-side callbacks can become SSRF when an allowlist is implemented as a URL prefix check.

**Audit question:** Does validation inspect the parsed scheme, hostname, credentials, and port rather than comparing raw strings?

**Failure pattern:** `starter.py` accepts any URL beginning with the configured prefix. An attacker can use a deceptive hostname such as `hooks.example.com.evil.test` or userinfo syntax.

**Fix:** `fixed.py` parses the URL, requires HTTPS, rejects credentials, permits only the default HTTPS port, and compares the normalized hostname against an exact allowlist.

**Regression evidence:** Trusted URLs pass; lookalike subdomains, HTTP, userinfo, alternate ports, and arbitrary hosts fail.
