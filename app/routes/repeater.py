"""app/routes/repeater.py.

API Router for Repeaters.
"""

from typing import List
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from app.models.repeater import Repeaters, RepeatersCreate, RepeatersUpdate

router = APIRouter(prefix='/repeater', tags=['repeater'])

@router.get('/', response_model=List[Repeaters])
async def get_repeater():
    repeaters = await Repeaters.find().to_list()

    if not repeaters:
        raise HTTPException(status_code=404, detail='no repeaters found.')

    return repeaters


@router.post('/', response_model=Repeaters)
async def create_repeater(repeater_data: RepeatersCreate):
    new_repeater = Repeaters(
        name = repeater_data.name,
        status = repeater_data.status,
        frequency_downlink = repeater_data.frequency_downlink,
        frequency_uplink = repeater_data.frequency_uplink,
        frequency_offset = repeater_data.frequency_offset,
        band = repeater_data.band,
        bandwidth = repeater_data.bandwidth,
        country = repeater_data.country.lower(),
        state = repeater_data.state.lower(),
        grid = repeater_data.grid.lower(),
        sponsor = repeater_data.sponsor,
        coordination = repeater_data.coordination
    )

    if repeater_data.county:
        new_repeater.county = repeater_data.county.lower()
    if repeater_data.nets:
        new_repeater.nets = repeater_data.nets
    if repeater_data.latitude:
        new_repeater.latitude = repeater_data.latitude
    if repeater_data.longitude:
        new_repeater.longitude = repeater_data.longitude
    if repeater_data.ctone_downlink:
        new_repeater.ctone_downlink = repeater_data.ctone_downlink
    if repeater_data.ctone_uplink:
        new_repeater.ctone_uplink = repeater_data.ctone_uplink
    if repeater_data.dtone_downlink:
        new_repeater.dtone_downlink = repeater_data.dtone_downlink
    if repeater_data.dtone_uplink:
        new_repeater.dtone_uplink = repeater_data.dtone_uplink

    await new_repeater.insert()
    return new_repeater


@router.put('/{repeater_id}', response_model=Repeaters)
async def update_repeater(repeater_id: PydanticObjectId, repeater_data: RepeatersUpdate):
    repeater = await Repeaters.get(repeater_id)

    if not repeater:
        raise HTTPException(status_code=404, detail='repeater not found.')

    if repeater_data.name is not None:
        repeater.name = repeater_data.name
    if repeater_data.status is not None:
        repeater.status = repeater_data.status
    if repeater_data.frequency_downlink is not None:
        repeater.frequency_downlink = repeater_data.frequency_downlink
    if repeater_data.frequency_uplink is not None:
        repeater.frequency_uplink = repeater_data.frequency_uplink
    if repeater_data.frequency_offset is not None:
        repeater.frequency_offset = repeater_data.frequency_offset
    if repeater_data.band is not None:
        repeater.band = repeater_data.band
    if repeater_data.bandwidth is not None:
        repeater.bandwidth = repeater_data.bandwidth
    if repeater_data.country is not None:
        repeater.country = repeater_data.country.lower()
    if repeater_data.state is not None:
        repeater.state = repeater_data.state.lower()
    if repeater_data.grid is not None:
        repeater.grid = repeater_data.grid.lower()
    if repeater_data.sponsor  is not None:
        repeater.sponsor = repeater_data.sponsor
    if repeater_data.coordination is not None:
        repeater.coordination = repeater_data.coordination
    if repeater_data.county is not None:
        repeater.county = repeater_data.county.lower()
    if repeater_data.nets is not None:
        repeater.nets = repeater_data.nets
    if repeater_data.latitude is not None:
        repeater.latitude = repeater_data.latitude
    if repeater_data.longitude is not None:
        repeater.longitude = repeater_data.longitude
    if repeater_data.ctone_downlink is not None:
        repeater.ctone_downlink = repeater_data.ctone_downlink
    if repeater_data.ctone_uplink is not None:
        repeater.ctone_uplink = repeater_data.ctone_uplink
    if repeater_data.dtone_downlink is not None:
        repeater.dtone_downlink = repeater_data.dtone_downlink
    if repeater_data.dtone_uplink is not None:
        repeater.dtone_uplink = repeater_data.dtone_uplink

    await repeater.save()
    return repeater


@router.delete('/{repeater_id}')
async def delete_repeater(repeater_id: PydanticObjectId):
    repeater = await Repeaters.get(repeater_id)

    if not repeater:
        raise HTTPException(status_code=404, detail='repeater not found.')

    await repeater.delete()
    return {"message": f"Repeater {repeater_id} has been deleted."}


@router.get('/grid/{maidenhead}', response_model=List[Repeaters])
async def get_repeater_maidenhead(maidenhead: str):
    repeaters = await Repeaters.find({'grid': maidenhead}).to_list()

    if not repeaters:
        raise HTTPException(status_code=404, detail='no repeaters found.')

    return repeaters


@router.get('/{country}', response_model=List[Repeaters])
async def get_repeater_country(country: str):
    repeaters = await Repeaters.find({'country': country}).to_list()

    if not repeaters:
        raise HTTPException(status_code=404, detail='no repeaters found.')

    return repeaters


@router.get('/{country}/{state}', response_model=List[Repeaters])
async def get_repeater_state(country: str, state: str):
    repeaters = await Repeaters.find({'country': country,
                                      'state': state}).to_list()

    if not repeaters:
        raise HTTPException(status_code=404, detail='no repeaters found.')

    return repeaters


@router.get('/{country}/{state}/{county}', response_model=List[Repeaters])
async def get_repeater_county(country: str, state: str, county: str):
    repeaters = await Repeaters.find({'country': country,
                                      'state': state,
                                      'county': county}).to_list()

    if not repeaters:
        raise HTTPException(status_code=404, detail='no repeaters found.')

    return repeaters
