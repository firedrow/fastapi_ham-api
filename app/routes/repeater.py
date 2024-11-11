"""app/routes/repeater.py.

API Router for Repeaters.
"""

from fastapi import APIRouter

router = APIRouter(prefix='/repeater', tags=['repeater'])

@router.get('/')
async def get_repeater():
    return [{'foo': 'bar'}]

@router.post('/')
async def create_repeater():
    return [{'foo': 'bar'}]

@router.put('/{repeater_id}')
async def update_repeater(repeater_id: str):
    return [{'foo': 'bar'}]

@router.delete('/{repeater_id}')
async def delete_repeater(repeater_id: str):
    return [{'foo': 'bar'}]

@router.get('/maidenhead/{maidenhead}')
async def get_repeater_maidenhead(maidenhead: str):
    return [{'maidenhead': maidenhead}]

@router.get('/{country}')
async def get_repeater_country(country: str):
    return [{'country': country}]

@router.get('/{country}/{state}')
async def get_repeater_state(country: str, state: str):
    return [{
                'country': country,
                'state': state
            }]

@router.get('/{country}/{state}/{county}')
async def get_repeater_county(country: str, state: str, county: str):
    return [{
                'country': country,
                'state': state,
                'county': county
            }]
