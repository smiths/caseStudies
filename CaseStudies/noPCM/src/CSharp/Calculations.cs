using System.Collections.Generic;
using System.Linq;
using Microsoft.Research.Oslo;

public class Calculations {
    public static List<double> func_T_W(InputParameters inParams) {
        var sol = Ode.RK547M(
            0, 
            new Vector(inParams.T_init), 
            (t,T_W_ode) => new Vector((1/inParams.tau_W) * (inParams.T_C - T_W_ode[0])),
            new Options {
              AbsoluteTolerance = inParams.A_tol,
              RelativeTolerance = inParams.R_tol
            });
        
        var points = sol.SolveFromToStep(0, inParams.t_final, inParams.t_step).ToArray();

        List<double> T_W = new List<double>();
        foreach (var sp in points) {
          T_W.Add(sp.X);
        }

        return T_W;
    }
}