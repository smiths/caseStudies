import load_params
import verify_params
import energy
import calculations
import plot
import output
import verify_output
import sys
from scipy.integrate import ode
import numpy as np

filename = sys.argv[1]
filenamePrefix = ""
for char in filename:
    filenamePrefix = filenamePrefix + char
    if char is '.':
        break
params = load_params.load_params(filename)
verify_params.verify_valid(params)
verify_params.verify_recommended(params)

t, Tw = calculations.func_T_W(params)
  
Ew = energy.energyWat(Tw, params)  

verify_output.verify_output(t, Tw, Ew, params)
plot.plot(t, Tw, Ew, filenamePrefix)
output.output(params, t, Tw, Ew, Ew, filenamePrefix)
