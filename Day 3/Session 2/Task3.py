#Task: Using Canny Edge Detection, detect edges of any image

import cv2                              # Import OpenCV for image processing

img = cv2.imread(r"scenery.jpeg", cv2.IMREAD_GRAYSCALE)
# Read the image from the specified file path in grayscale mode

img = cv2.resize(img, (732, 586))
# Resize the grayscale image to width = 732 pixels and height = 586 pixels

blurred = cv2.GaussianBlur(img, (5, 5), 1.4)
# Apply Gaussian blur to reduce noise before edge detection
# (5, 5) is the kernel size and 1.4 is the standard deviation

edges = cv2.Canny(blurred, 20, 100)
# Perform Canny edge detection
# 20 is the lower threshold and 100 is the upper threshold

cv2.imshow('Image', img)               # Display the original grayscale image
cv2.imshow('Canny Edges', edges)       # Display the detected edges

cv2.waitKey(0)                         # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()                # Close all OpenCV windows