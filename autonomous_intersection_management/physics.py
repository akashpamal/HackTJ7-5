from sympy.solvers import solve
from sympy import Symbol


# class Physics:
#     def get_position(self, a, timeofAcc dtAcc, elapsed_time):
#         if elapsed_time <= timeofAcc:
#             return initV*elapsed_time
#         elif elapsed_time <= (timeofAcc+dt):
#             return initV*timeofAcc + (initV*(elapsed_time-timeofAcc) + (0.5*a*(elapsed_time-timeofAcc))
#         else:
#             return initV*timeofAcc + (initV*dt) + (0.5*a*dt) + (finalV*(elapsed_time-dt-timeofAcc))

#     def funcname(self, parameter_list):
#         """
#         docstring
#         """
#         pass


def get_acceleration_function(V0, Vf, deltat, deltax):
    # a = Symbol('a')
    # b = Symbol('b')
    c = V0
    b = (deltax - V0*deltat - deltat**3*Vf-deltat**3*V0) / (deltat/2 - deltat**4)
    # a = (6*deltax - 3*V0*deltat - 3*Vf) / ((2*deltat**3) - (3*delta**2))
    # b = b[0]
    # b = -25.276
    # a = solve(a * deltat ** 2 + b * deltat + c, a)
    # a = solve((Vf - V0 - b * deltat) ** .5 / deltat, a)
    # a = a[0]
    # deltat_new = Symbol('t')
    # b = (Vf - V0 - a*deltat**2) / deltat
    derivative_function = sym.diff(a * deltat_new ** 2 + b * deltat_new + c)
    return derivative_function
    

if __name__ == '__main__':
    acceleration_function = get_acceleration_function(50, 30, 5, 20)