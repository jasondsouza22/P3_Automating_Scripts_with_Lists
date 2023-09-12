import arcpy

arcpy.env.workspace = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P3_Automating_Scripts_with_Lists\Practical_3_ProProject\03_Automating_Scripts_With_Lists.gdb"

# Creating a list of feature classes in the current workspace
fc_list = arcpy.ListFeatureClasses()

for fc_name in fc_list:
    print(fc_name)