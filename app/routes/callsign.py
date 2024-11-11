"""app/routes/callsign.py.

API Router for Callsigns.
"""

from fastapi import APIRouter

router = APIRouter(prefix='/callsign', tags=['callsign'])

@router.get('/{callsign}')
async def get_callsign_index(callsign: str):
    return [{'callsign': callsign}]
