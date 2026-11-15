# Tenant-scoped authorization

**Risk:** Critical. Authentication and role membership do not prove that a user owns the tenant containing the requested resource.

**Audit question:** Does the authorization decision bind the caller's tenant scope to the resource scope?

**Failure pattern:** `starter.py` grants access to any authenticated member or admin, allowing an ID change to cross tenant boundaries.

**Fix:** `fixed.py` requires an approved role and an explicit, matching `tenant_id` on both the caller and the resource. Missing scope is denied by default.

**Regression evidence:** Same-tenant members pass; cross-tenant admins and users with missing scope fail.
