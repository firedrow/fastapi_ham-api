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
      - POST /login
      - POST /register
        - needs approval process
        - add roles: admin, repeater owner, repeater council (limited to state or specific areas)
        - GET calls are public
        - POST requires registration approval
        - PUT only by admin or original POSTer
        - DELETE only by admin or original POSTer
    - /callsign
      - GET /
    - /repeaters
      - GET /
      - POST /
      - PUT /:id
      - DELETE /:id
      - GET /:country
      - GET /:country/:state
      - GET /:country/:state/:county
      - GET /:maidenhead
    - /location
      - something with maidenhead lookups, gps to maidenhead, maidenhead to gps, maidenhead to maidenhead distances
- Models
  - repeaters, add sub-document/model for DMR/D-STAR/X-WIRES/etc, different nested information (tones?)
  - callsign based off FCC info
