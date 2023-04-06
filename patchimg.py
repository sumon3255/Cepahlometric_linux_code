import cv2
import numpy as np

# Load the cephalometric image
img = cv2.imread("/home/sumon/CepahloMetric/Dataset_v2/Maindatset/all_photos/001.jpg")

# Load the landmark coordinates from the txt file
with open("/home/sumon/CepahloMetric/Dataset_v2/Maindatset/TrainingLabels/001.txt") as f:
    landmarks = np.array([list(map(float, line.strip().split(","))) for line in f])

# Define the patch size (assumed to be square)
patch_size = 64

# Define the stride for the sliding window
stride = int(patch_size / 2)

# Open the output file for writing the recalculated xy coordinates
output_file = open("/home/sumon/CepahloMetric/Dataset_v2/patchlabels/patch_xy.txt", "w")

# Loop through the landmark coordinates and extract patches
for i, (x, y) in enumerate(landmarks):
    # Calculate the patch coordinates
    x1 = int(x - patch_size / 2)
    y1 = int(y - patch_size / 2)
    x2 = int(x + patch_size / 2)
    y2 = int(y + patch_size / 2)

    # Crop the patch from the image
    patch = img[y1:y2, x1:x2]

    # Save the patch to disk
    cv2.imwrite(f"/home/sumon/CepahloMetric/Dataset_v2/patchimg/patch_{i}.jpg", patch)

    # Recalculate the xy coordinates relative to the patch
    new_x = patch_size / 2
    new_y = patch_size / 2

    # Write the recalculated xy coordinates to the output file
    output_file.write(f"{new_x},{new_y}\n")

# Close the output file
output_file.close()
    # Save the patch to disk
    
