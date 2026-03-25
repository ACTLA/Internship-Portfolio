import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

alpha, beta, gamma, mu, nu = 1, 1, 1, 1, 1

def system(vars):
    x1, x2, x3, x4 = vars
    eq1 = beta*x1 + gamma*x2 + nu*x3 + x4 - (10*mu + nu)
    eq2 = x1 - 3*mu*x2 + 2*x3 + 4*alpha*x4 - (9 + gamma)
    eq3 = -5*x1 + nu*x2 - x3 - 7*x4 + 5
    eq4 = nu*x1 - 6*x2 + 2*x3 + 6*x4 - mu
    return [eq1, eq2, eq3, eq4]

initial_guess = [0, 0, 0, 0]
sol = root(system, initial_guess)
print(f"Решение системы: {sol.x}")