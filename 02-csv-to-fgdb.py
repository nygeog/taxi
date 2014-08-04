import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True
import glob

#for each csv in this day folder, table to table csv to table. 

csv_dir = 'Z:/Desktop/tripData2013/day/'

print 'add geoid field for each table - 5 seconds'
for a_csv in glob.glob(csv_dir+"*.csv"):
	print a_csv
	tripDay = a_csv[40:48] #   Z:/Desktop/tripData2013/day/trip_data_1_20130201.csv
	print tripDay
	#arcpy.TableToTable_conversion(a_csv,"Z:/Desktop/tripData2013/taxi.gdb","trip_"+tripDay)
	#arcpy.MakeXYEventLayer_management("Z:/Desktop/tripData2013/taxi.gdb/trip_"+tripDay,"pickup_longitude","pickup_latitude","trip_"+tripDay+"_Layer","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision","#")
	#arcpy.FeatureClassToFeatureClass_conversion("trip_"+tripDay+"_Layer","Z:/Desktop/tripData2013/taxi.gdb","trip_"+tripDay+"_p_xy")

	#gotta remove the last day which is Feb. 1.

	arcpy.Project_management("Z:/Desktop/tripData2013/taxi.gdb/trip_"+tripDay+"_p_xy","Z:/Desktop/tripData2013/taxi.gdb/trip_"+tripDay+"_p_xy_prj","PROJCS['NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',984250.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-74.0],PARAMETER['Standard_Parallel_1',40.66666666666666],PARAMETER['Standard_Parallel_2',41.03333333333333],PARAMETER['Latitude_Of_Origin',40.16666666666666],UNIT['Foot_US',0.3048006096012192]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]")
	arcpy.Near_analysis("Z:/Desktop/tripData2013/taxi.gdb/trip_"+tripDay+"_p_xy_prj","W:/GIS/Data/Municipal/USA/New_York/New_York_City/Streets_Centerline/20140609/CSCL_PUB_Centerline/CSCL_PUB_Centerline.shp","1000 Feet","LOCATION","ANGLE")