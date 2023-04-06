import numpy as np
import cv2

# ...

def cv_size(img):
    return tuple(img.shape[1::-1])



img ="/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/Separate_patches/Train/images/patch_0_random/008_patch_0.jpg"

img = cv2.imread(img)

size  = cv_size(img)
print(size)