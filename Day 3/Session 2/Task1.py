#Task: Using Sobel Method, detect the edges of any image.

import cv2 as cv                       # Import OpenCV (aliased as cv) for image processing
import numpy as np                     # Import NumPy for numerical and array operations

img = cv.imread(r"scenery.jpeg", cv.IMREAD_GRAYSCALE)
# Read the image in grayscale mode from the specified file path

blur = cv.GaussianBlur(img, (9, 9), 1.5)
# Apply Gaussian blur to reduce noise before edge detection
# (9, 9) is the kernel size, 1.5 is the standard deviation

sx = cv.Sobel(blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=3)
# Compute the Sobel gradient in the x-direction

sy = cv.Sobel(blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=3)
# Compute the Sobel gradient in the y-direction

mag = np.hypot(sx, sy)
# Compute gradient magnitude using sqrt(sx^2 + sy^2)

mag = mag / mag.max() * 255
# Normalize gradient magnitude to the range [0, 255]

mag = mag.astype(np.uint8)
# Convert gradient magnitude image to unsigned 8-bit format

abs_sx = np.absolute(sx)
abs_sy = np.absolute(sy)
# Take absolute values of Sobel gradients

abs_sx = (abs_sx / abs_sx.max() * 255).astype(np.uint8)
abs_sy = (abs_sy / abs_sy.max() * 255).astype(np.uint8)
# Normalize absolute Sobel gradients to [0, 255] and convert to uint8

cv.namedWindow("orig", cv.WINDOW_NORMAL)
# Create a resizable window for the original image

cv.imshow("orig", img)                 # Display the original grayscale image
cv.imshow("Sobel X (abs)", abs_sx)      # Display absolute Sobel X gradient
cv.imshow("Sobel Y (abs)", abs_sy)      # Display absolute Sobel Y gradient
cv.imshow("Gradient magnitude", mag)    # Display gradient magnitude image

cv.waitKey(0)                          # Wait indefinitely until a key is pressed
cv.destroyAllWindows()                 # Close all OpenCV windows