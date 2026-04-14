============================================================
PROJECT TITLE: Path Planning on IIT Kharagpur's Map
Author: Varchas Jasti
Date: [March 2026]
============================================================

1. PROJECT OVERVIEW
-------------------
This project contains a single file containing python code for the implementation of RRT* algorithm to find the shortest path between any two given points on the IIT Kharagpur map.
The user can click any two points on the map displayed to them, and the shortest path traced using the algorithm is displayed to the user, rendered in real-time.

2. PREREQUISITES
----------------
Before running the script, ensure you have:
* Python version: 3.7+
* Required Modules: OpenCV, NumPy, Random, Math
* Other tools: Visual Studio Code, Terminal/Command Prompt Access

3. INSTALLATION & SETUP
-----------------------
1. Extract the project folder.
2. Open your terminal/command prompt.
3. Navigate to this project folder named "Task 1"
4. Install dependencies using command:
	pip install -		(or equivalent terminal command)
	if any of the required modules are not installed

4. HOW TO RUN
-------------
After checking that you are inside the right project directory named "Task 1" on terminal/command prompt, type the command:
	> python task1.py 	(or equivalent terminal command)
in order to run the program.

5. BASIC USAGE
--------------
When the program begins to run, a map of the IIT Kharagpur Campus will be displayed to you.
Click on any two points on the map one after another, making sure that the points being clicked are not coinciding with obstacles.
The coordinates of the points being stored are displayed on the terminal as the program is running.
If the points clicked coincide with obstacles, the program does not register the point. It gives a warning message on the terminal and allows you to click another point instead.
Once the points are clicked, the program begins finding the optimal path between the two points using their Euclidean coordinates, by implementing the RRT* algorithm.
After the processing is done, the number of iterations is displayed on the terminal. 
The image is displayed again and the growth of the tree is rendered in real-time.
Hence, the optimal path between the two points is represented by the red line shown on the image displayed.

6. CONTACT / SUPPORT
--------------------
For queries, contact: [jastivarchas@gmail.com/25MA10065]
============================================================