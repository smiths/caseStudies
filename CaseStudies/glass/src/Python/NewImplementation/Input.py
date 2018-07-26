## @file Input.py
#  @brief Library module that loads and verifies values.
#  @date 07/25/2018

import Constants as Con
from GlassTypeADT import GlassTypeT
from ThicknessADT import ThicknessT

## @brief Loads values from input file, Constraints.py, and calculations
#  @param s filename
def load_params ( s ):
    infile = open(s, "r")
    text = infile.readline()
    # length and width of glass slab
    a = float(infile.readline())
    b = float(infile.readline())
    text = infile.readline()
    # glass type
    g = GlassTypeT(infile.readline().rstrip())
    text = infile.readline()
    # tolerable probability
    Pbtol = float(infile.readline())
    text = infile.readline()
    # stand off distance coordinates
    SDx = float(infile.readline())
    SDy = float(infile.readline())
    SDz = float(infile.readline())
    text = infile.readline()
    # thickness of glass slab
    t = ThicknessT(float(infile.readline()))
    text = infile.readline()
    # TNT equivalent factor
    TNT = float(infile.readline())
    text = infile.readline()
    # weight of Charge
    w = float(infile.readline())   
    infile.close()

    m, k, E, td, LSF = Con.m, Con.k, Con.E, Con.td, Con.LSF

    LDF = pow(td / 60, m / 16)
    h = t.toMinThick()
    GTF = g.GTF()
    SD = pow(pow(SDx, 2) + pow(SDy, 2) + pow(SDz, 2), 0.5)
    AR = a / b

## @brief Loads values from input file, Constraints.py, and calculations
def verify_params ( ):
    if a <= 0:
        raise ValueError("a must be positive")
    if AR < 1.0:
        raise ValueError("a must be greater than or equal to b")
    if a < Con.dmin or a > Con.dmax:
        raise ValueError("a too large or small")
    if AR > Con.ARmax:
        raise ValueError("allowable aspect ratio exceeded")
    if b <= 0:
        raise ValueError("b must be positive")
    if b < Con.dmin or b > Con.dmax:
        raise ValueError("b too large or small")
    if Pbtol <= 0 or Pbtol >= 1:
        raise ValueError("Pbtol must be between 0 and 1")
    if w <= 0:
        raise ValueError("charge weight (w) must be greater than zero")
    if w < Con.wmin or w > Con.wmax:
        raise ValueError("charge weight (w) is too small or too large")
    if TNT <= 0:
        raise ValueError("TNT must be positive")
    if SD <= 0:
        raise ValueError("stand off distance (SD) must be positive")
    if SD < Con.SDmin or SD > Con.SDmax:
        raise ValueError("stand off distance (SD) is too small or too large")
