"""app/models/users.py.

MongoDB model for the users collection.
"""

from datetime import datetime
from typing import Annotated, Any, Optional
from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr


class UserAuth(BaseModel):
    """User register and login auth."""

    email: EmailStr
    password: str


class User(Document):
    """Beanie Document for the users collection."""
    class Settings:
        """Set the MongoDB Collection name."""
        name = "users"

    email: Indexed(EmailStr, unique=True)
    password: str
    email_confirmed_at: datetime | None = None
    role: str = 'user'
    disabled: bool = False

    @property
    def created(self) -> datetime | None:
        """Datetime user was created from ID."""
        return self.id.generation_time if self.id else None

    @property
    def jwt_subject(self) -> dict[str, Any]:
        """JWT subject fields."""
        return {"username": self.email}

    @classmethod
    async def by_email(cls, email: str) -> Optional["User"]:
        """Get a user by email."""
        return await cls.find_one(cls.email == email)

    def update_email(self, new_email: str) -> None:
        """Update email logging and replace."""
        # Add any pre-checks here
        self.email = new_email


class UserCreate(Document):
    """Beanie Document for the users collection."""
    class Settings:
        """Set the MongoDB Collection name."""
        name = "users"

    email: Indexed(EmailStr, unique=True)
    password: str
    email_confirmed_at: datetime | None = None
    role: str = 'user'
    disabled: bool = False

    @property
    def created(self) -> datetime | None:
        """Datetime user was created from ID."""
        return self.id.generation_time if self.id else None

    @property
    def jwt_subject(self) -> dict[str, Any]:
        """JWT subject fields."""
        return {"username": self.email}

    @classmethod
    async def by_email(cls, email: str) -> Optional["User"]:
        """Get a user by email."""
        return await cls.find_one(cls.email == email)

    def update_email(self, new_email: str) -> None:
        """Update email logging and replace."""
        # Add any pre-checks here
        self.email = new_email


class UserUpdate(Document):
    """Updatable user fields."""

    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserOut(UserUpdate):
    """User fields returned to the client."""

    email: Annotated[str, Indexed(EmailStr, unique=True)]
    disabled: bool = False
