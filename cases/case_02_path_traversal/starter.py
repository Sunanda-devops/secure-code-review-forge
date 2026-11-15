"""Intentionally unsafe: joining does not confine the resolved path."""

from pathlib import Path


def artifact_path(root: str, user_name: str) -> Path:
    return Path(root) / user_name
