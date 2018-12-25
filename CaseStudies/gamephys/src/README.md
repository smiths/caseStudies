This project contains the folders and files for the implementation of Tamias2D.

Tamias2D folder:
===============
Contains all the implementation files for all the modules in the library.

Test folder:
============
test_system.py contains all system tests and this uses output.py and plotter.py for results 
and graph display, this can be run by right clicking the file name and click run or click on the function name and click run(this eill run each test as required)

test_unit.py contain all the unit test cases for Tamias2D. 
To run unit test located in test_unit.py use: type pytest tests/test_unit.py in the terminal
Results of test will be displayed in the terminal.

example folder:
==============
The 'examples' folder contains sample codes that can be run by the user
Game.py gives a visual image of objects falling from space, user can modify the code to see the behaviour

The 'PlotDemo.py' is the simulation of 3 bodies colliding. The output result displays the history of their position, velocity and angular velocity over a period of time.


Additional file added during implementation/testing:
====================================================
*clock.py was implemented at a later stage in development, to track the time.Initially the time function in pygame was used to implement the time but Tamias2D now has its own clock function, it will be added to documentation at a future phase.

* output.py is used for outputting to the console and activating the plotter when the time is right. Plotting is handled in plotter.py and it displays the graphs based on the specified parameters e.g graph of position over time, velocity over time e.t.c. In output.py, an enumerator class is defined to make choosing what values to display easier. The enumerator is called Options. And can be used as a constant so no misspelling happens.
	
Class Options(Enum)
	POSITION = ‘’position”
	ROTATION = “rotation”
	VELOCITY = “velocity”
	ANGVEL = “angularVel”
	FORCE = “force”
	TORQUE = “torque”
	ACCEL = “accel”
	ANGACCEL = “angAccel”

The above is used alongside another class called OutputOptions, which contains a dictionary that has all the keys from the enumerators paired with a Boolean value. 

Class Options(Enum)
	Options.POSITION = “False”
	Options.ROTATION = “False”
	Options.VELOCITY = “False”
	Options.ANGVEL = “False”
	Options.FORCE = “False”
	Options.TORQUE = “False”
	Options.ACCEL = “False”
	Options.ANGACCEL = “False”
If you want any of the above values to be outputted for the test you’re executing, just enable it using the key. For example:
opt = OutputOptions()
opt.enable_option(Options.POSITION)
opt.enable_option(Options.VELOCITY)
output.options = opt