"""Intentionally unsafe: check-then-add is not atomic across workers."""


def accept_event(seen: set[str], event_id: str) -> bool:
    if event_id in seen:
        return False
    seen.add(event_id)
    return True
