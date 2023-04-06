import os, cv2, random, shutil
import numpy as np


# Source path
source = "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/images/Test2Data"
# Destination path
dest =  "/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/Test2_images"


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
            
            
            patch_size = 64


            stride = int(patch_size / 2)
            
            
            for i, (x, y) in enumerate(landmarks):
                x1 = int(x - patch_size / 2)
                y1 = int(y - patch_size / 2)
                x2 = int(x + patch_size / 2)
                y2 = int(y + patch_size / 2)
                
                patch = img[y1:y2, x1:x2]
                new_x = patch.shape[1] / 2
                new_y = patch.shape[0] / 2
        
                print(new_x,new_y)
                if patch.shape[0] < patch_size or patch.shape[1] < patch_size:
                    diff_y = patch_size - patch.shape[0]
                    diff_x = patch_size - patch.shape[1]
                    patch = cv2.copyMakeBorder(patch, 0, diff_y, 0, diff_x, cv2.BORDER_CONSTANT, value=(0,0,0))
            
            
                # patch = cv2.circle(patch, (int(new_x), int(new_y)), 2, (0, 0, 255), -1)
                cv2.imwrite(f"{dest_folder_path}/{class_name}_patch_{i}.jpg", patch)

                # Recalculate the xy coordinates relative to the patch
                # new_x = x - x1 + int(patch_size / 2)
                # new_y = y - y1 + int(patch_size / 2)
                # Write the recalculated xy coordinates to the output file
                output_file = open(f"{dest_folder_path}/{class_name}_patch_{i}_xy.txt", "w")
                output_file.write(f"{new_x},{new_y}\n")


            # output_file.close()

            # print(img)

            # # destination file path
            # dest_file_path = os.path.join(dest_folder_path, file.split('.')[0]+'.avi')

            # # Capturing the video from file path
            # video_cap = cv2.VideoCapture(file_path)
            # # finding the fps to keep the fps same in the converted  video
            # fps = int(video_cap.get(cv2.CAP_PROP_FPS))
            # # counting the total number of frames in the video
            # frame_number = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # # check if the video has more frames than our required number
           
          