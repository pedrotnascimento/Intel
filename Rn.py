#!/usr/bin/env python
#-*- coding: utf-8 -*-

#A neural network trained with backpropagation is attempting to use input to predict output.

import matplotlib.pyplot as plt 
#import random as r
import numpy as np



#sigmoid function
#why not call sigmoid? nonlin can be another activation function
def nonlin(x,deriv=False):
    if deriv:
        return x*(1-x)
    
    return 1/(1+np.exp(-x))

# example sigmoid plot 
# Xaxis = np.arange(-5,5,0.2)
# plt.plot(Xaxis, nonlin(Xaxis))
# plt.show()
    
    
# input dataset
# it (seems) must to be in matrix format [[]]
x = np.array([[0,0,1],
            [1,1,1],
            [1,0,1],
            [0,1,1],
            ])

# showing a way of represent the data, it just a image which the black square are 0's, and its kind a colored matrix
# plt.matshow(np.hstack((x,y)).fignum=10, cmap-plt.cm.gray)
# plt.show()
#output dataset
y = np.array([[0,1,1,0]]).T # it (seems) must to be in matrix format [[]]

# seed random number 
np.random.seed(1)

# add random number to weights
#np.random.random() Return random floats in the half-open interval [0.0, 1.0).
#np.random.random((m,n)) returns a matrix with dimension mxn( m linhas, n colunas)
# Results are from the “continuous uniform” distribution over the stated interval. To sample Unif[a, b), b > a multiply the output of random_sample by (b-a) and add a:
# (b - a) * random_sample() + a
w = 2*np.random.random((3,1))-1

for i in xrange(500):
    #forward propagation
    l0 = x # why? l0 stands for layer 0, i.e, the input it self
    
    # nonlinear part
    l1 = nonlin(np.dot(l0, w)) # dot product between the input and the weights
    # the output means the probability of this being correct ;)
    
    # error test(how much it missed?)
    l1_error = y -l1
    
    # multiply how much missed by the slope of sigmoid at l1
    l1_delta = l1_error*l1 # reducing the error of high confidence predictions.
    
    # l1_delta =  (y - sig(x.w))*deriv(sig(x.w))
    
    #update weights
    w += np.dot(l0.T,l1_delta)
    # print "error\n", l1_error, "\nl1\n ", l1,"\nderiv\n",nonlin(l1, True),  "\nl1 delta\n", l1_delta, "\npesos atualizados\n", w
    
print "output after training", l1   

print "new prediction for input [[0,1,1],[1,1,1]] should give 0 and 1 (aproximately) of output"

l0  = np.array([[0,1,1],[1,1,1]])
print nonlin(np.dot(l0, w)) # final weights
