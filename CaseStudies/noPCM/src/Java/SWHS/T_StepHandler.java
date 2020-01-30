package SWHS;

import java.util.Arrays;
import java.util.ArrayList;
import org.apache.commons.math3.ode.sampling.StepHandler;
import org.apache.commons.math3.ode.sampling.StepInterpolator;

public class T_StepHandler implements StepHandler {
  public ArrayList<Double> T_W;

  public void init(double t0, double[] y0, double t) {
    this.T_W = new ArrayList<Double>(Arrays.asList(y0[0]));
  }

  public void handleStep(StepInterpolator interpolator, boolean isLast) {
    double[] T_W_curr = interpolator.getInterpolatedState();
    this.T_W.add(T_W_curr[0]);
  }
}