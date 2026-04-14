============================================================
PROJECT TITLE: Background Removal via K-Means [Real-Time Virtual Background]
Author: Varchas Jasti
Date: [March 2026]
============================================================

1. PROJECT OVERVIEW
-------------------
This project contains a single file containing python code to remove background from real-time camera input and include a virtual background, using K-Means Clustering.
The program detects the background (mostly uniform) in the frame captured using camera, and removes it to create a mask layer, followed by inclusion of an alternate background image leading to the formation of virtual background.

2. PREREQUISITES
----------------
Before running the script, ensure you have:
* Python version: 3.10+
* Required Libraries: NumPy, OpenCV
* Other tools: Visual Studio Code, Terminal/Command Prompt Access

3. INSTALLATION & SETUP
-----------------------
1. Extract the project folder.
2. Open your terminal/command prompt.
3. Navigate to this project folder named "Task 4"
4. Install dependencies using command:
	pip install -		(or equivalent terminal command)
	if any of the required modules are not installed

4. HOW TO RUN
-------------
After checking that you are inside the right project directory named "Task 4" on terminal/command prompt, type the command:
	> python task4.py 	(or equivalent terminal command)
in order to run the program.

5. BASIC USAGE
--------------
Once the program begins to run, the frame is captured from the camera.
Note that the computer on which the code is running needs to have camera input. If camera is not recognized or frame isn't captured successfully, the code is aborted and the program ends with an error message on the terminal.
Once the frame is successfully captured, the background is removed and the new image with the virtual background is rendered in real-time.
Apart from the camera dependency, there is no user-interaction involved in the program.
However, if the user desires to change the virtual background, the following steps may be followed:
1. Replace the "bg.jpg" file in this folder with the new image that intends to be used as a virtual background. Note that the image HAS to be of JPEG format and MUST be named "bg" ONLY.
2. Run the code as instructed in "HOW TO RUN" section above, to see the desired output.
In order to end the program, click the letter 'Q' on the keyboard.

6. CONTACT / SUPPORT
--------------------
For queries, contact: [jastivarchas@gmail.com/25MA10065]
============================================================