# Project Setup

## Virtual Environment

```bash
python -m venv .venv

source .venv/bin/activate # linux
# or
.\.venv\Scripts\Activate.ps1 # windows powershell

pip install -r requirements.txt
```

## Environment Variables

The API is looking for the `.env` file in the root directory. Variables to define are:

- `PROJ_URL` : This URL is sent out in the notification emails, it should match your local or public DNS name, including URI and port if needed. This will also be used on the FastAPI docs page.
- `PROJ_EMAIL` : This email is used with the notification emails, it should be a valid email in the event you get a reply. This will also be used on the FastAPI docs page.
- `PROJ_TEAM_NAME` : The Team Name will be used as the sender on the notification emails. This will also be used on the FastAPI docs page.
- `PROJ_SITE_NAME` : The Site Name will be used on the email body of the notification emails. This will also be used on the FastAPI docs page.
- `MONGO_URL` : URI for MongoDB, use part after `@` in Connection String
- `MONGO_USERNAME` : User name to MongoDB
- `MONGO_PASSWORD` : User password to MongoDB
- `AUTHJWT_SECRET` : Used to create JWT tokens
- `SALT` : Used in password hashing
- `MAIL_ENABLE` : Enable sending email / 0 for False, 1 for True. If **False**, outputs link and token to console.
- `MAIL_APIKEY` : API Key from Mailtrap.io
- `ANALYTICS_ENABLE` : Enable sending of data to APIAnalytics.dev dashboard / 0 for False, 1 for True.
- `ANALYTICS_APIKEY` : API Key from APIAnalytics.dev

## Generate SALT hash

1. With your virtual environment loaded, open Python
2. `import bcrypt`
3. `bcrypt.gensalt()` <-- this will generate a byte string
4. Just copy the value between the single quotes into your .env file

## Generate JWT Secret

1. Go to [jwtsecret.com/generate](https://jwtsecret.com/generate)
2. Click Generate
3. Copy secret to .env file

## Generate API Analytics API Key

1. Go to [apianalytics.com/generate](https://apianalytics.com/generate)
2. Click Generate
3. Copy secret to .env file

## Get MailTrap.io API Key

1. Go to [mailtrap.io](https://mailtrap.io) and sign-up for an account
2. Fill in information about your project
   1. Use Github repo link as project/company URL
3. Go to Sending Domains and add your FQDN
4. Add the assigned DNS records to your dns
5. Verify DNS
6. You may get a secondary confirmation email from MailTrap Support about your setup, answer the questions
7. Under your verified domain in Sending Domains, go to Integration -> Transactional Stream -> Integrate
8. Change integration from SMTP to API, copy key to .env file
