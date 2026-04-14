#Task: Take any short Video and Resize it. Try drawing a circle over the region of interest or any other shape.

import numpy as np                      # Import NumPy (commonly used with image/video data)
import cv2 as cv                       # Import OpenCV (aliased as cv) for video processing
import keyboard as kb                  # Import keyboard module to detect key presses

cap = cv.VideoCapture(r"videoplayback.mp4")
# Create a VideoCapture object to read the video file from the given path

if not cap.isOpened():
    print("Cannot Open Camera")         # Print error message if video cannot be opened
    exit()                              # Exit the program

while True:                             # Loop to read and display video frames
    ret, frame = cap.read()             # Read one frame from the video
    if not ret:
        print("Can't receive frame (stream end?), Exiting ...")
        break                           # Exit loop if no frame is received (end of video)

    cv.ellipse(frame, (240, 180), (100, 100), 0, 0, 360, (0, 0, 0), 8)
    # Draw a black ellipse on the current video frame
    # Center: (240, 180), Axes: (100, 100), Full ellipse, Thickness: 8

    cv.imshow('frame', frame)           # Display the current frame in a window named 'frame'

    if cv.waitKey(1) == ord('q'):
        break                           # Exit loop if 'q' key is pressed in the OpenCV window

    if (kb.is_pressed('ctrl')):
        break                           # Exit loop if Ctrl key is pressed

cap.release()                           # Release the video capture object
cv.destroyAllWindows()                  # Close all OpenCV windows