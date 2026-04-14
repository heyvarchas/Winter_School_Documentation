#Task: Download a Greyscale image of a coin and find the threshold value above which you can see the circle around the coin

import cv2                              # Import OpenCV for image loading and processing
import numpy as np                      # Import NumPy (commonly used with image arrays)
import matplotlib.pyplot as plt         # Import Matplotlib for displaying images

img = cv2.imread(r"coin.jpg")
# Read the image from the specified file path using OpenCV

img = cv2.resize(img, (610, 616))
# Resize the image to width = 610 pixels and height = 616 pixels

ret, binary = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
# Apply binary thresholding:
# Pixel values greater than 50 are set to 255 (white),
# and values less than or equal to 50 are set to 0 (black)

plt.imshow(binary, cmap='gray')         # Display the thresholded image in grayscale
plt.axis('off')                         # Turn off axis markings
plt.show()                              # Render the image window