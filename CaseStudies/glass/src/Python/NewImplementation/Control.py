## @file Control.py
#  @brief Implements the control for GlassBR
#  @date 07/30/2018

import Calc
import LoadASTM
import Input
import Output

class Control:

    # exported constants
    sTSD = "TSD.txt"
    sSDF = "SDF.txt"
    sIn  = "TestFiles/defaultInputFile.txt"
    sOut = "TestFiles/GenOutput.txt"

    def main(  ):

        # state variables
        Control.cTSD = LoadASTM.LoadTSD(Control.sTSD)
        Control.cSDF = LoadASTM.LoadSDF(Control.sSDF)
        Input.Input.load_params(Control.sIn)
        Control.q = Control.cTSD.eval(Input.Input.SD, Input.Input.w * Input.Input.TNT)
        Control.q_hat = Calc.calc_q_hat(Control.q, Input.Input)
        Control.Jtol = Calc.calc_J_tol(Input.Input)
        Control.J = Control.cSDF.evaly(Input.Input.AR, Control.q_hat)
        Control.q_hattol = Control.cSDF.eval(Input.Input.AR, Control.Jtol)
        Control.B = Calc.calc_B(Control.J, Input.Input)
        Control.Pb = Calc.calc_Pb(Control.B)
        Control.NFL = Calc.calc_NFL(Control.q_hattol, Input.Input)
        Control.LR = Calc.calc_LR(Control.NFL, Input.Input)

        Control.is_safePb = Calc.calc_is_safePb(Control.Pb, Input.Input)
        Control.is_safeLR = Calc.calc_is_safeLR(Control.LR, Control.q)

        Output.Output(Control.sOut, Input.Input, Control.is_safePb, Control.is_safeLR, Control.Pb, Control.B, Control.LR, Control.q, Control.J, Control.Jtol, Control.NFL, Control.q_hat, Control.q_hattol)

        print("Main has been executed and the results have been written to " + str(Control.sOut))

Control.main()
