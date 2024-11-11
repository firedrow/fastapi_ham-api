"""app/routes/auth.py.

API Router for Authentication and Registration.
"""

from datetime import datetime, UTC
from fastapi import APIRouter, Body, Response, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials
from pydantic import EmailStr
from app.models.auth import AccessToken, RefreshToken
from app.models.users import User, UserAuth, UserOut, UserCreate
from app.middleware.mail import send_password_reset_email, send_verification_email
from app.middleware.jwt import access_security, refresh_security, user_from_token
from app.middleware.password import hash_password

router = APIRouter(prefix='/auth', tags=['auth'])

embed = Body(..., embed=True)


@router.post("/login")
async def login(user_auth: UserAuth) -> RefreshToken:
    """Authenticate and returns the user's JWT."""
    user = await User.by_email(user_auth.email)
    if user is None or hash_password(user_auth.password) != user.password:
        raise HTTPException(status_code=401, detail="Bad email or password")
    if user.email_confirmed_at is None:
        raise HTTPException(status_code=400, detail="Email is not yet verified")
    access_token = access_security.create_access_token(user.jwt_subject)
    refresh_token = refresh_security.create_refresh_token(user.jwt_subject)
    return RefreshToken(access_token=access_token, refresh_token=refresh_token)


@router.post("/refresh")
async def refresh(
    auth: JwtAuthorizationCredentials = Security(refresh_security)
) -> AccessToken:
    """Return a new access token from a refresh token."""
    access_token = access_security.create_access_token(subject=auth.subject)
    return AccessToken(access_token=access_token)


@router.post("/register", response_model=UserCreate)
async def user_registration(user_auth: UserAuth):  # type: ignore[no-untyped-def]
    """Create a new user."""
    user = await User.by_email(user_auth.email)
    if user is not None:
        raise HTTPException(409, "User with that email already exists")
    hashed = hash_password(user_auth.password)
    user = User(email=user_auth.email, password=hashed)
    await user.create()
    return user


@router.post("/forgot-password")
async def forgot_password(email: EmailStr = embed) -> Response:
    """Send password reset email."""
    user = await User.by_email(email)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is not None:
        raise HTTPException(400, "Email is already verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    token = access_security.create_access_token(user.jwt_subject)
    await send_password_reset_email(email, token)
    return Response(status_code=200)


@router.post("/reset-password/{token}", response_model=UserOut)
async def reset_password(token: str, password: str = embed):  # type: ignore[no-untyped-def]
    """Reset user password from token value."""
    user = await user_from_token(token)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is None:
        raise HTTPException(400, "Email is not yet verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    user.password = hash_password(password)
    await user.save()
    return user


@router.post("/verify")
async def request_verification_email(
    email: EmailStr = Body(..., embed=True)
) -> Response:
    """Send the user a verification email."""
    user = await User.by_email(email)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is not None:
        raise HTTPException(400, "Email is already verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    token = access_security.create_access_token(user.jwt_subject)
    await send_verification_email(email, token)
    return Response(status_code=200)


@router.post("/verify/{token}")
async def verify_email(token: str) -> Response:
    """Verify the user's email with the supplied token."""
    user = await user_from_token(token)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is not None:
        raise HTTPException(400, "Email is already verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    user.email_confirmed_at = datetime.now(tz=UTC)
    await user.save()
    return Response(status_code=200)
