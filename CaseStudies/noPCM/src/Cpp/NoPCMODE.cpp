#include "NoPCMODE.hpp"

#include <iostream>
#include <vector>

#include "InputParameters.hpp"

using std::vector;

NoPCMODE::NoPCMODE(InputParameters inParams) {
  this->T_C = inParams.T_C;
  this->tau_W = inParams.tau_W;
}

void NoPCMODE::operator() (const double T_W , double &dT_Wdt , const double t) {
  dT_Wdt = (1/this->tau_W) * (this->T_C - T_W);
}

void NoPCMODE::populate_temp(const double &T_W_ode, const double t) {
  this->T_W.push_back(T_W_ode);
}

void write_cout( const double &x , const double t )
{
    std::cout << t << '\t' << x << std::endl;
}

Populate_T_W::Populate_T_W(vector<double> &T_W) : m_T_W(T_W) {};

void Populate_T_W::operator() (const double &T_W , double t) {
    this->m_T_W.push_back(T_W);
}