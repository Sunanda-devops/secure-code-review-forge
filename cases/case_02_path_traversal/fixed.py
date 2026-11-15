"""Constrained artifact paths that cannot escape the storage root."""

from pathlib import Path


def artifact_path(root: str, user_name: str) -> Path:
    if not user_name or "\x00" in user_name:
        raise ValueError("invalid artifact name")
    base = Path(root).resolve()
    candidate = (base / user_name).resolve()
    try:
        candidate.relative_to(base)
    except ValueError as exc:
        raise ValueError("artifact path escapes storage root") from exc
    return candidate
