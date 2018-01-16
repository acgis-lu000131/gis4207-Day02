
from sys import argv
arcpy= None
def importarcpy():
    global arcpy
    if arcpy== None:
        import arcpy
        from arcpy import Describe
        from arcpy import env

if len(argv) != 2:
    print "Describe03.py <FeatureClassName>"

else:
    importarcpy()
    working_folder= argv[0]
    env.workspace=  r"..\..\..\Data\Canada"
    working_file=argv[1]
    description=Describe(working_file)

    print "{:13}: {}".format("BaseName: ", description.BaseName)
    print "{:13}: {}".format("CatalougePath: ",description.CatalogPath)
    print "{:13}: {}".format("DataType: ", description.DataType)