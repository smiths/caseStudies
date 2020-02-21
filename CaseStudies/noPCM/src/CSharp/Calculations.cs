using System.Collections.Generic;
using System.Linq;
using Microsoft.Research.Oslo;

public class Calculations {
    public static List<double> func_T_W(InputParameters inParams) {
        Vector f(double t, Vector T_W) {
          return new Vector((1/inParams.tau_W) * (inParams.T_C - T_W[0]));
        }

        Options opts = new Options();
        opts.AbsoluteTolerance = inParams.A_tol;
        opts.RelativeTolerance = inParams.R_tol;

        IEnumerable<SolPoint> sol = Ode.GearBDF(
            0, 
            new Vector(inParams.T_init), 
            f,
            opts);

        IEnumerable<SolPoint> pts = sol.SolveFromToStep(0, inParams.t_final, inParams.t_step);

        List<double> T_W = new List<double>();
        foreach (SolPoint sp in pts) {
          T_W.Add(sp.X[0]);
        }

        return T_W;
    }
}