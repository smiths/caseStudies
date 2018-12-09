# SSP Source Code

This folder contains the scripts for the reimplemented SSP.

To run the program, start matlab in this directory and call the control function with the input file name, including the extension. For example,

`control('ExampleInput.txt')`

In the input file, values on the same line must be separated by at least one space. The input file should be structured as follows:

- The first line should say the number of layers and the direction of soil movement (1 if left-to-right, 0 otherwise)

- The second line should say the number of vertices for the first (topmost) slope layer followed by the material properties for that layer, in this order: Effective angle of friction, effective cohesion, dry soil unit weight, saturated soil unit weight

- The coordinates of the first slope layer should be defined in the following lines, with one x-y pair per line.

- This layout is repeated for subsequent soil layers, if any exist.

- After all soil layers have been defined, the next line should say the number of vertices describing the water table. If there is no water table, this should be 0.

- If there is a water table, the next line should say the unit weight of water. If there is no water table, this line should not exist.

- The next lines should specify the coordinates of the water table in the same format as the coordinates of the slope layers. If there is no water table, these lines should not exist.

- The next line should give the minimum and maximum x values for the slip surface entry point

- The next line should give the minimum and maximum x values for the slip surface exit point

- The next line should give the minimum and maximum y values for the slip surface

- The next and final line should be 0 if it is desired to model f as a half-sine, or 1 if it is desired to model f as a constant 1 (see SRS for more information)

See ExampleInput.txt for an example of a valid input file. More examples can be found in the ssp/test/dataFiles/Valid_Input_Files directory.