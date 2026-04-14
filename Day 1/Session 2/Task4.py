#Task: Write a code for a simple Pacman program of the ball opening and closing its mouth with keyboard input

import cv2                              # Import OpenCV for image creation and display
import numpy as np                      # Import NumPy for array operations
import keyboard as kb                   # Import keyboard module to detect key presses

i = 0                                   # Angle control variable for animation
j = 1                                   # Direction control variable for angle increment/decrement

vel = 3                                 # Velocity of movement in pixels

x, y = 25, 25                           # Initial position of the ellipse

while True:                             # Main infinite loop
    while (kb.is_pressed("right")):     # While the right arrow key is pressed
        img = np.full((500, 500, 3), (0, 0, 0), dtype=np.uint8)
        # Create a black background

        cv2.ellipse(img, (x, y), (15, 15), 0, i, 360 - i, (255, 0, 0), -1)
        # Draw a filled blue ellipse facing right with animated arc angles

        cv2.imshow("Image1", img)       # Display the image
        cv2.waitKey(5)                  # Short delay for smooth animation

        i += j                          # Update animation angle
        if (x < 482):
            x += vel                    # Move ellipse to the right

        if (i == 44 or i == -44 or i == 0):
            j = -j                      # Reverse angle animation direction

    while (kb.is_pressed("down")):      # While the down arrow key is pressed
        img = np.full((500, 500, 3), (0, 0, 0), dtype=np.uint8)

        cv2.ellipse(img, (x, y), (15, 15), 90, i, 360 - i, (255, 0, 0), -1)
        # Draw a filled ellipse rotated downward

        cv2.imshow("Image1", img)
        cv2.waitKey(5)

        i += j
        if (y < 482):
            y += vel                    # Move ellipse downward

        if (i == 44 or i == -44 or i == 0):
            j = -j

    while (kb.is_pressed("left")):      # While the left arrow key is pressed
        img = np.full((500, 500, 3), (0, 0, 0), dtype=np.uint8)

        cv2.ellipse(img, (x, y), (15, 15), 180, i, 360 - i, (255, 0, 0), -1)
        # Draw a filled ellipse rotated to the left

        cv2.imshow("Image1", img)
        cv2.waitKey(5)

        i += j
        if (x > 18):
            x -= vel                    # Move ellipse to the left

        if (i == 44 or i == -44 or i == 0):
            j = -j

    while (kb.is_pressed("up")):        # While the up arrow key is pressed
        img = np.full((500, 500, 3), (0, 0, 0), dtype=np.uint8)

        cv2.ellipse(img, (x, y), (15, 15), 270, i, 360 - i, (255, 0, 0), -1)
        # Draw a filled ellipse rotated upward

        cv2.imshow("Image1", img)
        cv2.waitKey(5)

        i += j
        if (y > 18):
            y -= vel                    # Move ellipse upward

        if (i == 44 or i == -44 or i == 0):
            j = -j

    if (kb.is_pressed("ctrl")):
        break                           # Exit the program if Ctrl key is pressed

    img = np.full((500, 500, 3), (0, 0, 0), dtype=np.uint8)
    # Draw idle frame when no arrow key is pressed

    cv2.ellipse(img, (x, y), (15, 15), 0, i, 360 - i, (255, 0, 0), -1)
    # Draw ellipse in the current position

    cv2.imshow("Image1", img)
    cv2.waitKey(5)

    i += j                              # Continue idle animation
    if (i == 44 or i == -44 or i == 0):
        j = -j                          # Reverse animation direction if limits reached

cv2.destroyAllWindows()                 # Close all OpenCV windows