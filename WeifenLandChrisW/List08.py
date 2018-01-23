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

if len(argv)!=3:
    print "Usage: List05.py <rootfolder> <outFileName>"
else:
    rootfolder=argv[1]
    file_list=[]
    if path.exists(rootfolder):
        importarcpy()
        outfile=open(argv[2],'w')
        arcpy.env.workspace=argv[1]
        for root,dirs,files in os.walk(rootfolder):
            for r in dirs:
               for w in arcpy.ListWorkspaces():
                    outfile.write(os.path.abspath(w+"\n"))
                    for fc in arcpy.ListFeatureClasses():
                        outfile.write(fc+"\n")
        outfile.close()
    else:
        root_split=rootfolder.split('/')
        print root_split[-1]+" does not exist"