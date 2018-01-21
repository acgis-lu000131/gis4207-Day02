from sys import argv
arcpy= None
def importarcpy():
    global arcpy
    if arcpy== None:
        import arcpy
        from arcpy import Describe
        from arcpy import env

if len(argv) != 2:
    print "Usage: Describe05.py <FeatureClassName>"

else:
    importarcpy()
    working_folder= argv[0]
    arcpy.env.workspace=  r"..\..\..\Data\Canada"
    working_file=argv[1]
    if arcpy.Exists(working_file):
        description=arcpy.Describe(working_file)
    else:
        print working_file +" does not exist."


    print "{:13}: {}".format("BaseName: ", description.BaseName)
    print "{:13}: {}".format("CatalougePath: ",description.CatalogPath)
    print "{:13}: {}".format("DataType: ", description.DataType)