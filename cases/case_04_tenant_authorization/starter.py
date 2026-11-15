"""Intentionally unsafe: role checks do not establish tenant ownership."""


def can_read(user: dict, resource: dict) -> bool:
    return user.get("role") in {"admin", "member"}
