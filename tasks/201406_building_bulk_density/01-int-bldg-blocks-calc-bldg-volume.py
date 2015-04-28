import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

wd = 'V:/GIS/projects/gps/tasks/201406_building_bulk_density/data/'

print 'create and calc geoid for nyc dcp census 2010 block'
input_block_file = wd+'input/census/dcp/nycb2010_11a_av/nycb2010.shp'
new_field_name = "geoid"
field_type = "TEXT"

# CalcBorotoCountyExpr  = "boroCountyFIPS(int(!BoroCode!), !CT2010!, !CB2010!)"
# CalcBorotoCountyBlock = """def boroCountyFIPS(boro,tract, block):
#   st = '36'
#   if boro == 1:
#     return st + '061' + tract + block
#   elif boro == 2:
#     return st + '005' + tract + block
#   elif boro == 3:
#     return st + '047' + tract + block
#   elif boro == 4:
#     return st + '081' + tract + block
#   elif boro == 5:
#     return st + '085' + tract + block
#   else:
#     return 'X' + tract + block"""
    
# print 'add field and calc - block geoid'
# arcpy.AddField_management(input_block_file,new_field_name,field_type,"#","#","#","#","NULLABLE","NON_REQUIRED","#")
# arcpy.CalculateField_management(input_block_file,new_field_name,CalcBorotoCountyExpr, "PYTHON_9.3",CalcBorotoCountyBlock)

# print 'calculate block area'
# arcpy.AddField_management(input_block_file,'origblarea','DOUBLE',"#","#","#","#","NULLABLE","NON_REQUIRED","#")
# arcpy.CalculateField_management(input_block_file,'origblarea','!shape.area@squaremeters!', "PYTHON_9.3")

# print 'intersect block and buildings'
buildings = wd+'input/buildings/building_0913.shp'
intout    = wd+"processing/building_block_int.gdb/building_block_int"
# arcpy.Intersect_analysis(input_block_file+' #;'+buildings+' #',intout,"ALL","#","INPUT")

# print 'calculate building area'
# arcpy.AddField_management(intout,'bldgarea','DOUBLE',"#","#","#","#","NULLABLE","NON_REQUIRED","#")
# arcpy.CalculateField_management(intout,'bldgarea','!shape.area@squaremeters!', "PYTHON_9.3")

# print 'calculate building height meters'
# arcpy.AddField_management(intout,'bldgheightmeters','DOUBLE',"#","#","#","#","NULLABLE","NON_REQUIRED","#")
# arcpy.CalculateField_management(intout,'bldgheightmeters','!HEIGHT_ROO!*0.3048', "PYTHON_9.3")

# print 'calculate ground elevation meters'
# arcpy.AddField_management(intout,'groundelevmeters','DOUBLE',"#","#","#","#","NULLABLE","NON_REQUIRED","#")
# arcpy.CalculateField_management(intout,'groundelevmeters','!GROUND_ELE!*0.3048', "PYTHON_9.3")

# print 'calculate building volume'
# arcpy.AddField_management(intout,'buildingvolume','DOUBLE',"#","#","#","#","NULLABLE","NON_REQUIRED","#")
# arcpy.CalculateField_management(intout,'buildingvolume','!bldgarea!*!bldgheightmeters!', "PYTHON_9.3")

# print 'dissolve by geoid (w/ block area) and sum building volume'
intdis = wd+"processing/building_block_int.gdb/building_block_int_dis"
# arcpy.Dissolve_management(intout,intdis,"geoid;origblarea","buildingvolume SUM","MULTI_PART","UNSPLIT_LINES")

print 'calculate building volume'
arcpy.AddField_management(intdis,'bulkdens','DOUBLE',"#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.CalculateField_management(intdis,'bulkdens','!SUM_buildingvolume!/!origblarea!', "PYTHON_9.3")

print 'export bulk dens and building volume table'
tbloutloc = wd+"processing/building_block_int.gdb"
tbloutnam = "building_block_int_dis_tbl"
arcpy.TableToTable_conversion(intdis,tbloutloc,tbloutnam)

print 'make blocks feature layer'
arcpy.MakeFeatureLayer_management(input_block_file,"nycb2010_Layer")

print 'add join'
arcpy.AddJoin_management("nycb2010_Layer","geoid",wd+"processing/building_block_int.gdb/building_block_int_dis_tbl","geoid","KEEP_ALL")

print 'fc to fc'
arcpy.FeatureClassToFeatureClass_conversion("nycb2010_Layer",wd+"processing/census.gdb","nycb2010_bulkdens")

print 'select 6 acre parks great than or equal to'
arcpy.Select_analysis(wd+"input/parks/Parks.shp",wd+"processing/parks.gdb/parks_sel_6_acres",""""ACRES" >= 6""")

print 'make block - bulkdens feature layer'
arcpy.MakeFeatureLayer_management(wd+"processing/census.gdb/nycb2010_bulkdens","nycb2010_bulkdens_Layer")

print 'select all features'
arcpy.SelectLayerByAttribute_management("nycb2010_bulkdens_Layer","NEW_SELECTION","#")

print 'select layer by location int parks, remove selection'
arcpy.SelectLayerByLocation_management("nycb2010_bulkdens_Layer","INTERSECT",wd+"processing/parks.gdb/parks_sel_6_acres","#","REMOVE_FROM_SELECTION")

print 'select layer by location int open space, remove selection'
arcpy.SelectLayerByLocation_management("nycb2010_bulkdens_Layer","INTERSECT",wd+"input/open_space/DOITT_OPEN_SPACE_NO_PARK_01_13SEPT2010.shp","#","REMOVE_FROM_SELECTION")

#CHECK OUT OCEAN AVE and FLATBUSH, BROOKLYN these linear parks are removed. 



print 'select layer by location int buildings, remove selection'
arcpy.SelectLayerByLocation_management("nycb2010_bulkdens_Layer","INTERSECT",wd+"input/buildings/building_0913.shp","#","REMOVE_FROM_SELECTION")





print 'fc to fc'
arcpy.FeatureClassToFeatureClass_conversion("nycb2010_bulkdens_Layer",wd+"processing/census.gdb","nycb2010_bulkdens_sel_loc")

print 'sum stats'
arcpy.Statistics_analysis(wd+"processing/census.gdb/nycb2010_bulkdens_sel_loc",wd+"processing/census.gdb/nycb2010_bulkdens_sel_loc_sumstat","building_block_int_dis_tbl_bulkdens COUNT;building_block_int_dis_tbl_bulkdens MIN;building_block_int_dis_tbl_bulkdens MAX","#")

print 'sort bulkdens'
arcpy.Sort_management(wd+"processing/census.gdb/nycb2010_bulkdens_sel_loc",wd+"processing/census.gdb/nycb2010_bulkdens_sel_loc_sort","building_block_int_dis_tbl_bulkdens ASCENDING","UR")

print 'variables after running sum stats'
#old freq = 38716.0
freq = 35646.0
minV = 0
maxV = freq

CalcQuartilesExpr  = "Reclass(!OBJECTID!, minV, maxV)"
CalcQuartilesBlock = """def Reclass(qVal, Min, Max):
  quant1 = Min + ((Max - Min)/4)
  quant2 = Min + (((Max - Min)/4)*2)
  quant3 = Min + (((Max - Min)/4)*3)

  if (qVal >= Min and qVal < quant1):
  	return 1
  elif (qVal >= quant1 and qVal < quant2):
  	return 2
  elif (qVal >= quant2 and qVal < quant3):
  	return 3
  elif (qVal >= quant3 and qVal <= Max):
  	return 4
  else:
  	return 99"""

print 'calculate bulkdens quartiles'
arcpy.AddField_management(wd+"processing/census.gdb/nycb2010_bulkdens_sel_loc_sort",'bulkdensquant','LONG')
arcpy.CalculateField_management(wd+"processing/census.gdb/nycb2010_bulkdens_sel_loc_sort",'bulkdensquant',CalcQuartilesExpr , "PYTHON_9.3",CalcQuartilesBlock )

print 'delete field'
arcpy.DeleteField_management(wd+"processing/census.gdb/nycb2010_bulkdens_sel_loc_sort","CB2010;BoroCode;BoroName;CT2010;BCTCB2010;Shape_Leng;building_block_int_dis_tbl_OBJECTID;building_block_int_dis_tbl_geoid;building_block_int_dis_tbl_origblarea;building_block_int_dis_tbl_SUM_buildingvolume;building_block_int_dis_tbl_Shape_Length;building_block_int_dis_tbl_Shape_Area")



###old
#print 'clean up table and export table (gdb) - psuedo manual'
#arcpy.TableToTable_conversion("nycb2010_bulkdens_sort","V:/GIS/projects/gps/tasks/201406_tree_gps_walks/data/processing/census.gdb","nycb2010_bulkdens_sort_tbl","#","""geoid "geoid" true true false 254 Text 0 0 ,First,#,V:/GIS/projects/gps/tasks/201406_building_bulk_density/data/processing/census.gdb/nycb2010_bulkdens_sort,geoid,-1,-1;origblarea "origblarea" true true false 8 Double 0 0 ,First,#,V:/GIS/projects/gps/tasks/201406_building_bulk_density/data/processing/census.gdb/nycb2010_bulkdens_sort,origblarea,-1,-1;sum_buildingvolume "SUM_buildingvolume" true true false 8 Double 0 0 ,First,#,V:/GIS/projects/gps/tasks/201406_building_bulk_density/data/processing/census.gdb/nycb2010_bulkdens_sort,building_block_int_dis_tbl_SUM_buildingvolume,-1,-1;bulkdens "bulkdens" true true false 8 Double 0 0 ,First,#,V:/GIS/projects/gps/tasks/201406_building_bulk_density/data/processing/census.gdb/nycb2010_bulkdens_sort,building_block_int_dis_tbl_bulkdens,-1,-1;bulkdensquant "bulkdensquant" true true false 4 Long 0 0 ,First,#,V:/GIS/projects/gps/tasks/201406_building_bulk_density/data/processing/census.gdb/nycb2010_bulkdens_sort,bulkdensquant,-1,-1""","#")

