"""Mail server config."""

from os import environ as ENV
import mailtrap as mt

# Getting bool from .env is seen as a string
mail_console = ENV.get('MAIL_CONSOLE')
if mail_console == '0':
    mail_console = False
if mail_console == '1':
    mail_console = True

async def send_verification_email(email: str, token: str) -> None:
    """Send user verification email."""
    # Change this later to public endpoint
    url = ENV.get('PROJ_URL') + "/v1/auth/verify/" + token
    if mail_console:
        print("POST to " + url)
    else:
        mail = mt.Mail(
            sender=mt.Address(email='noreply@ham-api.kf0mlb.xyz', name='Ham API No-Reply'),
            to=[mt.Address(email=email)],
            subject='Ham API Email Verification',
            text=f'Welcome to Ham API! We just need to verify your email to begin: {url}'
        )
        client = mt.MailtrapClient(token=ENV.get('MAIL_APIKEY'))
        client.send(mail)


async def send_password_reset_email(email: str, token: str) -> None:
    """Send password reset email."""
    # Change this later to public endpoint
    url = ENV.get('PROJ_URL') + "/v1/auth/reset-password/" + token
    if mail_console:
        print("POST to " + url)
    else:
        mail = mt.Mail(
            sender=mt.Address(email='noreply@ham-api.kf0mlb.xyz', name='Ham API No-Reply'),
            to=[mt.Address(email=email)],
            subject="Ham API Password Reset",
            text=f"Click the link to reset your Ham API account password: {url}\nIf you did not request this, please ignore this email"
        )
        client = mt.MailtrapClient(token=ENV.get('MAIL_APIKEY'))
        client.send(mail)
