from scipy.integrate import ode
  
def func_T_W(params):
  def f(t, Tw):
    return (1.0 / params.tau_w) * (params.Tc - Tw)

  r = ode(f).set_integrator('vode', method='bdf', atol=params.AbsTol, rtol=params.RelTol)
  r.set_initial_value(params.Tinit)

  t = [0.0]
  Tw = [params.Tinit]

  while r.successful() and r.t < params.tfinal:
    r.integrate(r.t + params.tstep)
    t.append(r.t)
    Tw.append(r.y[0])

  return t, Tw