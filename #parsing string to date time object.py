#parsing string to date time object
from datetime import datetime
datetime_string='Oct 1 2022, 00:00:00'
datetime_string_format='%b %d %Y, %H:%M:%S'
print(datetime.strptime(datetime_string, datetime_string_format))