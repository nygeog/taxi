import pandas as pd
import datetime

def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]

dropList = ['medallion','hack_license','vendor_id','rate_code','store_and_fwd_flag','passenger_count','trip_time_in_secs']
typeList = ['pickup','dropoff']

for i in range(2,13):
	inCSV = '/Users/danielmsheehan/Desktop/tripData2013/trip_data_'+str(i)+'.csv'
	df = pd.read_csv(i).drop(dropList, axis=1) #nrows=200000
	print 'read complete'

	print 'add new col'
	for j in typeList:
		df[j+'_datetime'] = df[j+'_datetime'].astype('datetime64[ns]')
		df[j+'_date'] = df[j+'_datetime'].map(pd.Timestamp.date)
		df = df.drop(j+'_datetime', axis=1)

	monthStart = i
	yearStart  = 2013
	if i > 11:
		monthEnd = 1
		yearEnd  = 2014
	else:
		monthEnd = i + 1
		yearEnd  = 2013

	start = datetime.date(yearStart,monthStart,01)
	end = datetime.date(yearEnd,monthEnd,01)
	dateList = date_range(start, end)
	for k in dateList:
		outCSV = '/Users/danielmsheehan/Desktop/tripData2013/day/trip_data_1_'+str(k).replace('-','')+'.csv'
		#m = k.split('-')[0]
		y = str(k)[0:4]
		m = str(k)[5:7]
		d = str(k)[8:10]
		yearV = int(y)
		monthV = int(m)
		dayV = int(d)
		dft = df[(df.pickup_date == datetime.date(yearV, monthV, dayV))]
		print 'save as csv for ' + str(k)
		#df = df.
		dft.to_csv(outCSV, index=False)
		
