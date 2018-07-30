## @file Input.py
#  @brief Library module that loads and verifies values.
#  @date 07/25/2018

import Constants as Con
from GlassTypeADT import GlassTypeT
from ThicknessADT import ThicknessT

class Input:

    a = 0.0
    b = 0.0
    g = GlassTypeT("AN")
    Pbtol = 0.0
    SDx = 0.0
    SDy = 0.0
    SDz = 0.0
    t = ThicknessT(2.5)
    TNT = 0.0
    w = 0.0
    
    m = 0.0
    k = 0.0
    E = 0.0
    td = 0.0
    LSF = 0.0

    LDF = 0.0
    h = 0.0
    GTF = 0.0
    SD = 0.0
    AR = 0.0

    ## @brief Loads values from input file, Constraints.py, and calculations
    #  @param s filename
    def load_params ( s ):
        inputFile = open(s, "r")
        text = inputFile.readline()
        # length and width of glass slab
        Input.a = float(inputFile.readline())
        Input.b = float(inputFile.readline())
        text = inputFile.readline()
        # glass type
        Input.g = GlassTypeT(inputFile.readline().rstrip())
        text = inputFile.readline()
        # tolerable probability
        Input.Pbtol = float(inputFile.readline())
        text = inputFile.readline()
        # stand off distance coordinates
        Input.SDx = float(inputFile.readline())
        Input.SDy = float(inputFile.readline())
        Input.SDz = float(inputFile.readline())
        text = inputFile.readline()
        # thickness of glass slab
        Input.t = ThicknessT(float(inputFile.readline()))
        text = inputFile.readline()
        # TNT equivalent factor
        Input.TNT = float(inputFile.readline())
        text = inputFile.readline()
        # weight of Charge
        Input.w = float(inputFile.readline())   
        inputFile.close()

        Input.m = Con.m
        Input.k = Con.k
        Input.E = Con.E
        Input.td = Con.td
        Input.LSF = Con.LSF

        Input.LDF = pow(Input.td / 60.0, Input.m / 16.0)
        Input.h = Input.t.toMinThick()
        Input.GTF = Input.g.GTF()
        Input.SD = pow(pow(Input.SDx, 2) + pow(Input.SDy, 2) + pow(Input.SDz, 2), 0.5)
        Input.AR = Input.a / Input.b
        Input.verify_params()

    ## @brief Loads values from input file, Constraints.py, and calculations
    def verify_params ( ):
        if Input.a <= 0:
            raise ValueError("a must be positive")
        if Input.AR < 1.0:
            raise ValueError("a must be greater than or equal to b")
        if Input.a < Con.dmin or Input.a > Con.dmax:
            raise ValueError("a too large or small")
        if Input.AR > Con.ARmax:
            raise ValueError("allowable aspect ratio exceeded")
        if Input.b <= 0:
            raise ValueError("b must be positive")
        if Input.b < Con.dmin or Input.b > Con.dmax:
            raise ValueError("b too large or small")
        if Input.Pbtol <= 0 or Input.Pbtol >= 1:
            raise ValueError("Pbtol must be between 0 and 1")
        if Input.w <= 0:
            raise ValueError("charge weight (w) must be greater than zero")
        if Input.w < Con.wmin or Input.w > Con.wmax:
            raise ValueError("charge weight (w) is too small or too large")
        if Input.TNT <= 0:
            raise ValueError("TNT must be positive")
        if Input.SD <= 0:
            raise ValueError("stand off distance (SD) must be positive")
        if Input.SD < Con.SDmin or Input.SD > Con.SDmax:
            raise ValueError("stand off distance (SD) is too small or too large")
