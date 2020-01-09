#include "Calculations.hpp"

#include <vector>

#include "boost/numeric/odeint.hpp"
#include "InputParameters.hpp"
#include "NoPCMODE.hpp"

using std::vector;
using namespace boost::numeric::odeint;

vector<double> func_T_W(InputParameters inParams) {
  NoPCMODE ode = NoPCMODE(inParams);
  vector<double> T_W;
  integrate_const(make_controlled(inParams.A_tol, inParams.R_tol, runge_kutta_dopri5<double>()), ode, inParams.T_init, 0.0, inParams.t_final, inParams.t_step, Populate_T_W(T_W));

  return T_W;
}