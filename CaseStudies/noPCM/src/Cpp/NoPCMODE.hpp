#ifndef NoPCMODE_h
#define NoPCMODE_h

#include <vector>

#include "InputParameters.hpp"

using std::vector;

class NoPCMODE {
  public: 
    vector<double> T_W;

    NoPCMODE(InputParameters inParams);
    void operator() (const double T_W , double &dT_Wdt , const double t);
    void populate_temp(const double &T_W, const double t);
  
  private:
    double tau_W;
    double T_C;
};

void write_cout( const double &x , const double t );

class Populate_T_W {
  public:
    vector<double>& m_T_W;

    Populate_T_W(vector<double> &T_W);

    void operator() (const double &T_W, double t);
};

#endif