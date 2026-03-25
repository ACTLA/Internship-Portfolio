import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def system(vars):
    x1, x2, x3, x4 = vars
    eq1 = 3*x1 + x2 + x3 + gamma*x4 - alpha
    eq2 = x1 - mu*x2 + nu*x3 + 4*x4 - beta
    eq3 = -5*x1 - x3 - 7*x4 + 5
    eq4 = x1 - 6*x2 + alpha*x3 + 6*x4 - 3
    return [eq1, eq2, eq3, eq4]

# Параметры
alpha, beta, gamma, mu, nu = 1, 1, 1, 1, 1

initial_guess = [0, 0, 0, 0]
sol = fsolve(system, initial_guess)
print(f"Решение системы: x1 = {sol[0]}, x2 = {sol[1]}, x3 = {sol[2]}, x4 = {sol[3]}")