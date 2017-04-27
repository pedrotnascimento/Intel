#!/usr/bin/env python
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand as rnd

def phony_data(n=3, size=4,seed=False):
    l = []
    y = []
    if seed:
        np.random.seed(1)
    for i in range(size):
        l.append([])
        for j in range(n):
            l[i].append(rnd())
    for i in range(size):
        y.append([rnd()])
    Y = np.array(y)
    X = np.array(l)
    # print "X:\n", X
    # print "Y:\n", Y
    return X, Y
    

phony_data()

def nonlin(x,deriv=False):
    if deriv:
        return x*(1-x)
    
    return 1/(1+np.exp(-x))

    
X,Y = phony_data(seed=True)
np.random.seed(1)
w = 2*np.random.random((3,1))-1

for i in xrange(10000):

    l0 = X
    l1 = nonlin(np.dot(l0, w)) 
    l1_error = Y -l1
 
    l1_delta = l1_error*nonlin(l1, True) 
    w += np.dot(l0.T,l1_delta)
    # print "error\n", l1_error, "\nl1\n ", l1,"\nderiv\n",nonlin(l1, True),  "\nl1 delta\n", l1_delta, "\npesos atualizados\n", w
    
print "out desired\n", Y, "\nout trained\n", l1   

# print "new prediction for input [[0,1,1],[1,1,1]] should give 0 and 1 (aproximately) of output"

# l0  = np.array([[0,1,1],[1,1,1]])
# print nonlin(np.dot(l0, w)) # final weights
