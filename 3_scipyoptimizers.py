# OPtimizers in SCipy: they are a set of procedures defined in scipy that either find the minimum value of a function or a root of an equation.
# optimizing function: all the algorithms which helps in minimizing the data.
# Root of an equation: x + cos(x), we will solve it via optimize.root function. 
# this function takes 2 arguments: "fun" and x0
# example: here we will find the root of the equation x + cos(x) :
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)

# here we want the info about not just x but the whole root:
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot)

# Minimizing the Function or data:
# high points are called maxima and low points are called minima.
# finding the Minima:
# we use scipy.optimize.minimize(). it uses 3 arguments: "fun", x0 and method:it also has some legal values: "CG", "BFGS", "NEWTON-CG", "L-BFGS-B", "TNC", "COBYLA", "SLSQP".
# callback: functions called after each iteration of optimizations.

# Example of the above: in which we will minimize the function: x^2 + x + 2 with BFGS:
from scipy.optimize import minimize
def eqn(x):
    return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin)