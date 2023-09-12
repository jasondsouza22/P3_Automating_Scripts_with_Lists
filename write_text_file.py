import os

folder_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P3_Automating_Scripts_with_Lists"

file_name = "writeme.txt"

file_path = os.path.join(folder_path, file_name)

# Read only ('r')
# Read and Write ('r+')
# Write only (w)
# Write and Read ('w+')
# Append Only 9 ('a')
# Append and Read ('a+')

file_obj = open(file_path, 'w')

input = "Glory, Glory Man United"
file_obj.write(input)
file_obj.close()

print("Process Completed")