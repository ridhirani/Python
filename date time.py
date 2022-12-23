#to convert the date time format
import datetime
dt = datetime.datetime.strptime(
    "22/12/22 09:23",
    "%d/%m/%y %H:%M"
     )
print(dt)

#to get the date time of real time
dt1=datetime.datetime.now()
print(dt1)

dt2=dt1.strftime(
    "%a %m %y"
)
print(dt2)