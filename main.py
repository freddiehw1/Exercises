from solvers import NewtonsMethod
import numpy as np 
from scipy.optimize import root


def f(x):
    return np.cos(x) - x 

def fdash(x):
    return -np.sin(x) - 1

tolerance = 10e-10
output = NewtonsMethod(f, fdash, 0, tolerance)
print(output)
    
#3c
output = root(f, 0)
print(output)