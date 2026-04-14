#Task: Write a code to show the projectile motion of a ball.

import cv2                               # Import OpenCV for displaying graphics
import numpy as np                       # Import NumPy for array creation and manipulation

width, height = 500, 500                 # Define the width and height of the window

x, y = 0, 450                            # Initial position of the projectile (starting near bottom-left)
vx = 4                                   # Horizontal velocity
vy = -12                                 # Initial vertical velocity (negative for upward motion)
gravity = 0.4                            # Constant acceleration due to gravity

while True:                              # Infinite loop to animate the motion
    frame = np.full((height, width, 3), (0, 0, 255), dtype=np.uint8)
    # Create a red background frame of given dimensions

    x += vx                              # Update horizontal position using horizontal velocity
    vy += gravity                        # Increase vertical velocity due to gravity
    y += vy                              # Update vertical position using vertical velocity

    cv2.circle(frame, (int(x), int(y)), 10, (255, 255, 255), -1)
    # Draw the projectile as a filled white circle at the current position

    cv2.imshow("Simple Projectile", frame)
    # Display the current frame in a window titled "Simple Projectile"

    if x > width or y > height:          # Check if the projectile has gone out of bounds
        x, y = 0, 450                    # Reset projectile to initial position
        vy = -12                         # Reset vertical velocity

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break                            # Exit the loop if the 'q' key is pressed

cv2.destroyAllWindows()                  # Close all OpenCV windows