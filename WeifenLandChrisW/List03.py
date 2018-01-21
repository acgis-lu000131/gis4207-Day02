from sys import argv
arcpy= None
def importarcpy():
    global arcpy
    if arcpy== None:
        import arcpy
        from arcpy import Describe
        from arcpy import env

if len(argv) != 3:
    print "Usage: List03.py <FeatureClassName> <FeatureType>"

else:
    importarcpy()
    working_folder= argv[0]
    path_to_folder= r"..\..\..\Data"
    folder= argv[1]
    arcpy.env.workspace= path_to_folder+folder
    fctype=arcpy.ListFeatureClasses('',argv[2])

    if arcpy.Exists(working_folder)==True:
        if len(fctype)>0:
            for fc in fctype:
                print fc
        else:
            print argv[2]+ "Is not a valid feature type"
    else:
        print datafolder +" does not exist."