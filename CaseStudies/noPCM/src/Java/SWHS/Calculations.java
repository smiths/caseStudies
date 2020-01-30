package SWHS;

import java.util.Arrays;
import java.util.ArrayList;
import org.apache.commons.math3.ode.nonstiff.AdamsBashforthIntegrator;

public class Calculations {
  public static ArrayList<Double> func_T_W(InputParameters inParams) {
    AdamsBashforthIntegrator it = new AdamsBashforthIntegrator(3, inParams.t_step, inParams.t_step, inParams.A_tol, inParams.R_tol);
    NoPCMODE ode = new NoPCMODE(inParams);
    double[] T_W_ode = new double[] {inParams.T_init};

    T_StepHandler stepHandler = new T_StepHandler();
    it.addStepHandler(stepHandler);
    it.integrate(ode, 0.0, T_W_ode, inParams.t_final, T_W_ode);

    return stepHandler.T_W;
  }
}