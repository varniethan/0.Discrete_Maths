from scipy.optimize import linprog
import numpy as np
from cvxopt import matrix
from cvxopt import glpk

#Cake Recipe Equations

#f + e + b + s = 700
#b - 0.5s = 0
#f + e  <= 450
#e + b  <= 300
#f + s - (e + b) <= 0

#Defining a matrix
var_list = ['flour', 'eggs', 'butter', 'sugar']

#Inequlity equations, LHS
A_ineq = [[1, 1, 0, 0], [0, 1, 1, 0], [-1, 1, -1, 1]]

#Inequlity equations, RHS
B_ineq = [450, 300, 0]

#Equality equations, LHS
A_eq = [[1, 1, 1, 1], [0, 0, 1, -0.5]]

#Equality equations, RHS
B_eq = [700, 0]

#Cost function
C = [0, 0, 1, 1]

# print('WITHOUT BOUNDS')
# res_no_bounds = linprog(C, A_ub=A_ineq, b_ub=B_ineq, A_eq=A_eq, b_eq=B_eq, method='interior-point')
# print(res_no_bounds)

def result_parser(res, var_list):
    solve_status = res.success
    if solve_status is True:
        solution_list = res.x
        soln = {var_list[i]: np.round(solution_list[i]) for i in range(len(var_list))}
    else:
        soln = []
    return soln

# these are the bounds that help the solver arrive at a solution
f_b = [0., 300.]  # limits for flour
e_b = [0., 200.]  # limits for eggs
b_b = [0., 100.]  # limits for butter
s_b = [0., 200.]  # limits for sugar

res_bounds = linprog(C, A_ub=A_ineq, b_ub=B_ineq, A_eq=A_eq, b_eq=B_eq, bounds=(f_b, e_b, b_b, s_b),
                     method='interior-point')
print('\nWITH BOUNDS')
print(result_parser(res_bounds, var_list))
# print(res_bounds)

