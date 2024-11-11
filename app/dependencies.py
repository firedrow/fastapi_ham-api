"""app/dependencies.py.

FastAPI Dependency Injection; anything used with the `Depends` keyword.  Shared
logic, database connections, enforced security, etc.
"""

import logging
from os import environ as ENV
from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.routes import index

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    """FastAPI Lifespan Events.

    Code above the `yield` will be executed on Start-up.
    Code below the `yield` will be executed on Shutdown.

    URL: [FastAPI Lifespan Events](https://fastapi.tiangolo.com/advanced/events/#lifespan-function)
    """
    # app start-up
    logging.info('Starting Ham API app...')
    mongo_user = ENV.get('MONGO_USERNAME') # pulled from .env file for Environment Variables
    mongo_pass = ENV.get('MONGO_PASSWORD') # pulled from .env file for Environment Variables
    mongo_url = ENV.get('MONGO_URL')       # pulled from .env file for Environment Variables
    #client = AsyncIOMotorClient(host=f'mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_url}')
    #db = client['hamapi'] # which MongoDB is being used

    logging.info(f'Connecting to MongoDB @ {mongo_url}...')
    #await init_beanie(database=db,
    #                  document_models=[
    #                      # Make sure the last string is the Class name.
                          #'app.models.blog.posts.Posts',
    #                  ])
    logging.info('Database connected and Beanie models initialized.')

    logging.info('Building app routes...')
    app.include_router(index.router)

    yield
    # app shutdown
    logging.info('Closing connection to MongoDB...')
    #client.close()

    logging.info('Shutting down Ham API app...')
