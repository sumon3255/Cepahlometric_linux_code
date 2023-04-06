import os, cv2, random, shutil, csv
import numpy as np


# Source path
source = "/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/main_txt_patches/patch_0"
# Destination path

# /home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/predicted_txt/patch_0_n0_re
labels_path = "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/labels/Test1Data"
labels_path1 = "/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/predicted_txt/patch_0_ref"

# CSV file path
csv_path = "/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/coverted_labels_patch/coverted_patch_0_ref.csv"

# Open the CSV file for writing
with open(csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for root,_,files in os.walk(source):
        if files:
            for file in sorted(files):
                headers = ['original_0_x', 'original_0_y']
                # Finding the class name
                class_name =  os.path.splitext(os.path.basename(file))[0]
                # print(class_name)
                
                with open(f"/home/sumon/CepahloMetric/Dataset_v2/average/average_xy.txt") as f:
                    landmarks = np.array([list(map(float, line.strip().split(","))) for line in f])
                
                with open(f"{labels_path}/{class_name}.txt") as f:
                    landmarks2 = np.array([list(map(float, line.strip().split(","))) for line in f])

                    
                with open(f"{labels_path1}/{class_name}.txt") as f:
                    landmarks3 = np.array([list(map(float, line.strip().split(","))) for line in f])
                

                # destination file path

                
                # # file path

                
                
                patch_size = 64


                stride = int(patch_size / 2)
                
                for i, (xo, yo) in enumerate(landmarks2):
                    
                    # x1 = int(landmarks[i][0] - patch_size / 2)
                    # y1 = int(landmarks[i][1]  - patch_size / 2)
                    # x2 = int(landmarks[i][0] + patch_size / 2)
                    # y2 = int(landmarks[i][1]  + patch_size / 2)
                    print(landmarks3[i][1])
                    # xo_x1 = (xo - x1)
                    # yo_y1 = (yo - y1)
                    # print(xo_x1, yo_y1)
      
                        

                        # # new_x = patch.shape[1] / 2
                        # # new_y = patch.shape[0] / 2
                
                        # # print(new_x,new_y)
                
                            
                    
                        # patch = cv2.circle(patch, (int(new_x), int(new_y)), 2, (0, 0, 255), -1)
          

                    # Recalculate the xy coordinates relative to the patch
                    # new_x = x - x1 + int(patch_size / 2)
                    # new_y = y - y1 + int(patch_size / 2)
                    # Write the recalculated xy coordinates to the output file
                    # x_prime = xo - x1
                    # y_prime = yo - y1
                    # print(f"Real  value is {xo,yo}")
                    # x_gt = landmarks3[i][0] + x1
                    # y_gt = landmarks3[i][1] + y1
                    # print(f"converted value is {x_gt,y_gt}")
                    # if csvfile.tell() == 0:
                    #     csvwriter.writerow(headers) 
                        
                    #     # Write the x_gt and y_gt values to the CSV file
                    # csvwriter.writerow([x_gt,y_gt])
