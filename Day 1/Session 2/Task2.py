#Task: Write a code of a moving box in 2D, which bounces when hits the boundary of the canvas.

import cv2                              # Import OpenCV for image creation and display
import numpy as np                      # Import NumPy for array operations
import keyboard as kb                   # Import keyboard module to detect key presses

i = 0                                   # Initialize a variable (not used further in the code)
x1 = 10                                 # Top-left x-coordinate of the rectangle
y1 = 10                                 # Top-left y-coordinate of the rectangle
x2 = 50                                 # Bottom-right x-coordinate of the rectangle
y2 = 50                                 # Bottom-right y-coordinate of the rectangle
velx = 10                               # Velocity of the rectangle along the x-axis
vely = 5                                # Velocity of the rectangle along the y-axis

while True:                             # Infinite loop for animation
    img = np.full((500, 500, 3), (0, 0, 0), dtype=np.uint8)
    # Create a 500x500 black background image

    cv2.rectangle(img, (x1, y1), (x2, y2), 255, -1)
    # Draw a filled rectangle (color intensity 255) using the given coordinates

    cv2.imshow("Image1", img)           # Display the image in a window named "Image1"
    cv2.waitKey(50)                     # Wait for 50 milliseconds between frames

    x1 += velx                          # Update rectangle position along x-axis (left side)
    x2 += velx                          # Update rectangle position along x-axis (right side)
    y1 += vely                          # Update rectangle position along y-axis (top side)
    y2 += vely                          # Update rectangle position along y-axis (bottom side)

    if ((x1 + x2) / 2 > 470 or (x1 + x2) / 2 < 30):
        velx = -velx                    # Reverse x-direction velocity when hitting vertical boundaries

    if ((y1 + y2) / 2 > 470 or (y1 + y2) / 2 < 30):
        vely = -vely                    # Reverse y-direction velocity when hitting horizontal boundaries

    if (kb.is_pressed("ctrl")):
        break                           # Exit the loop when the Ctrl key is pressed

cv2.destroyAllWindows()                 # Close all OpenCV windows