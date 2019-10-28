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
        InputParameters.input_constraints(inParams);
        double T_W = 40;
        double E_W = 0;
        OutputFormat.write_output(T_W, E_W);
    }
}
