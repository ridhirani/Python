#iterate over dates
#sometimes we need to iterate through dates over a range of dates from 
# start to end date 
import datetime
day_delta= datetime.timedelta(days=1)
start_date=datetime.date.today()
end_date=start_date + 7 * day_delta
for i in range ((end_date - start_date).days):
    print(start_date + i*day_delta)