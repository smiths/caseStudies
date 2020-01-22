#include "NoPCMODE.hpp"

#include <vector>

using std::vector;

NoPCMODE::NoPCMODE(double T_C, double tau_W) {
  this->T_C = T_C;
  this->tau_W = tau_W;
}

void NoPCMODE::operator()(vector<double> T_W , vector<double> &dT_Wdt , double t) {
  dT_Wdt.at(0) = (1/tau_W) * (T_C - T_W.at(0));
}

Populate_T_W::Populate_T_W(vector<double> &T_W) : T_W(T_W) {}

void Populate_T_W::operator() (vector<double> &T_W , double t) {
    this->T_W.push_back(T_W.at(0));
}