"""app/middleware/jwt.py.

FastAPI JWT configuration.
"""

from datetime import timedelta
from os import environ as ENV
from fastapi import HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer, JwtRefreshBearer
from app.models.users import User

ACCESS_EXPIRES = timedelta(minutes=15)
REFRESH_EXPIRES = timedelta(days=30)

access_security = JwtAccessBearer(
    ENV.get('AUTHJWT_SECRET'),
    access_expires_delta=ACCESS_EXPIRES,
    refresh_expires_delta=REFRESH_EXPIRES,
)

refresh_security = JwtRefreshBearer(
    ENV.get('AUTHJWT_SECRET'),
    access_expires_delta=ACCESS_EXPIRES,
    refresh_expires_delta=REFRESH_EXPIRES,
)


async def user_from_credentials(auth: JwtAuthorizationCredentials) -> User | None:
    """Return the user associated with auth credentials."""
    return await User.by_email(auth.subject["username"])


async def user_from_token(token: str) -> User | None:
    """Return the user associated with a token value."""
    # Check if jwt_backend exists and use it to decode the token
    try:
        payload = access_security.jwt_backend.decode(token, access_security.secret_key)
    except Exception as e:
        raise HTTPException(401, "Token is invalid or expired") from e

    # Extract the email or user information from the payload as needed
    username = payload.get("subject", {}).get("username")
    if username is None:
        raise HTTPException(401, "Invalid token payload")

    return await User.by_email(username)


async def current_user(
    auth: JwtAuthorizationCredentials = Security(access_security)
) -> User:
    """Return the current authorized user."""
    if not auth:
        raise HTTPException(401, "No authorization credentials found")
    user = await user_from_credentials(auth)
    if user is None:
        raise HTTPException(404, "Authorized user could not be found")
    return user
