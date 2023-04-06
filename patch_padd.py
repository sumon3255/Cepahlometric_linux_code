import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("new.jpg")


with open("/home/sumon/CepahloMetric/Dataset_v2/Maindatset/TrainingLabels/012.txt") as f:
    landmarks = np.array([list(map(float, line.strip().split(","))) for line in f])


patch_size = 64


stride = int(patch_size / 2)

 


for i, (x, y) in enumerate(landmarks):

    x1 = int(x - patch_size / 2)
    y1 = int(y - patch_size / 2)
    x2 = int(x + patch_size / 2)
    y2 = int(y + patch_size / 2)
    # print(x,y)
    
    # new_x = patch_size / 2
    # new_y = patch_size / 2


    patch = img[y1:y2, x1:x2]
    
    new_x = patch.shape[1] / 2
    new_y = patch.shape[0] / 2
        
    x_gt = new_x + x - int(patch.shape[1] / 2)
    y_gt = new_y + y - int(patch.shape[0] / 2)
    print(x_gt,y_gt)


    if patch.shape[0] < patch_size or patch.shape[1] < patch_size:
        diff_y = patch_size - patch.shape[0]
        diff_x = patch_size - patch.shape[1]
        patch = cv2.copyMakeBorder(patch, 0, diff_y, 0, diff_x, cv2.BORDER_CONSTANT, value=(0,0,0))
        
   

    # Assume that (x_gt, y_gt) are the ground truth points in the original image
    
    
    # x_gt = new_x + x1 - int(patch.shape[1] / 2)
    # y_gt = new_y + y1 - int(patch.shape[0] / 2)

    # print(x_gt,y_gt)


    patch = cv2.circle(patch, (int(new_x), int(new_y)), 2, (0, 0, 255), -1)
    cv2.imwrite(f"/home/sumon/CepahloMetric/Dataset_v2/patchimg/patch_{i}.jpg", patch)

    # Recalculate the xy coordinates relative to the patch
    # new_x = x - x1 + int(patch_size / 2)
    # new_y = y - y1 + int(patch_size / 2)
    # Write the recalculated xy coordinates to the output file
    # output_file = open(f"/home/sumon/CepahloMetric/Dataset_v2/patchlabels/patch_{i}_xy.txt", "w")
    # output_file.write(f"{new_x},{new_y}\n")


output_file.close()
