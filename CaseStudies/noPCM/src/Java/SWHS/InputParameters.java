package SWHS;

/** \file InputParameters.java
    \author Thulasi Jegatheesan, Brooks MacLachlan
    \brief Provides the structure for holding input values, the function for reading inputs, and the function for checking the physical constraints and software constraints on the input
*/
import java.util.Arrays;
import java.util.BitSet;
import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.File;
import java.util.ArrayList;

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
    public static final double L_min = 0.1;
    public static final double L_max = 50;
    public static final double rho_W_min = 950;
    public static final double rho_W_max = 1000;
    public static final double A_C_max = 100000;
    public static final double C_W_min = 4170;
    public static final double C_W_max = 4210;
    public static final double h_C_min = 10;
    public static final double h_C_max = 10000;
    public static final double t_final_max = 86400;
    public static final double AR_min = 1.0e-2;
    public static final double AR_max = 100;
    
    /** \brief Reads input from a file with the given file name
        \param inParams structure holding the input values
        \param filename name of the input file
    */
    public static void get_input(InputParameters inParams, String filename) throws Exception {
        Scanner infile;
        infile = new Scanner(new File(filename));
        infile.nextLine();
        inParams.A_C = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.C_W = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.h_C = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.T_init = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.t_final = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.L = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.T_C = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.t_step = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.rho_W = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.D = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.A_tol = Double.parseDouble(infile.nextLine());
        infile.nextLine();
        inParams.R_tol = Double.parseDouble(infile.nextLine());
        infile.close();
    }
    
    /** \brief Verifies that input values satisfy the physical constraints and software constraints
        \param inParams structure holding the input values
    */
    public static void input_constraints(InputParameters inParams) throws Exception {
        if (!(inParams.A_C <= InputParameters.A_C_max)) {
            System.out.print("Warning: ");
            System.out.print("A_C has value ");
            System.out.print(inParams.A_C);
            System.out.print(" but suggested to be ");
            System.out.print("below ");
            System.out.print(InputParameters.A_C_max);
            System.out.print(" (A_C_max)");
            System.out.println(".");
        }
        if (!(InputParameters.C_W_min < inParams.C_W && inParams.C_W < InputParameters.C_W_max)) {
            System.out.print("Warning: ");
            System.out.print("C_W has value ");
            System.out.print(inParams.C_W);
            System.out.print(" but suggested to be ");
            System.out.print("between ");
            System.out.print(InputParameters.C_W_min);
            System.out.print(" (C_W_min)");
            System.out.print(" and ");
            System.out.print(InputParameters.C_W_max);
            System.out.print(" (C_W_max)");
            System.out.println(".");
        }
        if (!(InputParameters.h_C_min <= inParams.h_C && inParams.h_C <= InputParameters.h_C_max)) {
            System.out.print("Warning: ");
            System.out.print("h_C has value ");
            System.out.print(inParams.h_C);
            System.out.print(" but suggested to be ");
            System.out.print("between ");
            System.out.print(InputParameters.h_C_min);
            System.out.print(" (h_C_min)");
            System.out.print(" and ");
            System.out.print(InputParameters.h_C_max);
            System.out.print(" (h_C_max)");
            System.out.println(".");
        }
        if (!(inParams.t_final < InputParameters.t_final_max)) {
            System.out.print("Warning: ");
            System.out.print("t_final has value ");
            System.out.print(inParams.t_final);
            System.out.print(" but suggested to be ");
            System.out.print("below ");
            System.out.print(InputParameters.t_final_max);
            System.out.print(" (t_final_max)");
            System.out.println(".");
        }
        if (!(InputParameters.L_min <= inParams.L && inParams.L <= InputParameters.L_max)) {
            System.out.print("Warning: ");
            System.out.print("L has value ");
            System.out.print(inParams.L);
            System.out.print(" but suggested to be ");
            System.out.print("between ");
            System.out.print(InputParameters.L_min);
            System.out.print(" (L_min)");
            System.out.print(" and ");
            System.out.print(InputParameters.L_max);
            System.out.print(" (L_max)");
            System.out.println(".");
        }
        if (!(InputParameters.rho_W_min < inParams.rho_W && inParams.rho_W <= InputParameters.rho_W_max)) {
            System.out.print("Warning: ");
            System.out.print("rho_W has value ");
            System.out.print(inParams.rho_W);
            System.out.print(" but suggested to be ");
            System.out.print("between ");
            System.out.print(InputParameters.rho_W_min);
            System.out.print(" (rho_W_min)");
            System.out.print(" and ");
            System.out.print(InputParameters.rho_W_max);
            System.out.print(" (rho_W_max)");
            System.out.println(".");
        }
        if (!(InputParameters.AR_min <= inParams.D && inParams.D <= InputParameters.AR_max)) {
            System.out.print("Warning: ");
            System.out.print("D has value ");
            System.out.print(inParams.D);
            System.out.print(" but suggested to be ");
            System.out.print("between ");
            System.out.print(InputParameters.AR_min);
            System.out.print(" (AR_min)");
            System.out.print(" and ");
            System.out.print(InputParameters.AR_max);
            System.out.print(" (AR_max)");
            System.out.println(".");
        }
        
        if (!(inParams.A_C > 0)) {
            System.out.print("Warning: ");
            System.out.print("A_C has value ");
            System.out.print(inParams.A_C);
            System.out.print(" but suggested to be ");
            System.out.print("above ");
            System.out.print(0);
            System.out.println(".");
        }
        if (!(inParams.C_W > 0)) {
            System.out.print("Warning: ");
            System.out.print("C_W has value ");
            System.out.print(inParams.C_W);
            System.out.print(" but suggested to be ");
            System.out.print("above ");
            System.out.print(0);
            System.out.println(".");
        }
        if (!(inParams.h_C > 0)) {
            System.out.print("Warning: ");
            System.out.print("h_C has value ");
            System.out.print(inParams.h_C);
            System.out.print(" but suggested to be ");
            System.out.print("above ");
            System.out.print(0);
            System.out.println(".");
        }
        if (!(0 < inParams.T_init && inParams.T_init < 100)) {
            System.out.print("Warning: ");
            System.out.print("T_init has value ");
            System.out.print(inParams.T_init);
            System.out.print(" but suggested to be ");
            System.out.print("between ");
            System.out.print(0);
            System.out.print(" and ");
            System.out.print(100);
            System.out.println(".");
        }
        if (!(inParams.t_final > 0)) {
            System.out.print("Warning: ");
            System.out.print("t_final has value ");
            System.out.print(inParams.t_final);
            System.out.print(" but suggested to be ");
            System.out.print("above ");
            System.out.print(0);
            System.out.println(".");
        }
        if (!(inParams.L > 0)) {
            System.out.print("Warning: ");
            System.out.print("L has value ");
            System.out.print(inParams.L);
            System.out.print(" but suggested to be ");
            System.out.print("above ");
            System.out.print(0);
            System.out.println(".");
        }
        if (!(0 < inParams.T_C && inParams.T_C < 100)) {
            System.out.print("Warning: ");
            System.out.print("T_C has value ");
            System.out.print(inParams.T_C);
            System.out.print(" but suggested to be ");
            System.out.print("between ");
            System.out.print(0);
            System.out.print(" and ");
            System.out.print(100);
            System.out.println(".");
        }
        if (!(0 < inParams.t_step && inParams.t_step < inParams.t_final)) {
            System.out.print("Warning: ");
            System.out.print("t_step has value ");
            System.out.print(inParams.t_step);
            System.out.print(" but suggested to be ");
            System.out.print("between ");
            System.out.print(0);
            System.out.print(" and ");
            System.out.print(inParams.t_final);
            System.out.print(" (t_final)");
            System.out.println(".");
        }
        if (!(inParams.rho_W > 0)) {
            System.out.print("Warning: ");
            System.out.print("rho_W has value ");
            System.out.print(inParams.rho_W);
            System.out.print(" but suggested to be ");
            System.out.print("above ");
            System.out.print(0);
            System.out.println(".");
        }
        if (!(inParams.D > 0)) {
            System.out.print("Warning: ");
            System.out.print("D has value ");
            System.out.print(inParams.D);
            System.out.print(" but suggested to be ");
            System.out.print("above ");
            System.out.print(0);
            System.out.println(".");
        }
    }

    public static void derived_values(InputParameters inParams) {
        inParams.V_t = Math.PI * Math.pow(inParams.D / 2, 2) * inParams.L;

        inParams.M_W = inParams.rho_W * inParams.V_t;

        inParams.tau_W = (inParams.M_W * inParams.C_W) / (inParams.h_C * inParams.A_C);
    }
}
