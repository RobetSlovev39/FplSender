from .get_data import get_data
from datetime import datetime, timedelta, time


async def get_text(text: str, dep_time: time, alt: str, radius: str, lat: float, lng: float) -> str:
  data = await get_data(lat, lng)

  civil_twilight_begin = data['results']['civil_twilight_begin']
  civil_twilight_begin = datetime.strptime(civil_twilight_begin, '%I:%M:%S %p').time()
  dep_time = civil_twilight_begin if civil_twilight_begin > dep_time else dep_time

  civil_twilight_end = data['results']['civil_twilight_end']
  civil_twilight_end = datetime.strptime(civil_twilight_end, '%I:%M:%S %p').time()

  civil_twilight_end_minutes = civil_twilight_end.hour * 60 + civil_twilight_end.minute
  dep_time_minutes = dep_time.hour * 60 + dep_time.minute

  endur_minutes = civil_twilight_end_minutes - dep_time_minutes
  endur_hours = endur_minutes // 60
  endur = time(hour=endur_hours, minute=endur_minutes - endur_hours * 60)

  dof = datetime.now() + timedelta(days=1)

  return text.format(
    dep_time=dep_time.strftime('%H%M'),
    alt=alt,
    radius=radius,
    endur=endur.strftime('%H%M'),
    dof=dof.strftime('%y%m%d')
  )
