import cv2 as cv                       # Import OpenCV for computer vision operations
import serial                          # Import serial for communication with external hardware
import time                            # Import time for delays and FPS calculation
import numpy as np                     # Import NumPy for numerical operations
import keyboard as kb                  # Import keyboard module for key press detection
import math                            # Import math for mathematical computations

coords = (x, y, z)                     # Tuple to store coordinates (x, y, z)

l1 = 9.2                               # Length of first arm segment
l2 = 9.8                               # Length of second arm segment

ser = serial.Serial(port='COM8', baudrate=9600, timeout=.1)
# Initialize serial communication on COM8 with baud rate 9600

time.sleep(2)                          # Wait for serial connection to stabilize

def Publish(x, y, z):
    try:
        theta0 = math.atan2(y, x)      # Base joint angle
        x = math.hypot(x, y)           # Project x onto horizontal plane
        r = math.hypot(x, z)           # Distance from arm base to target

        D = (r**2 - l1**2 - l2**2) / (2 * l1 * l2)
        # Cosine law for elbow angle

        if D > 1.0:
            D = 1.0
        elif D < -1.0:
            D = -1.0

        D = np.clip(D, -1, 1)          # Clamp D to valid range for acos

        dir = 1
        t = dir * math.sqrt(1 - D**2)
        theta2 = math.atan2(t, D)      # Elbow joint angle

        a = math.atan2(z, x)
        b = math.atan2(l2 * math.sin(theta2), l1 + l2 * math.cos(theta2))

        theta1 = a - b                 # Shoulder joint angle

        servo0 = np.clip(s0 + math.degrees(theta0), 0, 180)
        servo1 = np.clip(s1 + math.degrees(theta1), 0, 180)
        servo2 = np.clip(s2 + math.degrees(theta2), 0, 180)
        # Convert joint angles to servo angles and clamp to [0, 180]

        packet = f"{servo0}, {servo1}, {servo2}\n"
        # Format the data packet to send over serial

        ser.write(packet.encode('utf-8'))
        # Send packet to microcontroller

    except KeyboardInterrupt:
        ser.close()                    # Close serial connection on interrupt


wCam, hCam = 1200, 980                  # Camera resolution settings

cap = cv.VideoCapture(1)               # Open webcam with index 1
cFactor = 15.4 / 1780                  # Conversion factor from pixels to real-world units

cap.set(3, wCam)                       # Set camera width
cap.set(4, hCam)                       # Set camera height

pTime = 0                              # Initialize previous time for FPS calculation

while True:
    ret, img = cap.read()              # Capture a frame from the camera
    if not ret:
        break

    cTime = time.time()
    fps = 1 / (cTime - pTime + 1e-8)   # Compute FPS
    pTime = cTime

    img = cv.flip(img, 1)              # Flip the image horizontally

    cv.putText(
        img,
        f'FPS: {int(fps)}',
        (40, 70),
        cv.FONT_HERSHEY_COMPLEX,
        3,
        (255, 0, 255),
        3
    )
    # Display FPS on the image

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # Convert the image from BGR to HSV color space
    
    lower = np.array([95, 60, 50])     # Lower HSV bound for color detection
    upper = np.array([130, 255, 255])  # Upper HSV bound for color detection

    mask = cv.inRange(hsv, lower, upper)
    # Create a binary mask for the specified HSV range

    kernel = np.ones((5, 5), np.uint8)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    # Apply morphological operations to clean up the mask

    ys, xs = np.where(mask > 0)
    # Get coordinates of detected pixels

    if len(xs) > 0 and len(ys) > 0:
        cx_pix = xs.mean()             # X centroid in pixel coordinates
        cy_pix = ys.mean()             # Y centroid in pixel coordinates

        cx = cx_pix * cFactor * 2      # Convert to real-world X coordinate
        cy = cy_pix * cFactor * 2      # Convert to real-world Y coordinate

        xLen = len(xs)                 # Number of detected pixels

        k = 1
        c = 0

        if xLen != 0:
            cz = math.sqrt(k * 1080000 / (xLen - 1080000 * c)) * 2
            # Estimate Z coordinate based on object size
        else:
            cz = cy

        print(cx, cy, cz)              # Print computed coordinates
    else:
        print("no ball detected")      # No object detected

    cv.imshow("Img", img)              # Show original image
    cv.imshow("img2", mask)             # Show mask image

    if cv.waitKey(20) & 0xFF == 27:
        break                          # Exit loop on ESC key

    if kb.is_pressed('ctrl'):
        break                          # Exit loop on CTRL key press

cap.release()                          # Release camera
cv.destroyAllWindows()                 # Close all OpenCV windows