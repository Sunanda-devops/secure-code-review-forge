"""Strict callback validation for an exact allowlisted HTTPS host."""

from urllib.parse import urlparse


def allowed_callback(url: str, allowed_hosts: set[str]) -> bool:
    parsed = urlparse(url)
    return (
        parsed.scheme == "https"
        and parsed.hostname is not None
        and parsed.hostname.lower() in {host.lower() for host in allowed_hosts}
        and parsed.username is None
        and parsed.password is None
        and parsed.port in (None, 443)
    )
