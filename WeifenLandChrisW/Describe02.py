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

print "{:13}: {}".format("BaseName: ", description.BaseName)
print "{:13}: {}".format("CatalougePath: ",description.CatalogPath)
print "{:13}: {}".format("DataType: ", description.DataType)