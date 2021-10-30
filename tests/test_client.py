import pytest
from aiohttp.client import ClientSession

from pixii.client import client


@pytest.mark.asyncio
async def test_client():
    """
    Temp test for project init
    """
    async with client() as c:
        assert isinstance(c, ClientSession)
