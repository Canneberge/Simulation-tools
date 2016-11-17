# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:58:59 2016
@author: loicm
"""
import numpy as np
from numpy import linalg as ln
import pylab as P
# Imports the problem formulation from Assimulo
from assimulo.problem import Explicit_Problem
from assimulo.solvers import CVode  # Imports the solver CVode from Assimulo


def rhs(t, y):
    k = 10
    A = np.array([[0, 0, 1, 0],
                  [0, 0, 0, 1],
                  [-L(y, k), 0, 0, 0],
                  [0, -L(y, k), 0, 0]])
    b = np.array([0, 0, 0, -1])
    yd = np.dot(A,y) + b

    return yd
#def rhs(t,y):
#    A =np.array([[0, 1],[-2, -1]])
#    yd=np.dot(A, y)
#
#    return yd


def L(y, k):
    norm = ln.norm(y[0:2])
    return k * (norm - 1) / norm

y0 = np.array([1.0, 1.0, 1.0, 1.0])
t0 = 0.0

model = Explicit_Problem(rhs, y0, t0)  # Create an Assimulo problem
model.name = 'Linear Test ODE'         # Specifies the name of problem

sim = CVode(model)

tfinal = 10.0        #Specify the final time

t, y = sim.simulate(tfinal) #Use the .simulate method to simulate and provide the final time
sim.plot()
