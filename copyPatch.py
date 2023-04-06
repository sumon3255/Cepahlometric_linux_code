## For images

import os
import shutil

source_folder = '/home/sumon/CepahloMetric/Dataset_v2/Maindatset/refernceTest/ref_test1'
dest_folder = '/home/sumon/CepahloMetric/Dataset_v2/Maindatset/refernceTest/separate/Test1/labels'

if not  os.path.exists(dest_folder):
    os.makedirs(dest_folder)
for root,_,files in os.walk(source_folder):
    if files:
        for file in files:

            # if 'patch_1_' in file and file.endswith('.jpg'):
            if '_patch_0_xy.txt' in file:
                # print(file)
                src_path = os.path.join(root, file)
                # dest_path = os.path.join(root, file)
                shutil.copy(src_path, dest_folder)



## For txt
# import os
# import shutil

# source_folder = '/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/Test2_images'
# dest_folder = '/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/Separate_patches/Test2/labels/patch_3'

# if not  os.path.exists(dest_folder):
#     os.makedirs(dest_folder)

# for root,_,files in os.walk(source_folder):
#     if files:
#         for file in files:

#             # if 'patch_0' in file and file.endswith('.txt'):
#             if '_patch_3_xy.txt' in file:
#                 # print(file)
#                 src_path = os.path.join(root, file)
#                 # dest_path = os.path.join(root, file)
#                 shutil.copy(src_path, dest_folder)
