# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:48:14 2016

@author: charl
"""

import numpy as N
import pylab as P
from assimulo.problem import Explicit_Problem  #Imports the problem formulation from Assimulo
from assimulo.solvers import CVode #Imports the solver CVode from Assimulo

def rhs(t,y):
    A =N.array([[0,1],[-2,-1]])
    yd=N.dot(A,y)

    return yd

def rhs2(t,y):
    A=N.array([[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])

def lambde(y1,y2,k):
    return k*(sqrt(y1*y1+y2*y2)-1)/(sqrt(y1*y1+y2*y2))
y0=N.array([1.0,1.0])
t0=0.0
model = Explicit_Problem(rhs, y0, t0) #Create an Assimulo problem
model.name = 'Linear Test ODE'        #Specifies the name of problem (optional)
sim = CVode(model)
"sim.plot()"
#Plots the result
P.plot(t,y)
P.show()