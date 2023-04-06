from PIL import Image
import os

# Set the paths for the input and output folders
input_folder = '/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/Images/patch_0/images'
output_folder = '/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/resize_images/images'

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open the image and resize it
        image = Image.open(os.path.join(input_folder, filename))
        image = image.resize((256, 256))
        
        # Save the resized image to the output folder
        output_path = os.path.join(output_folder, filename)
        image.save(output_path)
