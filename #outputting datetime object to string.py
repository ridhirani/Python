#outputting datetime object to string
from datetime import datetime
datetime_for_string=datetime(2023, 3, 24, 1, 0,0)
datetime_string_format='%b %d %y, %H:%M:%S'
print(datetime.strftime(datetime_for_string,datetime_string_format))