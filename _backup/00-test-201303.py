import pandas as pd
import datetime


inCSV = '/Users/danielmsheehan/Desktop/tripData2013/trip_data_2.csv'
outCSV = '/Users/danielmsheehan/Desktop/tripData2013/day/trip_data_2_TEST.csv'

df = pd.read_csv(inCSV, nrows=200)#.drop(dropList, axis=1) #nrows=200000
df = df.rename(columns=lambda x: x.replace(' ', ''))
theCols = list(df.columns.values)
print theCols
df.to_csv(outCSV, index=False)

# ValueError: labels ['hack_license' 'vendor_id' 'rate_code' 'store_and_fwd_flag'
#  'passenger_count' 'trip_time_in_secs'] not contained in axis

# medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude