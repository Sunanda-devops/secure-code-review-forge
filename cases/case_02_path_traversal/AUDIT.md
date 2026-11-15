# Storage-root containment

**Risk:** Critical. A download or export endpoint that joins a storage root with untrusted input can expose configuration, source, or credential files.

**Audit question:** Does the final resolved path remain inside the intended root, including symlink and `..` cases?

**Failure pattern:** `starter.py` returns `Path(root) / user_name` without resolving or checking containment.

**Fix:** `fixed.py` resolves both the base and candidate, then requires the candidate to be relative to the base. Null bytes and empty names are rejected before filesystem use.

**Regression evidence:** Safe nested paths are accepted; traversal, nested traversal, and null-byte payloads raise `ValueError`.
