import os
from sys import argv
from os import path

if len(argv)!=2:
    print "Usage: List05.py <rootfolder>"
else:
    rootfolder=argv[1]
    file_list=[]
    if path.exists(rootfolder):
        for root,dirs,files in os.walk(rootfolder):
            print root
    else:
        root_split=rootfolder.split('/')
        print root_split[-1]+" does not exist"
