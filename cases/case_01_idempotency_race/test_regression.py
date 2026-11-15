from concurrent.futures import ThreadPoolExecutor

from .fixed import IdempotencyGate


def test_duplicate_event_is_accepted_once_under_concurrency():
    gate = IdempotencyGate()
    with ThreadPoolExecutor(max_workers=64) as pool:
        results = list(pool.map(gate.accept, ["evt-42"] * 256))
    assert sum(results) == 1


def test_event_id_is_required():
    gate = IdempotencyGate()
    try:
        gate.accept("")
    except ValueError:
        pass
    else:
        raise AssertionError("empty event IDs must be rejected")
