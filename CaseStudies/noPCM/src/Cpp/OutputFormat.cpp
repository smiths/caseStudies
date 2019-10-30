#include "OutputFormat.hpp"

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

void write_output(vector<double> T_W) {
    ofstream outputfile;
    outputfile.open("output.txt", std::fstream::out);
    outputfile << "T_W = [";
    for (int list_i1 = 0; list_i1 < (int)(T_W.size()) - 1; list_i1++) {
        outputfile << T_W.at(list_i1);
        outputfile << ", ";
    }
    if ((int)(T_W.size()) > 0) {
        outputfile << T_W.at((int)(T_W.size()) - 1);
    }
    outputfile << "]" << std::endl;
    outputfile.close();
}
