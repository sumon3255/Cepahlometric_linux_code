import albumentations as A
import cv2
import numpy as np
import os



# img_paths = r"H:\Cephalometric Project\CepahloMain\Datas and others\RawImage\Newlyupdated\resized\TrainingData" # replace with your own image paths
# label_path = r"H:\Cephalometric Project\CepahloMain\Datas and others\RawImage\Newlyupdated\labels\TrainingData"


img_paths = "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/TrainingData"# replace with your own image paths
label_path =  "/home/sumon/CepahloMetric/Dataset_v2/Maindatset/TrainingLabels"

dest_img_path =  "/home/sumon/CepahloMetric/Dataset_v2/Augment_v2/images"
dest_labels_path = "/home/sumon/CepahloMetric/Dataset_v2/Augment_v2/labels"




label_list = os.listdir(label_path)
labels = []

for label in label_list:
    with open(os.path.join(label_path, label)) as f:
        lines = f.readlines()
        data = []
        for line in lines:
            row = line.strip().split(',')
            if len(row) == 2:
                data.append([float(x) for x in row])
        if data:
            labels.append(np.array(data))



img_list = os.listdir(img_paths)
images = []
for path in img_list:
    img = cv2.imread(os.path.join(img_paths, path))
    images.append(img)





# transform = A.Compose([
#     A.HorizontalFlip(p=0.5),
#     A.RandomBrightnessContrast(p=0.2),
#     A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1, rotate_limit=45, p=0.5),
 
# ], keypoint_params=A.KeypointParams(format='xy', remove_invisible=False))

# transform = A.Compose([
#     A.HorizontalFlip(p=0.5),
#     A.RandomBrightnessContrast(p=0.2),
#     A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1, rotate_limit=45, p=0.5),
#     A.Blur(blur_limit=3, p=0.2),
#     A.GaussNoise(var_limit=(10, 50), p=0.2),
#     A.RGBShift(r_shift_limit=20, g_shift_limit=20, b_shift_limit=20, p=0.2),
#     A.CLAHE(clip_limit=4.0, tile_grid_size=(8,8), p=0.2),
#     A.RandomFog(fog_coef_lower=0.1, fog_coef_upper=0.3, p=0.2),
# ], keypoint_params=A.KeypointParams(format='xy', remove_invisible=False))

# transform = A.Compose([
#        A.RandomBrightnessContrast(p=0.5),
#     A.Rotate(limit=10, p=0.5),
#     A.HorizontalFlip(p=0.5),
#     A.Resize(height=512, width=512, p=0.5),
#     A.ShiftScaleRotate(shift_limit=0.2, p=0.5),
#     A.CoarseDropout(p=0.5),
 
# ], keypoint_params=A.KeypointParams(format='xy', remove_invisible=False))




# transform = A.Compose([

#     # A.Rotate(limit=30, p=1),
#     #  A.Rotate(limit=(-15, 15), p=1),

#     # A.RandomScale(scale_limit=(0.8, 1.1), p=1.0)
#      A.ShiftScaleRotate(shift_limit=0.0, scale_limit=0.0, rotate_limit=0.0, p=1.0)
#     #  A.ShiftScaleRotate(shift_limit=0.2, p=1, rotate_limit=0)
#     # A.VerticalFlip(p=1),
#     # A.HorizontalFlip(p=1),
#     # A.GaussNoise(var_limit=(10.0, 50.0), p=1),
#     # A.RandomBrightnessContrast(p=1, brightness_limit=(-0.3, 0.3), contrast_limit=0)
#     # A.RandomResizedCrop(height=512, width=512, scale=(0.5, 1.0), p=1)
 
# ], keypoint_params=A.KeypointParams(format='xy', remove_invisible=False))





transform = A.Compose([

 

    # A.RandomScale(scale_limit=(0.6), p=1), #0.8 to 1.1  # Alldone
    
    # A.GaussNoise(var_limit=(10.0, 50.0), p=1),
    # A.RandomBrightnessContrast(p=1),
    # A.RandomBrightnessContrast(p=1, brightness_limit=(-0.2, 0.2), contrast_limit=(-0.2, 0.2))
#     A.ShiftScaleRotate(
#     shift_limit=0.31, # maximum fraction of the image size to shift horizontally and vertically
#     p=1.0 # apply the transformation to all images


# )
    # A.ShiftScaleRotate(shift_limit=0.0, scale_limit=0.0, rotate_limit=0.0, p=1.0),
    #    A.RandomBrightnessContrast(p=1.0, brightness_limit=0.25, contrast_limit=0),
    A.RandomGamma(
    gamma_limit=(80, 120), # the range of gamma values to choose from
    p=1.0 # apply the transformation to all images
)

#  A.Rotate(limit=(-17, 17), p=1),
# A.HorizontalFlip(p=1),
], keypoint_params=A.KeypointParams(format='xy', remove_invisible=False))



# aug_images = []
# aug_labels = []
# for img, label in zip(images, labels):
#     for i in range(30):
#         aug_data = transform(image=img, keypoints=label)
#         aug_image = aug_data['image']
#         aug_label = aug_data['keypoints']
#         aug_images.append(aug_image)
#         aug_labels.append(aug_label)

aug_images = []
aug_labels = []
for img, label in zip(images, labels):
    
   
    
    # print(landmarks)
    h, w = img.shape[:2]
    h_min, w_min = np.min(label, axis=0)
    h_max, w_max = np.max(label, axis=0)
    # print( h_max, h_min)
    h_limit = (h - h_max, -h_min)
    w_limit = (w - w_max, -w_min)
    # print(h_limit,w_limit)

    # aug_data = transform(image=img, keypoints=label)
    # aug_data = transform(image=img, keypoints=label, keypoint_shift=h_limit + w_limit)
    aug_data = transform(image=img, keypoints=label)
    aug_image = aug_data['image']
    aug_label = aug_data['keypoints']
    aug_images.append(aug_image)
    aug_labels.append(aug_label)

# num = 0
# for i, (aug_img, aug_label) in enumerate(zip(aug_images, aug_labels)):
#     cv2.imwrite(f'{dest_img_path}/augmented_image{num}.jpg', aug_img)
#     np.savetxt(f'{dest_labels_path}/augmented_image{num}.txt', aug_label,fmt='%.0f', delimiter=',')
#     num = num+1

import uuid

for aug_img, aug_label in zip(aug_images, aug_labels):
    # Generate a unique identifier for the file
    file_id = uuid.uuid4().hex
    
    # Use the identifier to create filenames for the image and label
    img_filename = f'{dest_img_path}/augmented_image_{file_id}.jpg'
    label_filename = f'{dest_labels_path}/augmented_image_{file_id}.txt'
    
    # Save the image and label files with the generated filenames
    cv2.imwrite(img_filename, aug_img)
    np.savetxt(label_filename, aug_label, fmt='%.0f', delimiter=',')

