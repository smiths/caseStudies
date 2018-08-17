## @file ThicknessADT.py
#  @brief Implements an ADT for the thickness
#  @date 07/25/2018

class ThicknessT :

    def __init__ ( self, x ):

        T = [2.5, 2.7, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 16.0, 19.0, 22.0]

        if x not in T:
            raise ValueError("Invalid input")
        if type(x) is not float:
            raise ValueError("Invalid type")

        # state variable
        self.t = x

    ## @brief Gets the nominal thickness value
    # @return the minimum thickness value
    def toMinThick ( self ):
        if self.t == 2.5:
            return 2.16e-3
        elif self.t == 2.7:
            return 2.59e-3
        elif self.t == 3.0:
            return 2.92e-3
        elif self.t == 4.0:
            return 3.78e-3
        elif self.t == 5.0:
            return 4.57e-3
        elif self.t == 6.0:
            return 5.56e-3
        elif self.t == 8.0:
            return 7.42e-3
        elif self.t == 10.0:
            return 9.02e-3
        elif self.t == 12.0:
            return 11.91e-3
        elif self.t == 16.0:
            return 15.09e-3
        elif self.t == 19.0:
            return 18.26e-3
        elif self.t == 22.0:
            return 21.44e-3

    ## @brief Gets the nominal thickness
    def toFloat ( self ):
        return self.t
