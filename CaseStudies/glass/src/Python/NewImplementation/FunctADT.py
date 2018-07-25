## @file FunctADT.py
#  @brief Implements an ADT for a function
#  @date 07/25/2018

import pytest
from SeqServices import *
from Exceptions import *

## @brief An implementation for a CurveADT
class FuncT :

    # exported constants
    MAX_ORDER = 2

    def __init__ ( self , X , Y , i ):

        # raise any necessary exceptions
        if (not(isAscending(X))):
            raise IndepVarNotAscending("Independent variables are not in ascending order!")
        if (len(X) != len(Y)):
            raise SeqSizeMismatch("Sequences are not of the same length!")
        if (not(i in [1, self.MAX_ORDER])):
            raise InvalidInterpOrder("Invalid interpretation error!")
        if (len(X) < 3):
            raise TooFewDataPts("Sequence has too few data points")

        # state variables
        self.__X = X
        self.__Y = Y
        self.__minx = X[0]
        self.__maxx = X[len(X) - 1]
        self.__o = i

    ## @brief Gets the minimum independent variable value
    #  @return smallest x-value in CurveT instance
    def minD ( self ) :
        return self.__minx

    ## @brief Gets the maximum independent variable value
    #  @return largest x-value in CurveT instance
    def maxD ( self ) :
        return self.__maxx

    ## @brief Gets the order of the CurveT instance
    #  @return order of CurveT instance
    def order ( self ) :
        return self.__o

    def eval ( self, x ):
        if (not(self.__minx <= x <= self.__maxx)):
            raise OutOfDomain("Out of domain!")
        if (not(1 <= index(self.__X, x) <= (len(self.__X) - 2))):
            raise OutOfDomain("Out of range!")

        i = index ( self.__X, x)

        if self.__o == 1:
            return (interpLin (self.__X[i], self.__Y[i], self.__X[i + 1], self.__Y[i + 1], x))
        elif self.__o == 2:
            return (interpQuad (self.__X[i - 1], self.__Y[i - 1], self.__X[i], self.__Y[i], self.__X[i + 1], self.__Y[i + 1], x))
