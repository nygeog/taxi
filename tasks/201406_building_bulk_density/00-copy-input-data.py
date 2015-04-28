import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

wd = 'V:/GIS/projects/gps/tasks/201406_building_bulk_density/data/'

print 'copy blocks'
cb2000in  = 'W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nycb2000_11a_av'
cb2010in  = 'W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nycb2010_11a_av'
cb2000out = wd+'input/census/dcp/nycb2000_11a_av'
cb2010out = wd+'input/census/dcp/nycb2010_11a_av'
#arcpy.Copy_management(cb2000in,cb2000out,"Workspace")
#arcpy.Copy_management(cb2010in,cb2010out,"Workspace")

print 'copy building footprints'
inFile  = r'W:\GIS\Data\Municipal\USA\New_York\New_York_City\Building_footprints\building_footprints_shape_09-13'
outFile = wd+'input/buildings'
#arcpy.Copy_management(inFile,outFile,"Workspace")

print 'copy elevation points'
inFile  = r'W:\GIS\Data\Municipal\USA\New_York\New_York_City\Elevation\elevation_points.gdb'
outFile = wd+'input/elevation/elevation_points.gdb'
arcpy.Copy_management(inFile,outFile,"Workspace")

print 'copy roadbeds' 
inFile  = r'W:\GIS\Data\Municipal\USA\New_York\New_York_City\Roadbed'
outFile = wd+'input/roadbed'
arcpy.Copy_management(inFile,outFile,"Workspace")

print 'copy transportation structures' 
inFile  = r'W:\GIS\Data\Municipal\USA\New_York\New_York_City\Transportation_Structures'
outFile = wd+'input/transportation_structures'
arcpy.Copy_management(inFile,outFile,"Workspace")

print 'copy parks'
inFile  = 'W:/GIS/Data/Municipal/USA/New_York/New_York_City/Parks/2014/DPR_Parks_001'
outFile = wd+'input/parks'
arcpy.Copy_management(inFile,outFile,"Workspace")

print 'copy open space'
inFile  = 'W:/GIS/Data/Municipal/USA/New_York/New_York_City/Open_Space/DOITT_OPEN_SPACE'
outFile = wd+'input/open_space'
arcpy.Copy_management(inFile,outFile,"Workspace")
