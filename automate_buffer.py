import arcpy

arcpy.env.workspace = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P3_Automating_Scripts_with_Lists\Practical_3_ProProject\03_Automating_Scripts_With_Lists.gdb"

fc_list = arcpy.ListFeatureClasses()

buffer_distance = 0

for fc in fc_list:
    desc_obj = arcpy.Describe(fc)
    shape_type = desc_obj.shapeType

    # Point: 500 feet, Polyline: 1000 feet, Polygon: 600 feet

    if shape_type == "Point":
        buffer_distance = "500 feet"
    elif shape_type == "Polyline":
        buffer_distance = "1000 feet"
    elif shape_type == "Polygon":
        buffer_distance = "600 feet"

    output_buffer = fc + "_Buffer"

    arcpy.analysis.Buffer(fc, output_buffer, buffer_distance)

print("Process Completed")