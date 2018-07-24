## @file SeqServices.py
#  @brief Library module that provides services for processing sequences.
#  @date 07/24/2018

## @brief Checks to see if a given list is monotonically increasing
#  @param X list in question
def isAscending ( X ):
    for i in range (0, len(X) - 1):
        if (X[i+1] <= X[i]):
            return False
    return True

## @brief Checks to see if a given value is within the bounds of a provided list
#  @details Assumes isAscending is True
#  @param X list providing boundaries
#  @param x variable in question
def isInBounds ( X , x ):
    if (X[0] <= x <= X[len(X) - 1]):
        return True
    return False

## @brief Linear interpolation function
#  @details Assumes isAscending is True
#  @return interpolated value calculated using provided inputs
def interpLin ( x1 , y1 , x2 , y2 , x ):
    return (((y2 - y1)/(x2 - x1))*(x - x1) + y1) # y value

## @brief Quadratic interpolation function
#  @details Assumes isAscending is True
#  @return interpolated value calculated using provided inputs
def interpQuad ( x0 , y0 , x1 , y1 , x2 , y2 , x ):
    return ( y1 +
             ((y2 - y0)/(x2 - x0))*(x - x1) +
             ((y2 - 2*y1 + y0)/(2*(pow(x2 - x1, 2))))*(pow(x - x1, 2)))

## @brief Determines the best "placement" for a value against a provided list
#  @details Assumes isAscending is True and isInBounds is True
#  @param x the real number input which is getting compared to elements in the current sequence
#  @return The index at which X(i) <= v < X(i+1) holds true
def index ( X , x ):
    for i in range(0, len(X) - 1):
        if ((X[i] <= x < X[i+1])):
            return i
