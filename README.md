# fastapi_ham-api

This project is just something to work on for a more modern amateur radio record lookup.

## Project Setup

### Virtual Environment

```bash
python -m venv .venv

source .venv/bin/active # linux
# or
.\.venv\Scripts\Activate.ps1 # windows powershell

pip install -r requirements.txt
```

### Environment Variables

The API is looking for the `.env` file in the root directory. Variables to define are:

- `PROJ_URL` : This URL is sent out in the notification emails, it should match your local or public DNS name, including URI and port if needed.
- `MONGO_URL` : URI for MongoDB, use part after `@` in Connection String
- `MONGO_USERNAME` : User name to MongoDB
- `MONGO_PASSWORD` : User password to MongoDB
- `AUTHJWT_SECRET` : Used to create JWT tokens
- `SALT` : Used in password hashing
- `MAIL_APIKEY` : API Key from Mailtrap.io
- `MAIL_CONSOLE` : Enable sending email / 0 for False, 1 for True. If **False**, outputs link and token to console.

## Register/Login Steps

1. `/v1/auth/register` to register your account
2. `/v1/auth/verify` to request verification link
3. `/v1/auth/verify/{token}` to verify account
4. `/v1/auth/login` to login and get `access_token`

## References

- [GitHub : devdupont/fastapi-beanie-jwt](https://github.com/devdupont/fastapi-beanie-jwt)
  - Used as a baseline for integrating JWT into my project.