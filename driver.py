# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 04:23:51 2016

@author: Chris
"""
import numpy as np
import math
from matplotlib import animation
import matplotlib.pyplot as plt
from numba import cuda
from lineSolve import lineSolve

a = -2
b = 2
N = 32
x1 = np.linspace(-2, -1.75, 4*N)
x2 = np.linspace(-1.75, -1.0 , 16*N)
x3 = np.linspace(-1.0, -.5 , 16*N)
x4 = np.linspace(-.5 , 0 , 16*N)
x5 = np.linspace(0 , .5 , 16*N)
x6 = np.linspace(.5 , 1 , 16*N)
x7 = np.linspace(1 , 1.5 , 16*N)
x8 = np.linspace(1.5 , 2 , 16*N)
#x1 = np.linspace(-2, 0, N,dtype = np.float32)
#x2 = np.linspace(0, 2 , N,dtype = np.float32)
p = 144*2
f = lambda x: math.exp(-p*((x-(a+b)/2)/(b-a))**2)
g = lambda x: 2*p/(b-a)**2*(x-(a+b)/2)*math.exp(  -p*( (x-(a+b)/2) / (b-a) )**2)
#f = lambda x: math.cos(40*x)/(1+10*x**2)
#g  = lambda x: 0
c = 1
cfl = 10
bcs = "periodic"

solver = lineSolve([x1,x2,x3,x4,x5,x6,x7,x8], f, g , c , cfl , bcs)
uSoln = []
for i in range(1000):
    solver.propogate()
    uSoln.append(solver.getSolns())
x = solver.getXSize()

def animate(i):
    line.set_data(x,uSoln[i])
    return line,
def init():
    line.set_data([], [])
    return line,
fig   = plt.figure()
ax    = plt.axes(xlim=(-2,2),ylim = (-1.3,4))
line, = ax.plot([],[] , lw=2)
anim = animation.FuncAnimation(fig,animate, blit=True)