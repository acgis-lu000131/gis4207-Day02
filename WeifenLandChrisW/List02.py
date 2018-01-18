from sys import argv
arcpy= None
def importarcpy():
    global arcpy
    if arcpy== None:
        import arcpy
        from arcpy import Describe
        from arcpy import env

if len(argv) != 2:
    print "List02.py <FeatureClassName>"

else:
    importarcpy()
    working_folder= argv[0]
    path_to_folder= r"..\..\..\Data"
    folder= argv[1]
    arcpy.env.workspace= path_to_folder+folder
    fclist=arcpy.ListFeatureClasses()

    if arcpy.Exists(working_folder)==True:
        for fc in fclist:
            print fc
    else:
        print working_folder+" does not exist."