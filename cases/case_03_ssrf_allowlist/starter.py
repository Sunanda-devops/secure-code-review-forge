"""Intentionally unsafe: prefix matching is not host validation."""


def allowed_callback(url: str, allowed_prefix: str) -> bool:
    return url.startswith(allowed_prefix)
