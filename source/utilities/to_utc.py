from datetime import datetime, timedelta

utc = datetime.utcnow()
now = datetime.now()

difference = timedelta(hours=now.hour - utc.hour, minutes=now.minute - utc.minute)


def to_utc(date: datetime) -> datetime:
  return date + difference
