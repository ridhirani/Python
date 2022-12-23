#date formatting
from datetime import datetime
a=datetime(2021, 3, 23, 0, 0, 0)
b=datetime(2022, 3, 23, 23, 59, 59)
print(a-b)
print((a-b).days)
print((a-b).total_seconds())