import numpy as np
import os
import cv2
import csv



#Define the path location
path= "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/refernceTest/separate/Test2/labels"
dest = "/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/labels_csv/Train/patch_0_ref"

if not  os.path.exists(dest):
    os.makedirs(dest)

# path where you can write the pose or segmented videos 


for root,_,files in os.walk(path):
    if files:
       
        # finding  the class name

        # class_name = root.split(os.sep)[-1:]
        for file in sorted(files):
            print(file)
            base_name, extension = os.path.splitext(file)
            base_name = base_name.replace("_xy", "")
            with open(os.path.join(root, file), 'r') as f:

                lines = f.readlines()
            # headers = ['image_name', 'scale', 'center_w', 'center_h', 'original_0_x', 'original_0_y', 'original_1_x', 'original_1_y', 'original_2_x', 'original_2_y', 'original_3_x', 'original_3_y', 'original_4_x', 'original_4_y', 'original_5_x', 'original_5_y', 'original_6_x', 'original_6_y', 'original_7_x', 'original_7_y', 'original_8_x', 'original_8_y', 'original_9_x', 'original_9_y', 'original_10_x', 'original_10_y', 'original_11_x', 'original_11_y', 'original_12_x', 'original_12_y', 'original_13_x', 'original_13_y', 'original_14_x', 'original_14_y', 'original_15_x', 'original_15_y', 'original_16_x', 'original_16_y', 'original_17_x', 'original_17_y', 'original_18_x', 'original_18_y']
            headers = ['image_name', 'scale', 'center_w', 'center_h', 'original_0_x', 'original_0_y']
            coords = []
            for line in lines:
                parts = line.split()
                split_values = parts[0].split(',')
                if len(split_values) == 2:
                    coords.append((float(split_values[0]), float(split_values[1])))
            
            
            final_value = [item for tpl in coords for item in tpl]

            with open(f'{dest}/patch_0_test2.csv', mode='a', newline='') as Csvfile:
                writer = csv.writer(Csvfile)
                if Csvfile.tell() == 0:
                    writer.writerow(headers) 
                writer.writerow([f'{base_name}.jpg', 0.32, 32,32] + final_value) 
                # writer.writerow([f'{file.split(".")[0]}.jpg', 0.32, 32,32] + final_value)  # flatten the list of tuples and write as one row

            

        # finding the destination folder path
        

        # checking if the path exists or not
    