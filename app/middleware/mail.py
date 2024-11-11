"""Mail server config."""

from os import environ as ENV, getenv
from fastapi_mail import FastMail, ConnectionConfig, MessageSchema, MessageType

mail_conf = ConnectionConfig(
    MAIL_USERNAME=ENV.get('MAIL_USERNAME'),
    MAIL_PASSWORD=ENV.get('MAIL_PASSWORD'),
    MAIL_FROM=ENV.get('MAIL_FROM'),
    MAIL_PORT=ENV.get('MAIL_PORT'),
    MAIL_SERVER=ENV.get('MAIL_SERVER'),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
)

mail = FastMail(mail_conf)


async def send_verification_email(email: str, token: str) -> None:
    """Send user verification email."""
    # Change this later to public endpoint
    url = ENV.get('PROJ_URL') + "/v1/auth/verify/" + token
    print(ENV.get('MAIL_CONSOLE'))
    if getenv('MAIL_CONSOLE', 'False'):
        print("POST to " + url)
    else:
        message = MessageSchema(
            recipients=[email],
            subject="Ham API Email Verification",
            body=f"Welcome to Ham API! We just need to verify your email to begin: {url}",
            subtype=MessageType.plain,
        )
        await mail.send_message(message)


async def send_password_reset_email(email: str, token: str) -> None:
    """Send password reset email."""
    # Change this later to public endpoint
    url = ENV.get('PROJ_URL') + "/v1/auth/reset-password/" + token
    if getenv('MAIL_CONSOLE', 'False'):
        print("POST to " + url)
    else:
        message = MessageSchema(
            recipients=[email],
            subject="Ham API Password Reset",
            body=f"Click the link to reset your Ham API account password: {url}\nIf you did not request this, please ignore this email",
            subtype=MessageType.plain,
        )
        await mail.send_message(message)
