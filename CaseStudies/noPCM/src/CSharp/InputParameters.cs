/** \file InputParameters.cs
    \author Thulasi Jegatheesan
    \brief Provides the structure for holding input values, the function for reading inputs, and the function for checking the physical constraints and software constraints on the input
*/
using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;

public class InputParameters {
    public double A_C;
    public double C_W;
    public double h_C;
    public double T_init;
    public double t_final;
    public double L;
    public double T_C;
    public double t_step;
    public double rho_W;
    public double D;
    public double A_tol;
    public double R_tol;
    public double V_t;
    public double M_W;
    public double tau_W;
    public const double L_min = 0.1;
    public const double L_max = 50;
    public const double rho_W_min = 950;
    public const double rho_W_max = 1000;
    public const double A_C_max = 100000;
    public const double C_W_min = 4170;
    public const double C_W_max = 4210;
    public const double h_C_min = 10;
    public const double h_C_max = 10000;
    public const double t_final_max = 86400;
    public const double AR_min = 1.0e-2;
    public const double AR_max = 100;
    
    /** \brief Reads input from a file with the given file name
        \param inParams structure holding the input values
        \param filename name of the input file
    */
    public static void get_input(InputParameters inParams, string filename) {
        StreamReader infile;
        infile = new StreamReader(filename);
        infile.ReadLine();
        inParams.A_C = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.C_W = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.h_C = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.T_init = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.t_final = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.L = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.T_C = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.t_step = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.rho_W = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.D = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.A_tol = Double.Parse(infile.ReadLine());
        infile.ReadLine();
        inParams.R_tol = Double.Parse(infile.ReadLine());
        infile.ReadLine();
    }
    
    /** \brief Verifies that input values satisfy the physical constraints and software constraints
        \param inParams structure holding the input values
    */
    public static void input_constraints(InputParameters inParams) {
        if (!(inParams.A_C <= InputParameters.A_C_max)) {
            Console.Write("Warning: ");
            Console.Write("A_C has value ");
            Console.Write(inParams.A_C);
            Console.Write(" but suggested to be ");
            Console.Write("below ");
            Console.Write(InputParameters.A_C_max);
            Console.Write(" (A_C_max)");
            Console.WriteLine(".");
        }
        if (!(InputParameters.C_W_min < inParams.C_W && inParams.C_W < InputParameters.C_W_max)) {
            Console.Write("Warning: ");
            Console.Write("C_W has value ");
            Console.Write(inParams.C_W);
            Console.Write(" but suggested to be ");
            Console.Write("between ");
            Console.Write(InputParameters.C_W_min);
            Console.Write(" (C_W_min)");
            Console.Write(" and ");
            Console.Write(InputParameters.C_W_max);
            Console.Write(" (C_W_max)");
            Console.WriteLine(".");
        }
        if (!(InputParameters.h_C_min <= inParams.h_C && inParams.h_C <= InputParameters.h_C_max)) {
            Console.Write("Warning: ");
            Console.Write("h_C has value ");
            Console.Write(inParams.h_C);
            Console.Write(" but suggested to be ");
            Console.Write("between ");
            Console.Write(InputParameters.h_C_min);
            Console.Write(" (h_C_min)");
            Console.Write(" and ");
            Console.Write(InputParameters.h_C_max);
            Console.Write(" (h_C_max)");
            Console.WriteLine(".");
        }
        if (!(inParams.t_final < InputParameters.t_final_max)) {
            Console.Write("Warning: ");
            Console.Write("t_final has value ");
            Console.Write(inParams.t_final);
            Console.Write(" but suggested to be ");
            Console.Write("below ");
            Console.Write(InputParameters.t_final_max);
            Console.Write(" (t_final_max)");
            Console.WriteLine(".");
        }
        if (!(InputParameters.L_min <= inParams.L && inParams.L <= InputParameters.L_max)) {
            Console.Write("Warning: ");
            Console.Write("L has value ");
            Console.Write(inParams.L);
            Console.Write(" but suggested to be ");
            Console.Write("between ");
            Console.Write(InputParameters.L_min);
            Console.Write(" (L_min)");
            Console.Write(" and ");
            Console.Write(InputParameters.L_max);
            Console.Write(" (L_max)");
            Console.WriteLine(".");
        }
        if (!(InputParameters.rho_W_min < inParams.rho_W && inParams.rho_W <= InputParameters.rho_W_max)) {
            Console.Write("Warning: ");
            Console.Write("rho_W has value ");
            Console.Write(inParams.rho_W);
            Console.Write(" but suggested to be ");
            Console.Write("between ");
            Console.Write(InputParameters.rho_W_min);
            Console.Write(" (rho_W_min)");
            Console.Write(" and ");
            Console.Write(InputParameters.rho_W_max);
            Console.Write(" (rho_W_max)");
            Console.WriteLine(".");
        }
        if (!(InputParameters.AR_min <= inParams.D && inParams.D <= InputParameters.AR_max)) {
            Console.Write("Warning: ");
            Console.Write("D has value ");
            Console.Write(inParams.D);
            Console.Write(" but suggested to be ");
            Console.Write("between ");
            Console.Write(InputParameters.AR_min);
            Console.Write(" (AR_min)");
            Console.Write(" and ");
            Console.Write(InputParameters.AR_max);
            Console.Write(" (AR_max)");
            Console.WriteLine(".");
        }
        
        if (!(inParams.A_C > 0)) {
            Console.Write("Warning: ");
            Console.Write("A_C has value ");
            Console.Write(inParams.A_C);
            Console.Write(" but suggested to be ");
            Console.Write("above ");
            Console.Write(0);
            Console.WriteLine(".");
        }
        if (!(inParams.C_W > 0)) {
            Console.Write("Warning: ");
            Console.Write("C_W has value ");
            Console.Write(inParams.C_W);
            Console.Write(" but suggested to be ");
            Console.Write("above ");
            Console.Write(0);
            Console.WriteLine(".");
        }
        if (!(inParams.h_C > 0)) {
            Console.Write("Warning: ");
            Console.Write("h_C has value ");
            Console.Write(inParams.h_C);
            Console.Write(" but suggested to be ");
            Console.Write("above ");
            Console.Write(0);
            Console.WriteLine(".");
        }
        if (!(0 < inParams.T_init && inParams.T_init < 100)) {
            Console.Write("Warning: ");
            Console.Write("T_init has value ");
            Console.Write(inParams.T_init);
            Console.Write(" but suggested to be ");
            Console.Write("between ");
            Console.Write(0);
            Console.Write(" and ");
            Console.Write(100);
            Console.WriteLine(".");
        }
        if (!(inParams.t_final > 0)) {
            Console.Write("Warning: ");
            Console.Write("t_final has value ");
            Console.Write(inParams.t_final);
            Console.Write(" but suggested to be ");
            Console.Write("above ");
            Console.Write(0);
            Console.WriteLine(".");
        }
        if (!(inParams.L > 0)) {
            Console.Write("Warning: ");
            Console.Write("L has value ");
            Console.Write(inParams.L);
            Console.Write(" but suggested to be ");
            Console.Write("above ");
            Console.Write(0);
            Console.WriteLine(".");
        }
        if (!(0 < inParams.T_C && inParams.T_C < 100)) {
            Console.Write("Warning: ");
            Console.Write("T_C has value ");
            Console.Write(inParams.T_C);
            Console.Write(" but suggested to be ");
            Console.Write("between ");
            Console.Write(0);
            Console.Write(" and ");
            Console.Write(100);
            Console.WriteLine(".");
        }
        if (!(0 < inParams.t_step && inParams.t_step < inParams.t_final)) {
            Console.Write("Warning: ");
            Console.Write("t_step has value ");
            Console.Write(inParams.t_step);
            Console.Write(" but suggested to be ");
            Console.Write("between ");
            Console.Write(0);
            Console.Write(" and ");
            Console.Write(inParams.t_final);
            Console.Write(" (t_final)");
            Console.WriteLine(".");
        }
        if (!(inParams.rho_W > 0)) {
            Console.Write("Warning: ");
            Console.Write("rho_W has value ");
            Console.Write(inParams.rho_W);
            Console.Write(" but suggested to be ");
            Console.Write("above ");
            Console.Write(0);
            Console.WriteLine(".");
        }
        if (!(inParams.D > 0)) {
            Console.Write("Warning: ");
            Console.Write("D has value ");
            Console.Write(inParams.D);
            Console.Write(" but suggested to be ");
            Console.Write("above ");
            Console.Write(0);
            Console.WriteLine(".");
        }
    }

    public static void derived_values(InputParameters inParams) {
        inParams.V_t = Math.PI * Math.Pow(inParams.D / 2, 2) * inParams.L;

        inParams.M_W = inParams.rho_W * inParams.V_t;

        inParams.tau_W = (inParams.M_W * inParams.C_W) / (inParams.h_C * inParams.A_C);
    }
}
