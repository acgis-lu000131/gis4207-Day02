from sys import argv
arcpy= None
def importarcpy():
    global arcpy
    if arcpy== None:
        import arcpy
        from arcpy import Describe
        from arcpy import env

if len(argv) != 2:
    print "Usage: List04.py <RootFolder>"

else:
    importarcpy()
    path_to_folder= r"..\..\..\Data\Canada"
    folder= argv[1]
    arcpy.env.workspace= path_to_folder+folder


    if arcpy.Exists(folder)==True:
        workspaces=arcpy.ListWorkspaces()
        print workspaces

    else:
        print "workspace does not exist."

