import arcpy
from arcpy import Describe
from arcpy import env
from sys import argv

if len(argv) != 2:
    print "Describe03.py <FeatureClassName>"

else:
    working_folder= argv[0]
    env.workspace=  r"..\..\..\Data\Canada"
    working_file= argv[1]
    description=Describe(working_file)

    print "{:13}: {}".format("BaseName: ", description.BaseName)
    print "{:13}: {}".format("CatalogPath: ",description.CatalogPath)
    print "{:13}: {}".format("DataType: ", description.DataType)