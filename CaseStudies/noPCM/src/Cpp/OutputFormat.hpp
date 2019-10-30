/** \file OutputFormat.hpp
    \author Thulasi Jegatheesan
    \brief Provides the function for writing outputs
*/
#ifndef OutputFormat_h
#define OutputFormat_h

#include <string>
#include <vector>

using std::string;
using std::vector;
using std::ifstream;
using std::ofstream;

/** \brief Writes the output values to output.txt
    \param inParams structure holding the input values
*/
void write_output(vector<double> T_W);

#endif
