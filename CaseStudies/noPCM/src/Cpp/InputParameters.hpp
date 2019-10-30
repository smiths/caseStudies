/** \file InputParameters.hpp
    \author Thulasi Jegatheesan
    \brief Provides the structure for holding input values, the function for reading inputs, and the function for checking the physical constraints and software constraints on the input
*/
#ifndef InputParameters_h
#define InputParameters_h

#include <string>
#include <vector>

using std::string;
using std::vector;
using std::ifstream;
using std::ofstream;

/** \brief Structure for holding the input values and constant values
*/
class InputParameters {
    public:
        double A_C;
        double C_W;
        double h_C;
        double T_init;
        double t_final;
        double L;
        double T_C;
        double t_step;
        double rho_W;
        double D;
        double A_tol;
        double R_tol;
        double V_t;
        double M_W;
        double tau_W;
        static const double L_min;
        static const double L_max;
        static const double rho_W_min;
        static const double rho_W_max;
        static const double A_C_max;
        static const double C_W_min;
        static const double C_W_max;
        static const double h_C_min;
        static const double h_C_max;
        static const double t_final_max;
        static const double AR_min;
        static const double AR_max;
        
    
    private:
};

/** \brief Reads input from a file with the given file name
    \param inParams structure holding the input values
    \param filename name of the input file
*/
void get_input(InputParameters &inParams, string filename);

/** \brief Verifies that input values satisfy the physical constraints and software constraints
    \param inParams structure holding the input values
*/
void input_constraints(InputParameters &inParams);

void derived_values(InputParameters &inParams);

#endif
