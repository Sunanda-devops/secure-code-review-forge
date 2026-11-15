"""Tenant-aware authorization policy for resource reads."""


def can_read(user: dict, resource: dict) -> bool:
    role = user.get("role")
    tenant_id = user.get("tenant_id")
    resource_tenant_id = resource.get("tenant_id")
    if role not in {"admin", "member"}:
        return False
    if not tenant_id or not resource_tenant_id:
        return False
    return tenant_id == resource_tenant_id
