# Concurrent idempotency gate

**Risk:** High. A duplicate event can trigger a second side effect when two workers observe the same missing key before either records it.

**Audit question:** Is the check-and-record operation atomic under concurrent delivery?

**Failure pattern:** `starter.py` performs a membership check followed by an insertion with no critical section. The code looks correct in a sequential test but does not establish the invariant under concurrent replay.

**Fix:** `fixed.py` uses a lock around the complete check-and-record section and rejects empty identifiers. A multi-process deployment should replace the in-memory set with a database uniqueness constraint or an atomic cache operation.

**Regression evidence:** 256 concurrent deliveries of the same event produce exactly one acceptance.
