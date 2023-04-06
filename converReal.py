import os, cv2, random, shutil, csv
import numpy as np


# Source path
source = "/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/main_txt_patches/patch_0"
# Destination path

# /home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/predicted_txt/patch_0_n0_re

labels_path = "/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/predicted_txt/patch_0_random"

# CSV file path
csv_path = "/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/coverted_labels_patch/coverted_patch_0_random.csv"

# Open the CSV file for writing
with open(csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for root,_,files in os.walk(source):
        if files:
            for file in sorted(files):
                headers = ['original_0_x', 'original_0_y']
                # Finding the class name
                class_name =  os.path.splitext(os.path.basename(file))[0]
                print(class_name)

                with open(os.path.join(root,file)) as f:
                    landmarks = np.array([list(map(float, line.strip().split(","))) for line in f])


                with open(f"{labels_path}/{class_name}.txt") as f:
                    landmarks2 = np.array([list(map(float, line.strip().split(","))) for line in f])


                patch_size = 64

                for i, (x, y) in enumerate(landmarks):
                    print(f"real valueis : {x,y}")

                    for i, (new_x,new_y) in enumerate(landmarks2):
                        x_gt = new_x + x - int(patch_size/ 2)
                        y_gt = new_y + y - int(patch_size / 2)
                        print(f"converted value is {x_gt,y_gt}")
                        if csvfile.tell() == 0:
                           csvwriter.writerow(headers) 
                        
                        # Write the x_gt and y_gt values to the CSV file
                        csvwriter.writerow([x_gt, y_gt])
