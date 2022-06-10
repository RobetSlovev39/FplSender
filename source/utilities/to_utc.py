from datetime import datetime, timedelta

difference = timedelta(
  hours=(now := datetime.now()).hour - (utc := datetime.utcnow()).hour,
  minutes=now.minute - utc.minute
)


def to_utc(date: datetime) -> datetime:
  return date + difference
