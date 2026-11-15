"""Thread-safe idempotency gate for a single process."""

from threading import Lock


class IdempotencyGate:
    def __init__(self) -> None:
        self._seen: set[str] = set()
        self._lock = Lock()

    def accept(self, event_id: str) -> bool:
        if not event_id:
            raise ValueError("event_id is required")
        with self._lock:
            if event_id in self._seen:
                return False
            self._seen.add(event_id)
            return True
