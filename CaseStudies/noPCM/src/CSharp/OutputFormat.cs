/** \file OutputFormat.cs
    \author Thulasi Jegatheesan
    \brief Provides the function for writing outputs
*/
using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;

public class OutputFormat {
    
    /** \brief Writes the output values to output.txt
        \param inParams structure holding the input values
    */
    public static void write_output(List<double> T_W) {
        StreamWriter outputfile;
        outputfile = new StreamWriter("output.txt", false);
        outputfile.WriteLine("T_W =");
        foreach (double temp in T_W) {
            outputfile.WriteLine(temp);
        }
        outputfile.Close();
    }
}
