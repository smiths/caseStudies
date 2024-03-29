##Derived Values Module
##Secret: The transformations from initial inputs to derived quantities
##Service: Defines the equations transforming the initial inputs into derived quantities

import math

def derived_params(params):
    # cal aspect ratio
    params.asprat = params.a / params.b
    # cal stand off distance
    temp = pow(params.sdvect[0], 2) + pow(params.sdvect[1], 2) + pow(params.sdvect[2], 2)
    params.sd = math.sqrt(temp)
    # cal load duration factor
    params.ldf = pow((params.td / 60.0), (params.m / 16.0))
    # cal weight of tnt
    params.wtnt = params.w * params.tnt
    # cal actual thickness
    if params.t == "2.5":
        params.h = 2.16
    elif params.t == "2.7":
        params.h = 2.59
    elif (params.t == "3.0"):
        params.h = 2.92
    elif (params.t == "4.0"):
        params.h = 3.78
    elif (params.t == "5.0"):
        params.h = 4.57
    elif (params.t == "6.0"):
        params.h = 5.56
    elif (params.t == "8.0"):
        params.h = 7.42
    elif (params.t == "10.0"):
        params.h = 9.02
    elif (params.t == "12.0"):
        params.h = 11.91
    elif (params.t == "16.0"):
        params.h = 15.09
    elif (params.t == "19.0"):
        params.h = 18.26
    elif (params.t == "22.0"):
        params.h = 21.44
    else:
        raise ValueError("Wrong thickness entered - Not an industrial standard")

    # cal glass type factor
    if params.gt in ['AN', 'an']:
        params.gtf = 1
    elif params.gt in ['HS', 'hs']:
        params.gtf = 2
    elif params.gt in ['FT', 'ft']:
        params.gtf = 4
    else:
        raise ValueError("Wrong glass type entered - must be AN, HS, or FT")
