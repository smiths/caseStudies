module Calculations

import DifferentialEquations as D

function func_V_W(V_tank::Float64)
    return V_tank
end

function func_m_W(rho_W::Float64, V_W::Float64)
    return V_W * rho_W
end

function func_tau_W(C_W::Float64, h_C::Float64, A_C::Float64, m_W::Float64)
    return m_W * C_W / (h_C * A_C)
end

""" Calculates temperature of the water: the average kinetic energy of the particles within the water (degreeC)
    - Parameter T_C: temperature of the heating coil: the average kinetic energy of the particles within the coil (degreeC)
    - Parameter T_init: initial temperature: the temperature at the beginning of the simulation (degreeC)
    - Parameter t_final: final time: the amount of time elapsed from the beginning of the simulation to its conclusion (s)
    - Parameter A_tol: absolute tolerance
    - Parameter R_tol: relative tolerance
    - Parameter t_step: time step for simulation: the finite discretization of time used in the numerical method for solving the computational model (s)
    - Parameter tau_W: ODE parameter for water related to decay time: derived parameter based on rate of change of temperature of water (s)
    - Returns: temperature of the water: the average kinetic energy of the particles within the water (degreeC)
"""
function func_T_W(T_C::Float64, T_init::Float64, T_final::Float64, A_tol::Float64, R_tol::Float64, t_step::Float64, tau_W::Float64)
    """ Calculates the rate of change of T_W based on its current value
        - Parameter T_W: current value of T_W
        - Parameter _: params (unused)
        - Parameter t: time(?) (unused)
        - Returns: derivative of T_W
    """
    function f(T_W, _, _)
        return [-(1.0 / tau_W) * T_W[1] + 1.0 / tau_W * T_C]
    end

    # Need to specify total time range.
    t_span = (0.0, T_final)
    # Need to give derivative function, initial value, and total time range.
    r = D.ODEProblem(f, [T_init], t_span)
    # Need to give problem, algorithm (if you want to choose it), relative tolerance,
    # absolute tolerance, and length of time steps.
    sol = D.solve(r, alg=D.DP5(), reltol=R_tol, abstol=A_tol, saveat=t_step)
    # Some post-processing to unwrap the data we want.
    T_W = Array{Float64}([])
    for x in sol.u
        append!(T_W, x[1])
    end

    return T_W
end

end