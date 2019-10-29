/** \file Control.cs
    \author Thulasi Jegatheesan
    \brief Controls the flow of the program
*/
using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;

public class Control {
    
    /** \brief Controls the flow of the program
        \param args List of command-line arguments
    */
    public static void Main(string[] args) {
        string filename = args[0];
        InputParameters inParams = new InputParameters();
        InputParameters.get_input(inParams, filename);
        InputParameters.input_constraints(inParams);
        double T_W = 40;
        OutputFormat.write_output(T_W);
    }
}
