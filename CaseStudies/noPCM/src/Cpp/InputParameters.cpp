#include "InputParameters.hpp"

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

const double InputParameters::L_min = 0.1;
const double InputParameters::L_max = 50;
const double InputParameters::rho_W_min = 950;
const double InputParameters::rho_W_max = 1000;
const double InputParameters::A_C_max = 100000;
const double InputParameters::C_W_min = 4170;
const double InputParameters::C_W_max = 4210;
const double InputParameters::h_C_min = 10;
const double InputParameters::h_C_max = 10000;
const double InputParameters::t_final_max = 86400;
const double InputParameters::AR_min = 1.0e-2;
const double InputParameters::AR_max = 100;

void get_input(InputParameters &inParams, string filename) {
    ifstream infile;
    infile.open(filename, std::fstream::in);
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.A_C;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.C_W;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.h_C;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.T_init;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.t_final;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.L;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.T_C;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.t_step;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.rho_W;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.D;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.A_tol;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile >> inParams.R_tol;
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    infile.close();
}

void input_constraints(InputParameters &inParams) {
    if (!(inParams.A_C <= InputParameters::A_C_max)) {
        std::cout << "Warning: ";
        std::cout << "A_C has value ";
        std::cout << inParams.A_C;
        std::cout << " but suggested to be ";
        std::cout << "below ";
        std::cout << InputParameters::A_C_max;
        std::cout << " (A_C_max)";
        std::cout << "." << std::endl;
    }
    if (!(InputParameters::C_W_min < inParams.C_W && inParams.C_W < InputParameters::C_W_max)) {
        std::cout << "Warning: ";
        std::cout << "C_W has value ";
        std::cout << inParams.C_W;
        std::cout << " but suggested to be ";
        std::cout << "between ";
        std::cout << InputParameters::C_W_min;
        std::cout << " (C_W_min)";
        std::cout << " and ";
        std::cout << InputParameters::C_W_max;
        std::cout << " (C_W_max)";
        std::cout << "." << std::endl;
    }
    if (!(InputParameters::h_C_min <= inParams.h_C && inParams.h_C <= InputParameters::h_C_max)) {
        std::cout << "Warning: ";
        std::cout << "h_C has value ";
        std::cout << inParams.h_C;
        std::cout << " but suggested to be ";
        std::cout << "between ";
        std::cout << InputParameters::h_C_min;
        std::cout << " (h_C_min)";
        std::cout << " and ";
        std::cout << InputParameters::h_C_max;
        std::cout << " (h_C_max)";
        std::cout << "." << std::endl;
    }
    if (!(inParams.t_final < InputParameters::t_final_max)) {
        std::cout << "Warning: ";
        std::cout << "t_final has value ";
        std::cout << inParams.t_final;
        std::cout << " but suggested to be ";
        std::cout << "below ";
        std::cout << InputParameters::t_final_max;
        std::cout << " (t_final_max)";
        std::cout << "." << std::endl;
    }
    if (!(InputParameters::L_min <= inParams.L && inParams.L <= InputParameters::L_max)) {
        std::cout << "Warning: ";
        std::cout << "L has value ";
        std::cout << inParams.L;
        std::cout << " but suggested to be ";
        std::cout << "between ";
        std::cout << InputParameters::L_min;
        std::cout << " (L_min)";
        std::cout << " and ";
        std::cout << InputParameters::L_max;
        std::cout << " (L_max)";
        std::cout << "." << std::endl;
    }
    if (!(InputParameters::rho_W_min < inParams.rho_W && inParams.rho_W <= InputParameters::rho_W_max)) {
        std::cout << "Warning: ";
        std::cout << "rho_W has value ";
        std::cout << inParams.rho_W;
        std::cout << " but suggested to be ";
        std::cout << "between ";
        std::cout << InputParameters::rho_W_min;
        std::cout << " (rho_W_min)";
        std::cout << " and ";
        std::cout << InputParameters::rho_W_max;
        std::cout << " (rho_W_max)";
        std::cout << "." << std::endl;
    }
    if (!(InputParameters::AR_min <= inParams.D && inParams.D <= InputParameters::AR_max)) {
        std::cout << "Warning: ";
        std::cout << "D has value ";
        std::cout << inParams.D;
        std::cout << " but suggested to be ";
        std::cout << "between ";
        std::cout << InputParameters::AR_min;
        std::cout << " (AR_min)";
        std::cout << " and ";
        std::cout << InputParameters::AR_max;
        std::cout << " (AR_max)";
        std::cout << "." << std::endl;
    }
    
    if (!(inParams.A_C > 0)) {
        std::cout << "Warning: ";
        std::cout << "A_C has value ";
        std::cout << inParams.A_C;
        std::cout << " but suggested to be ";
        std::cout << "above ";
        std::cout << 0;
        std::cout << "." << std::endl;
    }
    if (!(inParams.C_W > 0)) {
        std::cout << "Warning: ";
        std::cout << "C_W has value ";
        std::cout << inParams.C_W;
        std::cout << " but suggested to be ";
        std::cout << "above ";
        std::cout << 0;
        std::cout << "." << std::endl;
    }
    if (!(inParams.h_C > 0)) {
        std::cout << "Warning: ";
        std::cout << "h_C has value ";
        std::cout << inParams.h_C;
        std::cout << " but suggested to be ";
        std::cout << "above ";
        std::cout << 0;
        std::cout << "." << std::endl;
    }
    if (!(0 < inParams.T_init && inParams.T_init < 100)) {
        std::cout << "Warning: ";
        std::cout << "T_init has value ";
        std::cout << inParams.T_init;
        std::cout << " but suggested to be ";
        std::cout << "between ";
        std::cout << 0;
        std::cout << " and ";
        std::cout << 100;
        std::cout << "." << std::endl;
    }
    if (!(inParams.t_final > 0)) {
        std::cout << "Warning: ";
        std::cout << "t_final has value ";
        std::cout << inParams.t_final;
        std::cout << " but suggested to be ";
        std::cout << "above ";
        std::cout << 0;
        std::cout << "." << std::endl;
    }
    if (!(inParams.L > 0)) {
        std::cout << "Warning: ";
        std::cout << "L has value ";
        std::cout << inParams.L;
        std::cout << " but suggested to be ";
        std::cout << "above ";
        std::cout << 0;
        std::cout << "." << std::endl;
    }
    if (!(0 < inParams.T_C && inParams.T_C < 100)) {
        std::cout << "Warning: ";
        std::cout << "T_C has value ";
        std::cout << inParams.T_C;
        std::cout << " but suggested to be ";
        std::cout << "between ";
        std::cout << 0;
        std::cout << " and ";
        std::cout << 100;
        std::cout << "." << std::endl;
    }
    if (!(0 < inParams.t_step && inParams.t_step < inParams.t_final)) {
        std::cout << "Warning: ";
        std::cout << "t_step has value ";
        std::cout << inParams.t_step;
        std::cout << " but suggested to be ";
        std::cout << "between ";
        std::cout << 0;
        std::cout << " and ";
        std::cout << inParams.t_final;
        std::cout << " (t_final)";
        std::cout << "." << std::endl;
    }
    if (!(inParams.rho_W > 0)) {
        std::cout << "Warning: ";
        std::cout << "rho_W has value ";
        std::cout << inParams.rho_W;
        std::cout << " but suggested to be ";
        std::cout << "above ";
        std::cout << 0;
        std::cout << "." << std::endl;
    }
    if (!(inParams.D > 0)) {
        std::cout << "Warning: ";
        std::cout << "D has value ";
        std::cout << inParams.D;
        std::cout << " but suggested to be ";
        std::cout << "above ";
        std::cout << 0;
        std::cout << "." << std::endl;
    }
}

