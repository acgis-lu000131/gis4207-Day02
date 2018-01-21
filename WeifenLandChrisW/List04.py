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
    folder= argv[1]
    arcpy.env.workspace= folder
    print arcpy.env.workspace

    if arcpy.Exists(folder)==True:
        for workspaces in arcpy.ListWorkspaces('','all'):
            print workspaces


    else:
        print "Sorry, workspace does not exist."

