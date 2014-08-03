import datetime
 
def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]
 
start = datetime.date(2007,01,01)
end = datetime.date(2008,02,01)
dateList = date_range(start, end)
print '\n'.join([str(date) for date in dateList])
 
