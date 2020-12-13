from sympy.solvers import solve
from sympy import Symbol


class Physics:
    def get_position(self, a, timeofAcc dtAcc, elapsed_time):
        if elapsed_time <= timeofAcc:
            return initV*elapsed_time
        elif elapsed_time <= (timeofAcc+dt):
            return initV*timeofAcc + (initV*(elapsed_time-timeofAcc) + (0.5*a*(elapsed_time-timeofAcc))
        else:
            return initV*timeofAcc + (initV*dt) + (0.5*a*dt) + (finalV*(elapsed_time-dt-timeofAcc))

    def funcname(self, parameter_list):
        """
        docstring
        """
        pass

class Calculator:
    def get_acceleration_function(V0, deltat, Vf, deltax):
        a = Symbol('a')
        b = Symbol('b')
        b = solve((Vf - V0 - b * deltat) ** .5 / 3 * deltat ** 3 + b / 2 * deltat ** 2 + V0 * deltat)
        a = solve((Vf - V0 - b * deltat) ** .5 / deltat)
        c = V0
        deltat_new = Symbol('t')
        derivative_function = sym.diff(a * deltat_new ** 2 + b * deltat_new + c)