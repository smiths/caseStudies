We start from [[BT-consThermE]] and refine it as follows.

# Refine $\mathbf{q}$
Refine using [[BT-Gauss's Divergence Theorem]]

# Refine  g
By [[A-UniformHeatGen-OverVol]] we can change our equation to:

$$-{\nabla \cdot \mathbf{q} (\mathbf{x}, t)} + g(t) = \rho (\mathbf{x}, T) C (\mathbf{x}, T) \frac{\partial T(\mathbf{x}, t)}{\partial t}$$

# Refine $\rho$
Apply [[A-Density-Independent-of-Temp]] to get:

$$-{\nabla \cdot \mathbf{q} (\mathbf{x}, t)} + g(t) = \rho (\mathbf{x}) C (\mathbf{x}, T) \frac{\partial T(\mathbf{x}, t)}{\partial t}$$
Apply [[A-UniformDensity-OverVol]] to get:

$$-{\nabla \cdot \mathbf{q} (\mathbf{x}, t)} + g(t) = \rho C (\mathbf{x}, T) \frac{\partial T(\mathbf{x}, t)}{\partial t}$$
# Refine C

Apply [[A-Specific-Heat-Independent-of-Temp]] to get:

$$-{\nabla \cdot \mathbf{q} (\mathbf{x}, t)} + g(t) = \rho C (\mathbf{x}) \frac{\partial T(\mathbf{x}, t)}{\partial t}$$
Apply [[A-UniformSpecHeat-OverVol]] to get:

$$-{\nabla \cdot \mathbf{q} (\mathbf{x}, t)} + g(t) = \rho C \frac{\partial T(\mathbf{x}, t)}{\partial t}$$


# Refine T

Finally we have [[RT-rocTempSimp]]
