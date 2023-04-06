
import cv2

# Load the image
img = cv2.imread("/home/sumon/CepahloMetric/Dataset_v2/Maindatset/ref_2/151/151_patch_12.jpg")

# Define the x, y coordinates of the point to plot
x, y = 28,41

# Set the color and thickness of the point
color = (0, 0, 255)  # red
thickness = -1  # fill circle

# Plot the point on the image
cv2.circle(img, (x, y), radius=0, color=color, thickness=thickness)

# Display the image
cv2.imshow("Image with point", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
