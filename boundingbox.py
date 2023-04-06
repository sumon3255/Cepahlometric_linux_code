import cv2

# Load image
img = cv2.imread('/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/Separate_patches/Train/Images/patch_1/001_patch_1.jpg')

x, y = 100, 200
cv2.circle(img, (x,y), radius=2, color=(0, 0, 255), thickness=5)

# Show image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()