#extracting date time from a text
from dateutil.parser import parse
dt=parse("Today is December 22nd, 2022 at 12:23:00AM",fuzzy=True)
print(dt)