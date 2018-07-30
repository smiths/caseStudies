## @file LoadASTM.py
#  @brief Implements the ASTM of the load
#  @date 07/30/2018

from Input import *
from ThicknessADT import *
from GlassTypeADT import *
import io

def Output( s, params, is_safePb, is_safeLR, Pb, B, LR, q, J, Jtol, NFL, q̂, q̂tol):
    outputFile = io.open(s, "w", encoding="utf-8")
    outputFile.write("## From SRS R4;\n")

    outputFile.write("# From SRS R1:\n")
    outputFile.write("Plate length (long dimension):\na = " + repr(params.a))
    outputFile.write("\nPlate width (short dimension):\nb = " + repr(params.b))
    outputFile.write("\nGlass type g ∈ {AN,HS,FT}:\ng = " + repr(params.g.toString()))
    outputFile.write("\nTolerable probability:\nPbtol = " + repr(params.Pbtol))
    outputFile.write("\nStand off distance (x-component):\nSDx = " + repr(params.SDx))
    outputFile.write("\nStand off distance (y-component):\nSDy = " + repr(params.SDy))
    outputFile.write("\nStand off distance (z-component):\nSDz = " + repr(params.SDz))
    outputFile.write("\nNominal thickness of the glass slab")
    outputFile.write("\nt ∈ {2.5,2.7,3.0,4.0,5.0,6.0,8.0,10.0,12.0,16.0,19.0,22.0}: t = " + repr(params.t.toFloat()))
    outputFile.write("\nTNT equivalent factor\nTNT = " + repr(params.TNT))
    outputFile.write("\nCharge weight\nw = " + repr(params.w))

    outputFile.write("\n\n# From SRS R2:\n")
    outputFile.write("Surface flaw parameter:\nm = " + repr(params.m))
    outputFile.write("\nk = " + repr(params.k))
    outputFile.write("\nModulus of elasticity of glass:\nE = " + repr(params.E))
    outputFile.write("\nDuration of load:\ntd = " + repr(params.td))
    outputFile.write("\nLoad duration factor:\nLDF = " + repr(params.LDF))
    outputFile.write("\nLoad share factor:\nLSF = " + repr(params.LSF))
    outputFile.write("\nMinimum thickness:\nh = " + repr(params.h))
    outputFile.write("\nGlass type factor:\nGTF = " + repr(params.GTF))
    outputFile.write("\nstand off distance which is represented in coordinates (SDx,SDy,SDz):\nSD = " + repr(params.SD))
    outputFile.write("\nAspect ratio:\nAR = " + repr(params.AR))

    outputFile.write("\n\n## From SRS R5;\n")
    if is_safePb and is_safeLR:
        outputFile.write("For the given input parameters, the glass is considered safe")
    else:
        outputFile.write("For the given input parameters, the glass is NOT considered safe")

    outputFile.write("\n\n## From SRS R6;\n")
    outputFile.write("Probability of breakage:\nPb = " + str(Pb))
    outputFile.write("\nRisk function:\nB = " + str(B))
    outputFile.write("\nLoad resistance:\nLR = " + str(LR))
    outputFile.write("\nApplied load (demand):\nq = " + str(q))
    outputFile.write("\nStress distribution factor (Function):\nJ = " + str(J))
    outputFile.write("\nStress distribution factor (Function) based on Pbtol:\nJtol = " + str(Jtol))
    outputFile.write("\nNon-factored load:\nNFL = " + str(NFL))
    outputFile.write("\nDimensionless load:\nq̂ = " + str(q̂))
    outputFile.write("\nTolerable load:\nq̂tol = " + str(q̂tol))

    outputFile.close()
