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
    if arcpy.Exists(working_file):
        description=Describe(working_file)
        listoffields= arcpy.ListFields(working_file)
    else:
        print working_file +" does not exist."


fmt= "{:15} {:15} {}"
headings=("Field Name", "Field Type", "Length")
underlines= (len(headings[0])*'-', len(headings[1])*'-', len(headings[2])*'-')



print fmt.format(*headings)
print fmt.format(*underlines)
for field in listoffields:
    fields= (field.name, field.type, field.length)
    print fmt.format(*fields)
