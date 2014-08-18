import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True
import glob

csv_dir = 'Z:/Desktop/tripData2013/day/'
wd      = 'Z:/Desktop/tripData2013/'

monthList = ['01','02','03','04','05','06','07','08','09','10','11','12']

print 'for pickups and dropoffs'
for m in monthList:
        #arcpy.CreateFileGDB_management(wd, "taxi_2013"+m+".gdb")
        for a_csv in glob.glob(csv_dir+"trip_data_2013"+m+"*.csv"):
                print a_csv
                tripDay = a_csv[38:46] #   Z:/Desktop/tripData2013/day/trip_data_20130201_m1.csv
                print tripDay
                gdb = wd+"taxi_2013"+m+".gdb"
                print 'table to table - bring in csv'
                #arcpy.TableToTable_conversion(a_csv,gdb,"trip_"+tripDay)
                #print 'pickup make xy event layer for pickups'
                #arcpy.MakeXYEventLayer_management(gdb+"/trip_"+tripDay,"pickup_longitude","pickup_latitude","trip_"+tripDay+"_pickup_Layer","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision","#")
                print 'pickup make xy event layer'
                arcpy.MakeXYEventLayer_management(gdb+"/trip_"+tripDay,"dropoff_longitude","dropoff_latitude","trip_"+tripDay+"_dropoff_Layer","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision","#")
                #print 'fc to fc'
                #arcpy.FeatureClassToFeatureClass_conversion("trip_"+tripDay+"_pickup_Layer",gdb,"trip_"+tripDay+"_p_xy")
                print 'fc to fc'
                arcpy.FeatureClassToFeatureClass_conversion("trip_"+tripDay+"_dropoff_Layer",gdb,"trip_"+tripDay+"_d_xy")
                #print 'project pickup to sp'
                #arcpy.Project_management(gdb+"/trip_"+tripDay+"_p_xy",gdb+"/trip_"+tripDay+"_p_xy_prj","PROJCS['NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',984250.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-74.0],PARAMETER['Standard_Parallel_1',40.66666666666666],PARAMETER['Standard_Parallel_2',41.03333333333333],PARAMETER['Latitude_Of_Origin',40.16666666666666],UNIT['Foot_US',0.3048006096012192]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]")
                print 'project dropoff to sp'                
                arcpy.Project_management(gdb+"/trip_"+tripDay+"_d_xy",gdb+"/trip_"+tripDay+"_d_xy_prj","PROJCS['NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',984250.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-74.0],PARAMETER['Standard_Parallel_1',40.66666666666666],PARAMETER['Standard_Parallel_2',41.03333333333333],PARAMETER['Latitude_Of_Origin',40.16666666666666],UNIT['Foot_US',0.3048006096012192]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]")
                #print 'near analysis for pickups to street centerline'
                #arcpy.Near_analysis(gdb+"/trip_"+tripDay+"_p_xy_prj","W:/GIS/Data/Municipal/USA/New_York/New_York_City/Streets_Centerline/20140609/CSCL_PUB_Centerline/CSCL_PUB_Centerline.shp","1000 Feet","LOCATION","ANGLE")
                print 'near analysis for dropoffs to street centerline'
                arcpy.Near_analysis(gdb+"/trip_"+tripDay+"_d_xy_prj","W:/GIS/Data/Municipal/USA/New_York/New_York_City/Streets_Centerline/20140609/CSCL_PUB_Centerline/CSCL_PUB_Centerline.shp","1000 Feet","LOCATION","ANGLE")

arcpy.GenerateNearTable_analysis("Z:/Desktop/tripData2013/taxi_201301.gdb/trip_20130101_d_xy_prj","W:/GIS/Data/Municipal/USA/New_York/New_York_City/Roadbed/ROADBED.shp","Z:/Desktop/tripData2013/taxi_201301.gdb/trip_20130101_d_xy_prj_Gener","1000 Feet","LOCATION","ANGLE","CLOSEST","0")

                print 'near analysis to roadbed'
                arcpy.Near_analysis(gdb+"/trip_"+tripDay+"_d_xy_prj","W:/GIS/Data/Municipal/USA/New_York/New_York_City/Roadbed/ROADBED.shp","1000 Feet","LOCATION","ANGLE")





