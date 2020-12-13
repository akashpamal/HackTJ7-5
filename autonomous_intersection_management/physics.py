####################################
# Created by Akash Pamal, Jack Blair, and Rahel Selemon
# HackTJ 2020 12/13/20
# MIT License
####################################

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


def get_position_function(V0, Vf, spawn_time, intersect_time, deltax):
    deltat = intersect_time - spawn_time
    c = V0
    a = ( ( 6*(deltax - (V0*deltat))) - ( (3*deltat)*(Vf - V0) ) ) / ((deltat**3)*(2 - 3))
    b = (Vf - V0 - (a*(deltat**2))) / deltat
    # deltat_new = Symbol('deltat_new')

    # acceleration_function = Derivative(a * deltat_new ** 2 + b * deltat_new + c, deltat_new)
    # acceleration_function = sympy.diff(a * deltat_new ** 2 + b * deltat_new + c)
    velocity_function_on_approach = lambda current_time : a * (current_time - spawn_time)**2 + b * (current_time - spawn_time) + c
    position_function_on_approach = lambda current_time : (a/3 * (current_time - spawn_time) ** 3) + (b/2 * (current_time - spawn_time) ** 2) + (c * (current_time - spawn_time))
    position_function_in_intersection = lambda current_time : deltax + Vf * (current_time - intersect_time)
    def piecewise_position_function(deltat_new):
        if deltat_new >= deltat:
            return position_function_in_intersection(deltat_new)
        else:
            return position_function_on_approach(deltat_new)
    
    return piecewise_position_function


    
    

if __name__ == '__main__':
    acceleration_function = get_position_function(50, 30, 0, 5, 20)
    acceleration_function(5)
    print(acceleration_function)
    print(acceleration_function_manual)