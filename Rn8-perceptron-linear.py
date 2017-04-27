#!/usr/bin/env python
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand as rnd

def phony_line_data(coef_ang=1, coef_lin=0, interval=(0,4),standard_deviation=2, size=10, plot=False, random=True):
    rnd = np.random.rand
    if random:
        coef_ang = 10*rnd() -5
        coef_lin = 10*rnd() -5
        interval = (5*rnd() -5, 5*rnd())
        standard_deviation = 5*rnd()
    interval_range = interval[1] -interval[0]
    X = [ interval_range*rnd() + interval[0] for _ in range(size)]
    Y = [ coef_ang*y + standard_deviation*rnd() - standard_deviation/2 for y in X]
    Y = map(lambda x: x+coef_lin, Y)
    if plot:
        plt.plot(X,Y,'rx')
        plt.show()
    else:
        return X,Y

X,Y = phony_line_data()
# X2,Y2 = phony_circle_data(3,shift_x=2, shift_y=2, size=100)
# Y = Y1 + Y2
np.random.seed(1)
W = [ rnd() for _ in range(2)]
e_epoch= 100
alpha = 0.001
epoch =0

while e_epoch > 0.025 and epoch < 1000: # erro minimo é 0.25
    epoch+=1
    e_list = 0
    for i in xrange(len(X)):
        l0 = W[0] + W[1]*X[i]
        E = Y[i]- l0 
        # print "errorLocal: ", E
        e_list+= E**2 #localError
        # print "befor:\n", W, "\nX: \n",X[i], "\nError\n",E, "\ncalc\n",(alpha*E*X[i]).T
        W[1] = W[1] + alpha*E*X[i]
        W[0] +=  alpha*E
        # print W, X[i], alpha*E*X[i]
    e_epoch = np.sqrt(e_list/len(X)) # media das porcentagens
    print e_epoch
    # input()
    # l0 = [ W[0]*x**2 + W[1]*x + W[2] for x in X]
    # E = [ y - l for y,l ]

print epoch
# for i in xrange(X.shape[0]):
    # ones = np.ones((1,W.shape[0]))
    # l0 = X[i]
    # Z = W*l0 # matriz diagonal
    # Z_redux = Z*ones.T # vetor com elementos da diagonal principal
    # E = (Y - Z_redux)**2 
    # E_rms = np.sqrt(ones*E)
    # W = W.T + alpha*E_rms*l0.T
        

for i in range(len(X)):
   print "out desired  ", Y[i], " -  out trained", W[0] + W[1]*X[i]
reta = [ W[1]*x+W[0]  for x in xrange(int(min(X)), int(max(X)))] # calculado pela rede
plt.plot(X,Y,'ro', xrange(int(min(X)), int(max(X))), reta, '-g')
# print("coeficiente angular:", min_w1, "coeficiente linear", min_w2)
plt.show()

# l0  = np.array([[0,1,1],[1,1,1]])
# print nonlin(np.dot(l0, w)) # final weights
