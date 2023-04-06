# import os
# import cv2

# # Define the size of the output images
# IMG_SIZE = 256

# # Iterate over all txt files in the directory
# for file in os.listdir('.'):
#     if file.endswith('.txt'):
#         # Create a black image with size 256x256
#         img = cv2.im

#         with open(file, 'r') as f:
#             # Read all lines in the file
#             lines = f.readlines()
#             # Iterate over each line and extract x and y values
#             for line in lines:
#                 x, y = line.strip().split(',')
#                 # Convert the x and y values to integers
#                 x = int(float(x))
#                 y = int(float(y))
#                 # Draw a white circle at the (x, y) position on the image
#                 cv2.circle(img, (x, y), radius=2, color=255, thickness=-1)

#         # Save the image as a new file with a name that includes the original filename
#         filename = os.path.splitext(file)[0]
#         cv2.imwrite(f'{filename}_image.png', img)



import os, cv2, random, shutil
import numpy as np


# Source path
source = "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/images/Test1Data"
# Destination path
dest =  "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/annotate_test1"


labels_path = "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/labels/Test1Data"

for root,_,files in os.walk(source):
    if files:
        
        for file in files:
            # Finding the class name
            class_name =  os.path.splitext(os.path.basename(file))[0]
            print(class_name)
            img = cv2.imread(os.path.join(root,file))
            # print(class_name)
            with open(f'{os.path.join(labels_path,class_name)}.txt', 'r') as f:
            # Read all lines in the file
                lines = f.readlines()
                # Iterate over each line and extract x and y values
                i = 0
                for line in lines:
                    x, y = line.strip().split(',')
                    # Convert the x and y values to integers
                    x = int(float(x))
                    y = int(float(y))
                    # Draw a white circle at the (x, y) position on the image
                    cv2.circle(img, (x, y), radius=1, color=(0, 0, 255), thickness=-1)
                    cv2.putText(img, f'{i}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
                    i =i +1

            # Save the image as a new file with a name that includes the original filename
            # filename = os.path.splitext(file)[0]
            cv2.imwrite(f'{dest}/{class_name}.png', img)