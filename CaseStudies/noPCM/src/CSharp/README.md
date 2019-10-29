This implementation requires Oslo, an ODE solver than can be downloaded here: https://www.microsoft.com/en-us/research/project/open-solving-library-for-odes/#!downloads

Unfortunately, despite the User Guide implying it does, the Oslo download does not include the required .dll file, so you will need to build it yourself. The easiest way to do that is by opening the Oslo.sln file in Visual Studio and building the project. Then, copy the Microsoft.Research.Oslo.dll file into this directory.

With the set-up complete, the program can be compiled with:

`csc -r:Microsoft.Research.Oslo.dll Control.cs InputParameters.cs Calculations.cs OutputFormat.cs`

(Be sure you are using .NET version 4 or higher).

The program can be run on the test input provided here with:

`./Control.exe test.in`