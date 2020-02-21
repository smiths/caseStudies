#include "Calculations.hpp"

#include <vector>

#include "boost/numeric/odeint.hpp"
#include "InputParameters.hpp"
#include "NoPCMODE.hpp"

using std::vector;

vector<double> func_T_W(InputParameters inParams) {
  NoPCMODE ode = NoPCMODE(inParams.T_C, inParams.tau_W);
  vector<double> T_W;
  vector<double> init {inParams.T_init};
  boost::numeric::odeint::runge_kutta_dopri5<vector<double>> rk = boost::numeric::odeint::runge_kutta_dopri5<vector<double>>();
  auto stepper = boost::numeric::odeint::make_controlled(inParams.A_tol, inParams.R_tol, rk);
  boost::numeric::odeint::integrate_const(stepper, ode, init, 0.0, inParams.t_final, inParams.t_step, Populate_T_W(T_W));

  return T_W;
}