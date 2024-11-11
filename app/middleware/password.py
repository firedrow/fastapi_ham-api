"""Password utility functions."""

from os import environ as ENV
import bcrypt


def hash_password(password: str) -> str:
    """Return a salted password hash."""
    return bcrypt.hashpw(password.encode(), ENV.get('SALT').encode()).decode()
