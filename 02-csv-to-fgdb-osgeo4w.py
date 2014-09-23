import os

#run this only in windows with OSGEO4W Administrator Shell open


#for loop this through every single day of the year
os.system('ogr2ogr -overwrite -f CSV "U:/data/taxi/tripData2013/test/trip_20130902_d_road.csv" "U:/data/taxi/tripData2013/taxi_201309.gdb" "trip_20130902_d_road"')

