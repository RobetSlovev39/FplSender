from typing import Dict
from httpx import AsyncClient


async def get_data(lat: float, lng: float) -> Dict:
  url = 'https://api.sunrise-sunset.org/json'

  payload = {
    'lat': lat,
    'lng': lng,
    'formatted': 1
  }

  async with AsyncClient() as session:
    response = await session.get(url, params=payload)
    data = response.json()

  return data
