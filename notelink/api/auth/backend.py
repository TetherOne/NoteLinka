from fastapi_users.authentication import AuthenticationBackend

from notelink.api.auth.dependencies import get_database_strategy
from notelink.core.authentication.transport import bearer_transport


authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
