#Task: Write a code with a ball bouncing as in task 2, with a static circle on the canvas, such that the canvas closes when the ball touches the circle.

import cv2                              # Import OpenCV for image processing and display
import numpy as np                      # Import NumPy for array creation and manipulation
import math                             # Import math module for mathematical operations
import keyboard as kb                   # Import keyboard module to detect key presses

velx = 10                               # Velocity along the x-axis
vely = 5                                # Velocity along the y-axis

x, y = 250, 250                         # Initial position of the moving object
h = 150                                 # Fixed reference point for distance calculation

while True:                             # Infinite loop for continuous animation
    img = np.full((500, 500, 3), (0, 0, 0), dtype=np.uint8)
    # Create a 500x500 black background image

    cv2.ellipse(img, (x, y), (30, 30), 0, 0, 360, (0, 0, 255), -1)
    # Draw a filled red circle (ellipse) representing the moving object

    cv2.ellipse(img, (h, h), (30, 30), 0, 0, 360, (255, 0, 0), 2)
    # Draw a blue outlined circle (ellipse) at a fixed position

    cv2.imshow("Image1", img)           # Display the current frame
    cv2.waitKey(50)                     # Wait for 50 milliseconds between frames

    x += velx                           # Update x-coordinate of the moving object
    y += vely                           # Update y-coordinate of the moving object

    if (x > 470 or x < 30):
        velx = -velx                    # Reverse x-direction when hitting vertical boundaries

    if (y > 470 or y < 30):
        vely = -vely                    # Reverse y-direction when hitting horizontal boundaries
    
    if (math.sqrt(((x - h) * (x - h)) + ((y - h) * (y - h))) < 60):
        break                           # Stop the loop if the moving object is close to the fixed object

    if (kb.is_pressed("ctrl")):
        break                           # Exit the loop when the Ctrl key is pressed

cv2.destroyAllWindows()                 # Close all OpenCV windows