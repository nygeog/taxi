import pandas as pd
import datetime

def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]

csvList = ['/Users/danielmsheehan/Desktop/tripData2013/trip_data_1.csv']
#will change this to be a range 1-12 for motnsh
dropList = ['medallion','hack_license','vendor_id','rate_code','store_and_fwd_flag','passenger_count','trip_time_in_secs']
typeList = ['pickup','dropoff']

print 'just working with January data for now'

for i in csvList:
	 #'' + i
	df = pd.read_csv(i).drop(dropList, axis=1) #nrows=200000
	print 'read complete'

	print 'add new col'
	for j in typeList:
		df[j+'_datetime'] = df[j+'_datetime'].astype('datetime64[ns]')
		df[j+'_date'] = df[j+'_datetime'].map(pd.Timestamp.date)
		df = df.drop(j+'_datetime', axis=1)

	start = datetime.date(2013,01,01)
	end = datetime.date(2013,02,01)
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
		
