package SWHS;

/** \file Control.java
    \author Thulasi Jegatheesan
    \brief Controls the flow of the program
*/
import java.util.Arrays;
import java.util.BitSet;
import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.File;
import java.util.ArrayList;

public class Control {
    
    /** \brief Controls the flow of the program
        \param args List of command-line arguments
    */
    public static void main(String[] args) throws Exception {
        String filename = args[0];
        InputParameters inParams = new InputParameters();
        InputParameters.get_input(inParams, filename);
        InputParameters.derived_values(inParams);
        InputParameters.input_constraints(inParams);
        ArrayList<Double> T_W = Calculations.func_T_W(inParams);
        OutputFormat.write_output(T_W);
    }
}
