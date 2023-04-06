


import cv2

# Read the image
img = cv2.imread("/home/sumon/CepahloMetric/Dataset_v2/Maindatset/images/all_photos/302.jpg")
img_height, img_width = img.shape[:2]
# Read the YOLO format bounding box coordinates from the file
with open("/home/sumon/CepahloMetric/Dataset_v2/yolo/302.txt", "r") as f:
    boxes = f.readlines()

# Draw the bounding boxes on the image
for box in boxes:
    values = box.split()

    # Convert the values to floats
    yolo_format = list(map(float, values))
    x, y, w, h = yolo_format
    x_center = x * img_width
    y_center = y * img_height
    box_width = w * img_width
    box_height = h * img_height
    x_min = int(x_center - box_width / 2)
    y_min = int(y_center - box_height / 2)
    x_max = int(x_center + box_width / 2)
    y_max = int(y_center + box_height / 2)
        
    # x_min = int((x_center - width / 2) * img.shape[1])
    # y_min = int((y_center - height / 2) * img.shape[0])
    # x_max = int((x_center + width / 2) * img.shape[1])
    # y_max = int((y_center + height / 2) * img.shape[0])
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)

# show the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    # Draw the bounding box rectangle on the image
    # cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

# Display the image
# cv2.imshow("Image with bounding boxes", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
