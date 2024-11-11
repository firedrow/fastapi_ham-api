"""app/__init__.py.

FastAPI application initializer.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    title='Ham API',
    description=app_description,
    summary='Core API system.',
    contact={
        'name': 'Ham API Team',
        'email': 'me@kf0mlb.xyz',
        'url': 'https://ham-api.kf0mlb.xyz'
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
