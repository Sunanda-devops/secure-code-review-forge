import pytest

from .fixed import allowed_callback


@pytest.mark.parametrize(
    "url",
    [
        "https://hooks.example.com/events",
        "https://HOOKS.EXAMPLE.COM/events",
    ],
)
def test_exact_allowlisted_https_host_is_accepted(url):
    assert allowed_callback(url, {"hooks.example.com"}) is True


@pytest.mark.parametrize(
    "url",
    [
        "https://hooks.example.com.evil.test/events",
        "http://hooks.example.com/events",
        "https://hooks.example.com@evil.test/events",
        "https://evil.test/events",
        "https://hooks.example.com:8443/events",
    ],
)
def test_confusing_or_untrusted_urls_are_rejected(url):
    assert allowed_callback(url, {"hooks.example.com"}) is False
