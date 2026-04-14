============================================================
PROJECT TITLE: Path Planning on IIT Kharagpur's Map [RRT* Infused TSP]
Author: Varchas Jasti
Date: [March 2026]
============================================================

1. PROJECT OVERVIEW
-------------------
This project contains a single file containing python code for the implementation of RRT* algorithm to find the shortest path passing through multiple points on the IIT Kharagpur Map. It is called the Travelling Salesman Problem (TSP).
The user can click any number of points on the map displayed to them, and the shortest path traced using the algorithm is displayed to the user, rendered pair-wise.

2. PREREQUISITES
----------------
Before running the script, ensure you have:
* Python version: 3.7+
* Required Modules: OpenCV, NumPy, Random, Math, InterTools
* Other tools: Visual Studio Code, Terminal/Command Prompt Access

3. INSTALLATION & SETUP
-----------------------
1. Extract the project folder.
2. Open your terminal/command prompt.
3. Navigate to this project folder named "Task 2"
4. Install dependencies using command:
	pip install -		(or equivalent terminal command)
	if any of the required modules are not installed

4. HOW TO RUN
-------------
After checking that you are inside the right project directory named "Task 2" on terminal/command prompt, type the command:
	> python task2.py 	(or equivalent terminal command)
in order to run the program.

5. BASIC USAGE
--------------
When the program begins to run, a map of the IIT Kharagpur Campus will be displayed to you.
Click on any number of points on the map one after another, making sure that the points being clicked are not coinciding with obstacles.
Note that if too many points are clicked, the processing takes time due to high amount of computation involved.
If the points clicked coincide with obstacles, the program does not register the point. It just displays a message on the terminal/command prompt that a point cannot be placed on an obstacle.
Once the points are clicked, the program begins finding the optimal path between the end points, passing through all other points, using their Euclidean coordinates, by implementing the RRT* algorithm along with utilisation of a cost matrix.
After the processing is done, the image is displayed again and the growth of the tree is rendered.
The rendering is not real time. The first render captures entirely the path between the first pair of points, then the second one the path between first two pairs, and so on.
Hence, the optimal path passing through all the points clicked is represented by the magenta line shown on the image displayed.

6. CONTACT / SUPPORT
--------------------
For queries, contact: [jastivarchas@gmail.com/25MA10065]
============================================================