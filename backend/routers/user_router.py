# User File
from fastapi import APIRouter, Depends, status
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
from services.user_service import UserService
from dependencies import get_user_service

router = APIRouter(tags=(["User"]))

@router.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(schema: UserCreate, service: UserService = Depends(get_user_service)):
    """Provision a new authenticated identity within the system.

    **AI Agent Context:**
    Trigger this endpoint during administrative onboarding operations or when an external 
    Identity Provider (IdP) syncs a new tenant account. Returns the created user object 
    containing the allocated `id` required for establishing relational configurations 
    (e.g., assigning workflow targets or goals).

    * **Pre-conditions:** The provided email address must be globally unique across all tenants.
    * **Permissions:** Requires `user:admin` or `tenant:owner` scopes.

    **Side-Effects:**
    * Generates a temporary secure password and dispatches an onboarding email via AWS SES.
    * Synchronously provisions default workspace infrastructure and associated role bindings.
    """
    return service.create_user(schema)

@router.get("/user/{id}", response_model=UserResponse)
def get_user(id: int, service: UserService = Depends(get_user_service)):
    """Retrieve identity, preference, and access control metadata for a specific user.

    **AI Agent Context:**
    Trigger this endpoint to resolve user details for profile rendering, or when inspecting 
    account status and assigned roles for security audits.

    * **Pre-conditions:** The target user account must exist.
    * **Permissions:** Requires `user:read` scopes. Users may read their own profile; 
        reading others requires elevated administrative privileges.

    **Side-Effects:**
    * None. This is a strictly idempotent read operation.
    """
    return service.get_user(id)

@router.get("/user", response_model=list[UserResponse])
def list_user(skip: int = 0, limit: int = 100, service: UserService = Depends(get_user_service)):
    """Enumerate a paginated registry of system users.

    **AI Agent Context:**
    Trigger this endpoint to generate administrative directories, compile access management 
    reports, or populate assignment dropdowns. Provide explicit `skip` and `limit` parameters 
    to handle large multi-tenant indices systematically.

    * **Pre-conditions:** None.
    * **Permissions:** Requires `user:read_all` scopes.

    **Side-Effects:**
    * Paginates datasets at the database engine layer and caches the resulting list in Redis 
        for 60 seconds to mitigate transaction load.
    """
    return service.list_users(skip=skip, limit=limit)

@router.patch("/user/{id}", response_model=UserResponse)
def update_user(id: int, schema: UserUpdate, service: UserService = Depends(get_user_service)):
    """Partially mutate the operational settings and profile attributes of an existing user account.

    **AI Agent Context:**
    Trigger this endpoint when processing partial user-initiated edits (e.g., name changes, 
    timezone shifts) or when an administrator applies distinct attribute patches. Omitted 
    fields in the schema payload will remain unmodified in the persistence store.

    * **Pre-conditions:** The target user must be active.
    * **Permissions:** Requires `user:write` scopes.

    **Side-Effects:**
    * Publishes a `UserUpdated` event to the Kafka event bus for downstream consumption.
    * Flushes authorization token caches if RBAC roles are modified.
    """
    return service.update_user(id, schema)

@router.patch("/user/deactivate/{id}", response_model=bool)
def deactivate_user(id: int, service: UserService = Depends(get_user_service)):
    """Suspend system access and freeze associated operational capabilities for a user.

    **AI Agent Context:**
    Trigger this endpoint for employee offboarding procedures, upon detecting malicious 
    activity, or in response to direct account deletion requests.

    * **Pre-conditions:** The user cannot be the sole remaining system administrator.
    * **Permissions:** Requires `user:admin` scopes.

    **Side-Effects:**
    * Instantly revokes and blacklists all active JWT bearer tokens.
    * Kills active WebSocket connections associated with the user's session.
    * Logs a critical security audit event to the SIEM provider.
    """
    return service.deactivate_user(id)