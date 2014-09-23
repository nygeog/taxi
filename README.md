#Taxi

Near functions use local projection system. 
NAD 83 (feet) State Plane New York, Long Island

##To Do:
1) Find out how many dropoffs & pickups have outside NYC lat/lngs (or invalid - null island)

2) Export using 

	import os

	#run this only in windows with OSGEO4W Administrator Shell open


	#for loop this through every single day of the year
	os.system('ogr2ogr -overwrite -f CSV "U:/data/taxi/tripData2013/test/trip_20130902_d_road.csv" "U:/data/taxi/tripData2013/taxi_201309.gdb" "trip_20130902_d_road"')


##Geodatabase Structure


Each day has a file
######trip_^^^^^^ 
input day file, with pickup and dropoff x,y data, with trip distance data.
######trip_^^^^^^_d_road
Dropoff - near function on roadbed, 0 distance indicates within roadbed. 
######trip_^^^^^^_d_xy
Dropoff - xy brought in as lat,lng. 
######trip_^^^^^^_d_xy_prj
Dropoff - xy projected with near road centerline FID. 
######trip_^^^^^^_p_road
Pickup - near function on roadbed, 0 distance indicates within roadbed.
######trip_^^^^^^_p_xy
Pickup - xy brought in as lat,lng. 
######trip_^^^^^^_p_xy_prj
Pickup - xy projected with near road centerline FID.

##Number of Trips by Month
for month 1, the count of taxi trips is:
14776615
month 1 has 31 number of days, averaging 476665.0 taxi trips per day

for month 2, the count of taxi trips is:
13990176
month 2 has 28 number of days, averaging 499649.142857 taxi trips per day

for month 3, the count of taxi trips is:
15749228
month 3 has 31 number of days, averaging 508039.612903 taxi trips per day

for month 4, the count of taxi trips is:
15100468
month 4 has 30 number of days, averaging 503348.933333 taxi trips per day

for month 5, the count of taxi trips is:
15285049
month 5 has 31 number of days, averaging 493066.096774 taxi trips per day

for month 6, the count of taxi trips is:
14385456
month 6 has 30 number of days, averaging 479515.2 taxi trips per day

for month 7, the count of taxi trips is:
13823840
month 7 has 31 number of days, averaging 445930.322581 taxi trips per day

for month 8, the count of taxi trips is:
12597109
month 8 has 31 number of days, averaging 406358.354839 taxi trips per day

for month 9, the count of taxi trips is:
14107693
month 9 has 30 number of days, averaging 470256.433333 taxi trips per day

for month 10, the count of taxi trips is:
15004556
month 10 has 31 number of days, averaging 484017.935484 taxi trips per day

for month 11, the count of taxi trips is:
14388451
month 11 has 30 number of days, averaging 479615.033333 taxi trips per day

for month 12, the count of taxi trips is:
13971118
month 12 has 31 number of days, averaging 450681.225806 taxi trips per day


the total number of trips in the year is 173179759
the average number of taxi trips per day is 474465.093151