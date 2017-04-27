#!/usr/bin/env python
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand as rnd
"""
CARA ESSE ARQUIVO ESTÁ UMA MERDA DEVERIA SER UM LEASTMEAN SQUARE 
QUANDO NA VERDADE É BEM PARECIDO COM PERCEPTRON
foi inclusive baseado num vídeo errado
"""


def phony_quadratic_data(a=1,b=0,c=0, interval=(-1,1),standard_deviation=0.25, size=100, plot=False, random=False):
    rnd = np.random.rand
    if random:
        a = 10*rnd() -5
        b = 10*rnd() -5
        interval = (10*rnd() -5, 5*rnd())
        standard_deviation = 5*rnd()
    interval_range = interval[1] -interval[0]
    X = [ interval_range*rnd() + interval[0] for _ in range(size)]
    Y = [ a*x**2 + b*x + c + standard_deviation*rnd() - standard_deviation/2 for x in X]
    if plot:
        plt.plot(X,Y,'rx')
        plt.show()
    else:
        return X,Y    
        
def phony_data(n=3, size=20,seed=False):
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
    
# X,Y = phony_quadratic_data()
X,Y = phony_data()
np.random.seed(1)
W = 2*np.random.random((3,1))-1
e_epoch= 100
alpha = 0.006
epoch =0
while e_epoch > 0.25 and epoch < 1000: # erro minimo é 0.25
    epoch+=1
    e_list = 0
    for i in xrange(X.shape[0]):
        Xi = np.array([X[i]])
        l0 = Xi.dot(W) 
        E = Y[i] - l0 
        # print "errorLocal: ", E
        e_list+= E**2 #localError
        # array da porcentagem da diferença # parece que não é feito assim usualmente
        # e_list += [abs((Y[i]-l0)/l0)] 
        # print e_list
        # ones = np.ones((1,E.shape[0]))
        # E_rms = np.sqrt(ones.dot(E))
        # print Y.shape , E_rms.shape
        # print "befor:\n", W, "\nX: \n",X[i], "\nError\n",E, "\ncalc\n",(alpha*E*X[i]).T
        W = W + alpha*E*Xi.T
        # print "after:\n", W
    # print len(e_list)
    e_epoch = np.sqrt(e_list/X.shape[0]) # media das porcentagens
    print e_epoch
    # input()
    # l0 = [ W[0]*x**2 + W[1]*x + W[2] for x in X]
    # E = [ y - l for y,l ]

# for i in xrange(X.shape[0]):
    # ones = np.ones((1,W.shape[0]))
    # l0 = X[i]
    # Z = W*l0 # matriz diagonal
    # Z_redux = Z*ones.T # vetor com elementos da diagonal principal
    # E = (Y - Z_redux)**2 
    # E_rms = np.sqrt(ones*E)
    # W = W.T + alpha*E_rms*l0.T
        
print "out desired\n", Y, "\nout trained\n"
for i in range(X.shape[0]):
    print X[i].dot(W)

# print "new prediction for input [[0,1,1],[1,1,1]] should give 0 and 1 (aproximately) of output"

# l0  = np.array([[0,1,1],[1,1,1]])
# print nonlin(np.dot(l0, w)) # final weights
