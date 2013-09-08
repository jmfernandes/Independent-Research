#!/usr/bin/env python

# import the necessary modules
import numpy as np
from pylab import *
from scipy.optimize import curve_fit

# Define the fitting function
def func(x, a, b, c):
	return a*np.exp(-b*x) + c

# Generate x and y values which the curve will be fitted to
# (In practical cases, these should be read in)
x = np.array([0,1,2,4])
yn = np.array([4,3,2,.5])
#x = np.linspace(0,4,50)
#y = func(x, 2.5, 1.3, 0.5)
#yn = y + 0.2*np.random.normal(size=len(x))



# The actual fitting part
# popt = the fitted parameters as a tuple, namely (a,b,c)
# pconv = The estimated covariance of popt.
#        The diagonals provide the variance of the parameter estimate.
popt, pcov = curve_fit(func, x, yn)

plot(x,yn)
z = func(x,popt[0],popt[1],popt[2])
plot(x,z)
show()