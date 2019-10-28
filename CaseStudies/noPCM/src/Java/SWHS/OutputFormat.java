package SWHS;

/** \file OutputFormat.java
    \author Thulasi Jegatheesan
    \brief Provides the function for writing outputs
*/
import java.util.Arrays;
import java.util.BitSet;
import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.File;
import java.util.ArrayList;

public class OutputFormat {
    
    /** \brief Writes the output values to output.txt
        \param inParams structure holding the input values
    */
    public static void write_output(ArrayList<Double> T_W) throws Exception {
        PrintWriter outputfile;
        outputfile = new PrintWriter(new FileWriter(new File("output.txt"), false));
        outputfile.print("T_W = ");
        outputfile.println(T_W);
        outputfile.close();
    }
}
