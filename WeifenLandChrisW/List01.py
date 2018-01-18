import arcpy
from arcpy import Describe
from arcpy import env
import os


working_folder= os.path.dirname(__file__)
os.chdir(working_folder)
env.workspace=  r"..\..\..\Data\SanFrancisco"
fcList= arcpy.ListFeatureClasses()

for fc in fcList:
    print fc
