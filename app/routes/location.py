"""app/routes/location.py.

API Router for Locations.
"""

from fastapi import APIRouter

router = APIRouter(prefix='/location', tags=['location'])

@router.get('/')
async def get_location_index():
    return [{'foo': 'bar'}]
