"""app/__init__.py.

FastAPI application initializer.
"""

from os import environ as ENV
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_analytics.fastapi import Analytics

from app.dependencies import app_lifespan

cors_origins = [
    'http://localhost',
    'http://localhost:8000'
]

app_description = '''
This project is using Python + [FastAPI](https://fastapi.tiangolo.com/) to build a REST API for interaction with
Ham Radio Operators. Via the [Beanie](https://roman-right.github.io/beanie/) library, we can interface
with our MongoDB database.
'''

app = FastAPI(
    title=ENV.get('PROJ_SITE_NAME'),
    description=app_description,
    summary='Core API system.',
    contact={
        'name': ENV.get('PROJ_TEAM_NAME'),
        'email': ENV.get('PROJ_EMAIL'),
        'url': ENV.get('PROJ_URL')
    },
    lifespan=app_lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

analytics_send = ENV.get('ANALYTICS_ENABLE')
if analytics_send == '0':
    analytics_send = False
if analytics_send == '1':
    analytics_send = True

if analytics_send:
    app.add_middleware(
        Analytics,
        api_key=ENV.get('ANALYTICS_APIKEY')
    )
else:
    print('API Analytics disabled.')
