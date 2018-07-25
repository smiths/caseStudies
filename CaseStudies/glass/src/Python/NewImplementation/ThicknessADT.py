## @file ThicknessADT.py
#  @brief Implements an ADT for the thickness
#  @date 07/25/2018

class ThicknessT :

    def __init__ ( self, x ):

        T = [2.5, 2.7, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 16.0, 19.0, 22.0]

        if x not in T:
            raise ValueError("invalid input")

        # state variable
        self.__t = x

    ## @brief Gets the nominal thickness value
    # @return the minimum thickness value
    def toMinThick ( self ):
        if self.__t == 2.5:
            return 2.16
        elif self.__t == 2.7:
            return 2.59
        elif self.__t == 3.0:
            return 2.92
        elif self.__t == 4.0:
            return 3.78
        elif self.__t == 5.0:
            return 4.57
        elif self.__t == 6.0:
            return 5.56
        elif self.__t == 8.0:
            return 7.42
        elif self.__t == 10.0:
            return 9.02
        elif self.__t == 12.0:
            return 11.91
        elif self.__t == 16.0:
            return 15.09
        elif self.__t == 19.0:
            return 18.26
        elif self.__t == 22.0:
            return 21.44

    ## @brief Gets the nominal thickness
    def toFloat ( self ):
        return self.__t
