horiz_velo = 17 #m/s

height = 6 #m

g = 9.81 #m/s^2

pAx = 0
pAy = 0
vAx = horiz_velo
vAy = 0
pBy = -height

import math
tAB = math.sqrt((pAy - pBy)/(0.5*(g)))
print("ANSWER tAB = ", tAB, "s")
