import arcpy
import os

arcpy.env.workspace = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P3_Automating_Scripts_with_Lists\Practical_3_ProProject\03_Automating_Scripts_With_Lists.gdb"

# Output folder path is where the txt file will get created
output_folder_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P3_Automating_Scripts_with_Lists"
# Output file name
output_text_file = "field_info.txt"

output_file_path = os.path.join(output_folder_path, output_text_file)

print(output_file_path)

file_obj = open(output_file_path, "w")

# Listing all feature class from the gdb
fc_list = arcpy.ListFeatureClasses()

# Looping all features classes
for name in fc_list:
    print(name)
    file_obj.write(name + "\n")

# Listing all fields and looping fields
    field_list = arcpy.ListFields(name)
    for field in field_list:
        print("Name: {}, Type: {}, Length: {}".format(field.name, field.type, field.length))
        file_obj.write("Name: {}, Type: {}, Length: {} \n".format(field.name, field.type, field.length))

        print("------------------------------------------")
        file_obj.write("---------------------------------------------\n")
file_obj.close()
print("Process Completed")