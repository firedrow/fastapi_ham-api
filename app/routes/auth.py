"""app/routes/auth.py.

API Router for Authentication and Registration.
"""

from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/login')
async def make_index_login():
    return [{'foo': 'bar'}]

@router.post('/verify')
async def make_index_verify():
    return [{'foo': 'baz'}]
