## @file GlassTypeADT.py
#  @brief Implements an ADT for a GlassType
#  @date 07/25/2018

from enum import Enum

## @brief Enumeration type used for the state variable of GlassTypeT
class gtf ( Enum ):
    AN = 1
    FT = 2
    HS = 3

class GlassTypeT :

    def __init__ ( self, s ):

        # raise any exceptions
        if type(s) is not str:
            raise ValueError("Invalid type")
        if s not in ["AN","FT","HS"]:
            raise ValueError("Invalid input")

        # state variables
        if s == "AN":
            self.__g = gtf.AN
        elif s == "FT":
            self.__g = gtf.FT
        elif s == "HS":
            self.__g = gtf.HS

    ## @brief Gets the a numerical value based on the glass type
    # @return Glass Type Factor necessary for other calculations
    def GTF ( self ):
        if self.__g == gtf.AN:
            return 1.0
        if self.__g == gtf.FT:
            return 4.0
        if self.__g == gtf.HS:
            return 2.0

    ## @brief Gets the type of glass
    # @return the type of glass being tested
    # (AN => annealed, FT => fully tempered, HS => heat strengthened)
    def toString ( self ):
        if self.__g == gtf.AN:
            return "AN"
        if self.__g == gtf.FT:
            return "FT"
        if self.__g == gtf.HS:
            return "HS"
