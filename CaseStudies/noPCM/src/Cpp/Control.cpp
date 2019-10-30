/** \file Control.cpp
    \author Thulasi Jegatheesan
    \brief Controls the flow of the program
*/
#define _USE_MATH_DEFINES
#include <algorithm>
#include <iostream>
#include <fstream>
#include <iterator>
#include <string>
#include <math.h>
#include <sstream>
#include <limits>
#include <vector>

using std::string;
using std::vector;
using std::ifstream;
using std::ofstream;

#include "InputParameters.hpp"
#include "OutputFormat.hpp"

/** \brief Controls the flow of the program
    \param argc Number of command-line arguments
    \param argv List of command-line arguments
    \return exit code
*/
int main(int argc, const char *argv[]) {
    string filename = argv[1];
    InputParameters inParams = InputParameters();
    get_input(inParams, filename);
    input_constraints(inParams);
    double T_W = 40;
    write_output(T_W);
    
    return 0;
}
