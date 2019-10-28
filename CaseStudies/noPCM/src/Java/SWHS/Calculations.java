package SWHS;

import java.util.Arrays;
import java.util.ArrayList;
import org.apache.commons.math3.ode.*;
import org.apache.commons.math3.ode.nonstiff.EulerIntegrator;
import org.apache.commons.math3.ode.sampling.StepHandler;
import org.apache.commons.math3.ode.sampling.StepInterpolator;

public class Calculations {
  public static ArrayList<Double> func_T_W(InputParameters inParams) {
    FirstOrderIntegrator it = new EulerIntegrator(inParams.t_step);
    FirstOrderDifferentialEquations ode = new NoPCMODE(inParams);
    double[] T_W_ode = new double[] {inParams.T_init};
    ArrayList<Double> T_W = new ArrayList<Double>(Arrays.asList(inParams.T_init));

    StepHandler stepHandler = new StepHandler() {
      public void init(double t0, double[] y0, double t) {
      }

      public void handleStep(StepInterpolator interpolator, boolean isLast) {
        double[] T_W_curr = interpolator.getInterpolatedState();
        T_W.add(T_W_curr[0]);
      }
    };
    it.addStepHandler(stepHandler);
    it.integrate(ode, 0.0, T_W_ode, inParams.t_final, T_W_ode);

    return T_W;
  }
}