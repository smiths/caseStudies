## @file Input.py
#  @brief Library module that loads and verifies values.
#  @date 07/25/2018

import Constants as Con
from GlassTypeADT import GlassTypeT
from ThicknessADT import ThicknessT

class Input:

    def __init__ ( self ):
        self.a = 0.0
        self.b = 0.0
        self.g = "AN"
        self.Pbtol = 0.0
        self.SDx = 0.0
        self.SDy = 0.0
        self.SDz = 0.0
        self.t = 2.5
        self.TNT = 0.0
        self.w = 0.0
        
        self.m = 0.0
        self.k = 0.0
        self.E = 0.0
        self.td = 0.0
        self.LSF = 0.0

        self.LDF = 0.0
        self.h = 0.0
        self.GTF = 0.0
        self.SD = 0.0
        self.AR = 0.0

    ## @brief Loads values from input file, Constraints.py, and calculations
    #  @param s filename
    def load_params ( self, s ):
        inputFile = open(s, "r")
        text = inputFile.readline()
        # length and width of glass slab
        self.a = float(inputFile.readline())
        self.b = float(inputFile.readline())
        text = inputFile.readline()
        # glass type
        self.g = GlassTypeT(inputFile.readline().rstrip())
        text = inputFile.readline()
        # tolerable probability
        self.Pbtol = float(inputFile.readline())
        text = inputFile.readline()
        # stand off distance coordinates
        self.SDx = float(inputFile.readline())
        self.SDy = float(inputFile.readline())
        self.SDz = float(inputFile.readline())
        text = inputFile.readline()
        # thickness of glass slab
        self.t = ThicknessT(float(inputFile.readline()))
        text = inputFile.readline()
        # TNT equivalent factor
        self.TNT = float(inputFile.readline())
        text = inputFile.readline()
        # weight of Charge
        self.w = float(inputFile.readline())   
        inputFile.close()

        self.m = Con.m
        self.k = Con.k
        self.E = Con.E
        self.td = Con.td
        self.LSF = Con.LSF

        self.LDF = pow(self.td / 60, self.m / 16)
        self.h = self.t.toMinThick()
        self.GTF = self.g.GTF()
        self.SD = pow(pow(self.SDx, 2) + pow(self.SDy, 2) + pow(self.SDz, 2), 0.5)
        self.AR = self.a / self.b
        self.verify_params()

    ## @brief Loads values from input file, Constraints.py, and calculations
    def verify_params ( self ):
        if self.a <= 0:
            raise ValueError("a must be positive")
        if self.AR < 1.0:
            raise ValueError("a must be greater than or equal to b")
        if self.a < Con.dmin or self.a > Con.dmax:
            raise ValueError("a too large or small")
        if self.AR > Con.ARmax:
            raise ValueError("allowable aspect ratio exceeded")
        if self.b <= 0:
            raise ValueError("b must be positive")
        if self.b < Con.dmin or self.b > Con.dmax:
            raise ValueError("b too large or small")
        if self.Pbtol <= 0 or self.Pbtol >= 1:
            raise ValueError("Pbtol must be between 0 and 1")
        if self.w <= 0:
            raise ValueError("charge weight (w) must be greater than zero")
        if self.w < Con.wmin or self.w > Con.wmax:
            raise ValueError("charge weight (w) is too small or too large")
        if self.TNT <= 0:
            raise ValueError("TNT must be positive")
        if self.SD <= 0:
            raise ValueError("stand off distance (SD) must be positive")
        if self.SD < Con.SDmin or self.SD > Con.SDmax:
            raise ValueError("stand off distance (SD) is too small or too large")
