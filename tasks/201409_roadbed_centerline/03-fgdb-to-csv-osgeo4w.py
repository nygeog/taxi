import os
import datetime
from calendar import monthrange
#run this only in windows with OSGEO4W Administrator Shell open

for i in range(1,2): #change to 13
	j = str(i)
	x = monthrange(2013, i)
	y = x[1]
	if len(j) == 1:
		j = '0'+j #add leading zero to months less than 10 (October)

	for z in range(1, y+1):
		k = str(z)
		if len(k) == 1:
			k = '0'+k
		gdalCMD1 = 'ogr2ogr -overwrite -f CSV "W:/Desktop/tripData2013/tables/trip_2013'+j+k+'_d_roadbed.csv" "W:/Desktop/tripData2013/taxi_2013'+j+'.gdb" "trip_2013'+j+k+'_d_road"'
		gdalCMD2 = 'ogr2ogr -overwrite -f CSV "W:/Desktop/tripData2013/tables/trip_2013'+j+k+'_p_roadbed.csv" "W:/Desktop/tripData2013/taxi_2013'+j+'.gdb" "trip_2013'+j+k+'_p_road"'
		gdalCMD3 = 'ogr2ogr -overwrite -f CSV "W:/Desktop/tripData2013/tables/trip_2013'+j+k+'_d_centerl.csv" "W:/Desktop/tripData2013/taxi_2013'+j+'.gdb" "trip_2013'+j+k+'_d_xy_prj"'	
		gdalCMD4 = 'ogr2ogr -overwrite -f CSV "W:/Desktop/tripData2013/tables/trip_2013'+j+k+'_p_centerl.csv" "W:/Desktop/tripData2013/taxi_2013'+j+'.gdb" "trip_2013'+j+k+'_p_xy_prj"'
		
		print gdalCMD1
		os.system(gdalCMD1)
		print gdalCMD2
		os.system(gdalCMD2)
		print gdalCMD3
		os.system(gdalCMD3)
		print gdalCMD4
		os.system(gdalCMD4)

