from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9))
dt=datetime(2015, 1, 1, 10, 0, 0, tzinfo=JST)
print(dt)

