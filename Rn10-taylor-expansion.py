#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import  matplotlib.pyplot  as plt
from numpy.random import rand
from numpy import array, dot, ones, zeros, log, exp

degree = 2
def phony_function(degree=3, 
                    interval=(-2,2),
                    standard_deviation=0.25,
                    size=5,
                    plot=False,
                    random=False):
    if random:
        interval = (10*rand() -5, 5*rand())
        standard_deviation = 5*rand()
    interval_range = interval[1] -interval[0]
    X = [ interval_range*rand() + interval[0] for _ in range(size)]
    coef =[ 4*rand() -2 for _ in range(degree+1)]
    Y =[]
    for i in range(len(X)):
        Y+=[0]
        for d in range(degree+1):
            Y[i] += coef[d]*X[i]**d 
    if plot:
        plt.plot(X,Y,'g.')
        plt.show()
    else:
        return X,Y    

X, Y = phony_function(degree=degree)
X, Y = array([ones(len(X)),X]), array([Y])
X = X.T
U = array([[rand(),rand()]])
W = array([[rand(),rand()]])
A = array([[rand(),rand(),rand()]])
print X
print  X[0]
print  W

for i in range(len(X[0])):
    l0w = log(dot(W, X[i]))
    l0u = log(dot(U, X[i]))
    
    l0_arr = array([[l0w, l0u, 1]])
    l1 = dot(l0_arr, A)
    y = exp(l1)
    e = Y[i] - y
    