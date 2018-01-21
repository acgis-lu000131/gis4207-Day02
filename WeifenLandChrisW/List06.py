import os
from sys import argv
from os import path
arcpy=None
def importarcpy():
    global arcpy
    if arcpy== None:
        import arcpy
        from arcpy import Describe
        from arcpy import env

if len(argv)!=2:
    print "Usage: List06.py <rootfolder>"
else:
    rootfolder=argv[1]
    file_list=[]
    if path.exists(rootfolder):
        importarcpy()
        for root,dirs,files in os.walk(rootfolder):
            for r in dirs:
               for w in arcpy.ListWorkspaces():
                    print os.path.abspath(w)
    else:
        root_split=rootfolder.split('/')
        print root_split[-1]+" does not exist"