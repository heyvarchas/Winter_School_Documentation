============================================================
PROJECT TITLE: Background Removal via K-Means
Author: Varchas Jasti
Date: [March 2026]
============================================================

1. PROJECT OVERVIEW
-------------------
This project contains a single file containing python code to remove background from an image and include a virtual background using K-Means Clustering.
The program detects the background (mostly uniform) in the original image (largest cluster), and removes it to create a mask layer, followed by inclusion of an alternate background image leading to the formation of virtual background.

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
3. Navigate to this project folder named "Task 3"
4. Install dependencies using command:
	pip install -		(or equivalent terminal command)
	if any of the required modules are not installed

4. HOW TO RUN
-------------
After checking that you are inside the right project directory named "Task 3" on terminal/command prompt, type the command:
	> python task3.py 	(or equivalent terminal command)
in order to run the program.

5. BASIC USAGE
--------------
Once the program runs, the background is automatically separated from original image and new image with virtual background is displayed.
There is no user interaction involved in the usage of this program.
However, if the user wants to try the program with images other than those in this folder, the directions to do so are as follows:
1. Replace the "img.jpg" file in this folder with the new image for which background intends to be removed. It is preferred that the image must have a roughly uniform background. Note that the image HAS to be of JPEG format and MUST be named "img" ONLY.
2. Replace the "bg.jpg" file in this folder with the new image that intends to be used as a virtual background. Note that the image HAS to be of JPEG format and MUST be named "bg" ONLY.
3. Run the code as instructed in "HOW TO RUN" section above, to see the desired image.

6. CONTACT / SUPPORT
--------------------
For queries, contact: [jastivarchas@gmail.com/25MA10065]
============================================================