from sympy.solvers import solve
from sympy import Symbol, Derivative


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
    c = V0
    a = ( ( 6*(deltax - (V0*deltat))) - ( (3*deltat)*(Vf - V0) ) ) / ((deltat**3)*(2 - 3))
    b = (Vf - V0 - (a*(deltat**2))) / deltat
    # deltat_new = Symbol('deltat_new') 

    # acceleration_function = Derivative(a * deltat_new ** 2 + b * deltat_new + c, deltat_new)
    # acceleration_function = sympy.diff(a * deltat_new ** 2 + b * deltat_new + c)
    def acceleration_function(deltat_new):
        return (a/3 * deltat_new ** 3) + (b/2 * deltat_new ** 2) + (c * deltat_new)
#    acceleration_f unction_manual = lambda deltat_new : (a/3 * deltat_new ** 3) + (b/2 * deltat_new ** 2) + (c * deltat)
    return acceleration_function

if __name__ == '__main__':
    acceleration_function = get_acceleration_function(50, 30, 5, 20)
    acceleration_function(5)
    print(acceleration_function)
    print(acceleration_function_manual)