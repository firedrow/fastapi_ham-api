# fastapi_ham-api

This project is just something to work on for a more modern amateur radio record lookup.

## Plans

- FastAPI
- MongoDB ~~or SQL?~~
- Download FCC callsign data nightly
  - Parse and put in database, if doesn't exist
- REST API
  - /v1
    - /auth
      - ~~POST /login~~
      - ~~POST /register~~
        - ~~needs approval process~~
        - add roles: admin, repeater owner, repeater council (limited to state or specific areas)
        - ~~GET calls are public~~
        - ~~POST requires registration approval~~
        - PUT only by admin or original POSTer
        - DELETE only by admin or original POSTer
    - /callsign
      - GET /
    - /repeaters
      - ~~GET /~~
      - ~~POST /~~
      - ~~PUT /:id~~
      - ~~DELETE /:id~~
      - ~~GET /:country~~
      - ~~GET /:country/:state~~
      - ~~GET /:country/:state/:county~~
      - ~~GET /:maidenhead~~
    - /location
      - something with maidenhead lookups, gps to maidenhead, maidenhead to gps, maidenhead to maidenhead distances
- Models
  - repeaters, add sub-document/model for DMR/D-STAR/X-WIRES/etc, different nested information (tones?)
  - callsign based off FCC info

### ToDo

- [ ] Only owner or admin can delete
- [ ] Only owner or admin can update
- [ ] Need to set owner on POST of repeaters
- [ ] Add more features on repeaters
  - [ ] DMR
  - [ ] D-STAR
  - [ ] YSF
  - [ ] M17
  - [ ] IRLP
  - [ ] Echolink
  - [ ] AllStar
  - [ ] ATV
  - [ ] NXDN
  - [ ] P-25
  - [ ] WIRES
- [ ] https://mailtrap.io/pricing/ for smtp relay
  - [ ] Fix MAIL_CONSOLE = False issue in middleware/mail.py

## Register/Login Steps

1. `/v1/auth/register` to register your account
2. `/v1/auth/verify` to request verification link
3. `/v1/auth/verify/{token}` to verify account
4. `/v1/auth/login` to login and get `access_token`

## References

- https://github.com/devdupont/fastapi-beanie-jwt
- https://github.com/fastapi-users/fastapi-users-db-beanie
  - https://fastapi-users.github.io/fastapi-users/10.1/configuration/full-example/
  - https://fastapi-users.github.io/fastapi-users/latest/configuration/databases/beanie/