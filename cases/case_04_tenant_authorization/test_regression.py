from .fixed import can_read


RESOURCE = {"id": "invoice-7", "tenant_id": "tenant-a"}


def test_same_tenant_member_is_allowed():
    assert can_read({"role": "member", "tenant_id": "tenant-a"}, RESOURCE) is True


def test_cross_tenant_admin_is_denied():
    assert can_read({"role": "admin", "tenant_id": "tenant-b"}, RESOURCE) is False


def test_missing_scope_is_denied():
    assert can_read({"role": "admin"}, RESOURCE) is False
