#Task: Take any Image and convert it from RGB to Black and White without using OpenCV

import cv2                              # Import OpenCV for image loading and processing
import numpy as np                      # Import NumPy for array creation and manipulation
import matplotlib.pyplot as plt         # Import Matplotlib for displaying images

img = cv2.imread(r"scenery.jpeg")
# Read the image from the specified file path (BGR format)

img = cv2.resize(img, (732, 586))
# Resize the image to width = 732 pixels and height = 586 pixels

img_new = np.full((586, 732), 0, dtype=np.uint8)
# Create a new single-channel image initialized with zeros

for i in range(586):                   # Loop over rows (height) of the image
    for j in range(732):               # Loop over columns (width) of the image
        img_new[i][j] = (img[i][j][0] + img[i][j][1] + img[i][j][2]) / 3
        # Convert each pixel to grayscale by averaging its B, G, and R values

        if (img_new[i][j] < 50):
            img_new[i][j] = 0           # Set pixel to black if below threshold
        else:
            img_new[i][j] = 1           # Set pixel to white (binary) if above threshold

plt.imshow(img_new, cmap='gray')       # Display the binary image using Matplotlib
plt.axis('off')                        # Turn off axis markings
plt.show()                             # Render the image window