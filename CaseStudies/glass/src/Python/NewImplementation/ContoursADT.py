## @file ContoursADT.py
#  @brief Implements an ADT for a contour
#  @date 07/26/2018

from Exceptions import *
from FunctADT import FuncT

class ContoursT :

    # exported constants
    MAX_ORDER = 2

    def __init__ ( self, i ):

        if (not(i in list(range(1, self.MAX_ORDER + 1)))):
             raise InvalidInterpOrder("Invalid interpretation error!")

        # state variables
        self.S = []
        self.Z = []
        self.o = i

    ## @brief Appends elements to state variable sequences
    def add( self, s, z ):
        if ((len(self.Z)) > 0) and (z < self.Z[-1]):
            raise IndepVarNotAscending("Independent variables not in ascending order!")
        self.S.append(s)
        self.Z.append(z)

    ## @brief Gets the ith element from the sequence S
    #  @return the ith element from S
    def getC( self, i ):
        if (not(0 <= i < len(self.S))):
            raise InvalidIndex("Index out of range")
        return self.S[i]

    ## @brief Evaluates the FuncT class with respect to input z
    #  @return the calculated FuncT class based on z
    def eval( self, x, z ):
        return (self.slice(x,False).eval(z))

    ## @brief Evaluates the FuncT class with respect to input y
    #  @return the calculated FuncT class based on y
    def evaly( self, x, y ):
        return (self.slice(x,True).eval(y))

    ## @brief Generates a FuncT class using the state variable sequences
    #  @return the generated FuncT class
    def slice( self, x, flip):
        Zdef = []
        F = []
        for i in range(len(self.S)):
            try:
                y = self.S[i].eval(x)
                Zdef.append(self.Z[i])
                F.append(y)
            except OutOfDomain:
                pass
        if Zdef:
            if flip:
                return FuncT(F, Zdef, o)
            else:
                return FuncT(Zdef, F, o)
        else:
            raise OutOfDomain("Out of domain!")