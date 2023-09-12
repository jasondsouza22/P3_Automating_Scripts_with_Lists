import os

folder_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P3_Automating_Scripts_with_Lists"

file_name = "readme.txt"

file_path = os.path.join(folder_path, file_name)

file_obj = open(file_path, 'r')

# print(file_obj.read(10))

# print(file_obj.readline())

lines = (file_obj.readlines())

count = 1
for line in lines:
    print("{} -{}".format(count, line))
    count = count + 1



