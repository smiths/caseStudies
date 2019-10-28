package SWHS;

import org.apache.commons.math3.ode.*;
import org.apache.commons.math3.ode.nonstiff.EulerIntegrator;

public class Calculations {
  public static double func_T_W(InputParameters inParams) {
    FirstOrderIntegrator it = new EulerIntegrator(inParams.t_step);
    FirstOrderDifferentialEquations ode = new NoPCMODE(inParams);
    double[] T_W = new double[] {inParams.T_init};
    it.integrate(ode, 0.0, T_W, inParams.t_final, T_W);

    return T_W[0];
  }
}