This implementation uses odeint from the C++ Boost libraries. The boost libraries can be downloaded here: https://www.boost.org/.

The program can be compiled with:

`g++ -o Control.exe -I path/to/boost/directory Control.cpp InputParameters.cpp NoPCMODE.cpp Calculations.cpp OutputFormat.cpp`

The program can then be run on the test input provided here with:\

`./Control.exe test.in`