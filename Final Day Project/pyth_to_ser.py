import serial                          #Import serial module for serial communication
import time                            #Import time module for delays
   
ser = serial.Serial('COM12', 9600, timeout=1)
#Initialize serial communication on COM12 with baud rate 9600 and 1 second timeout

time.sleep(2)
#Wait for 2 seconds to allow the serial connection (e.g., Arduino) to initialize

try:
    while True:                        # Infinite loop to keep sending data
        ser.write(("2,4,8" + '\n').encode('utf-8'))
        #Send the string "2,4,8" followed by a newline over serial

except KeyboardInterrupt:
    ser.close()
    #Close the serial connection when the program is interrupted