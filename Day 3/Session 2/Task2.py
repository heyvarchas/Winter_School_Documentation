#Task: Using Laplace Method, detect the edges of any image.

import cv2                              # Import OpenCV for image processing
import numpy as np                      # Import NumPy for numerical operations

img = cv2.imread(r"scenery.jpeg")
# Read the image from the specified file path

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert the image from BGR color space to grayscale

lap = cv2.Laplacian(gray, cv2.CV_64F)
# Apply the Laplacian operator to detect edges (second-order derivatives)

lap = np.uint8(np.absolute(lap))
# Take the absolute value of the Laplacian result and convert it to uint8 for display

cv2.imshow("Laplacian Edge Detection", lap)
# Display the Laplacian edge-detected image

cv2.waitKey(0)
# Wait indefinitely until a key is pressed

cv2.destroyAllWindows()
# Close all OpenCV windows