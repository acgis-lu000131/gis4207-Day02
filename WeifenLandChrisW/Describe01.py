
import arcpy
from arcpy import Describe
from arcpy import env
import os


working_folder= os.path.dirname(__file__)
os.chdir(working_folder)
env.workspace=  r"..\..\..\Data\Canada"
fcList= arcpy.ListFeatureClasses()
working_file=fcList[4]
description=Describe(working_file)

print "BaseName: "+ description.BaseName
print "CatalougePath: "+description.CatalogPath
print "DataType: "+ description.DataType



