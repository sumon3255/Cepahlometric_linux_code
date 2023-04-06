





import os, cv2, random, shutil
import numpy as np

output_file_path = "new.txt"
# Source path
source = "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/images/Test2Data"
# Destination path
dest =  "/home/sumon/CepahloMetric/Dataset_v2/yolo"


labels_path = "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/labels/Test2Data"

for root,_,files in os.walk(source):
    if files:
        for file in files:
            # Finding the class name
            class_name =  os.path.splitext(os.path.basename(file))[0]
            # print(class_name)
            
            with open(f"{labels_path}/{class_name}.txt") as f:
                landmarks = np.array([list(map(float, line.strip().split(","))) for line in f])

                

            

            # destination file path
            dest_folder_path = os.path.join(dest, class_name)
            # checking if the destination folder exists
            if not os.path.exists(dest_folder_path):
                os.makedirs(dest_folder_path)
            
            
            # # file path
            file_path=os.path.join(root,  file)
            img = cv2.imread(file_path)
            
            image_width = img.shape[1]
            image_height = img.shape[0]
            
            
            patch_size = 64


            stride = int(patch_size / 2)
            
            with open(f"{dest}/{class_name}.txt", "w") as output_file:
                for i, (x, y) in enumerate(landmarks):
                    # x_normalized = x / image_width
                    # y_normalized = y / image_height
                    x1 = int(x - patch_size / 2)
                    y1 = int(y - patch_size / 2)
                    x2 = int(x + patch_size / 2)
                    y2 = int(y + patch_size / 2)

                    # Define the bounding box size
                    box_width = 0.1
                    box_height = 0.1

                    # Convert the bounding box size to the YOLO format
                    # box_width_normalized = box_width / image_width
                    # box_height_normalized = box_height / image_height

                    # # Calculate the normalized coordinates of the center of the bounding box
                    # x_center_normalized = x_normalized + box_width_normalized / 2
                    # y_center_normalized = y_normalized + box_height_normalized / 2
                    
                    image_width = img.shape[1]
                    image_height = img.shape[0]
                    x_center_normalized = (x - x1) / patch_size
                    y_center_normalized = (y - y1) / patch_size
                    box_width_normalized = patch_size / image_width
                    box_height_normalized = patch_size / image_height

                    # Write the YOLO format bounding box coordinates to the output file
                    output_file.write(f"0 {x_center_normalized} {y_center_normalized} {box_width_normalized} {box_height_normalized}\n")


