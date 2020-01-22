#ifndef NoPCMODE_h
#define NoPCMODE_h

#include <vector>

#include "InputParameters.hpp"

using std::vector;

class NoPCMODE {
  public: 
    vector<double> T_W;

    NoPCMODE(double T_C, double tau_W);
    void operator()(vector<double> T_W , vector<double> &dT_Wdt , double t);
  
  private:
    double tau_W;
    double T_C;
};

class Populate_T_W {
  public:
    vector<double> &T_W;

    Populate_T_W(vector<double> &T_W);

    void operator() (vector<double> &T_W, double t);
};

#endif