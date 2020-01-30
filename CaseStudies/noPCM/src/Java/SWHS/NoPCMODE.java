package SWHS;

import org.apache.commons.math3.ode.FirstOrderDifferentialEquations;

public class NoPCMODE implements FirstOrderDifferentialEquations {
  private double tau_W;
  private double T_C;

  public NoPCMODE (InputParameters inParams) {
    this.tau_W = inParams.tau_W;
    this.T_C = inParams.T_C;
  }

  public int getDimension() {
    return 1;
  }

  public void computeDerivatives(double t, double[] T_W, double[] dT_W) {
    dT_W[0] = (1.0 / tau_W) * (T_C - T_W[0]);
  }
}