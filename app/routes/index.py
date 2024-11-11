"""app/routes/index.py.

Main API Router.
"""

from fastapi import APIRouter
from app.routes import auth, callsign, location, repeater

router = APIRouter(prefix='/v1')
router.include_router(auth.router)
router.include_router(callsign.router)
router.include_router(location.router)
router.include_router(repeater.router)
