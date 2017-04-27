#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)

#sigmoid
def nonlin(x,deriv=False):
    if deriv:
        return x*(1-x)
    return 1/(1+np.exp(-x))

# input(new input that in Rn(first exercise))
# this exercise it's not a linear (nonlinear) pattern
# relationship between the input and output -linear
# relationship between the combination of inputs(ex:combination of pixels) - nonlinear
# nonlinear use several layers of network
# first layer COMBINE the inputs and generate a output that will be the input for the next layer
# and this is known as deep layer
x = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1],
            ])
#output
y = np.array([[0],[1],[1],[0]]) # it (seems) must to be in matrix format [[]]
#weights
w1 = 2*np.random.random((3,10))-1 # 3 entradas e 4 saídas para o próximo layer
w2 = 2*np.random.random((10,1)) -1 # 4 entradas e 1 saída para a função de ativação
# para mais algebra, 
#prod interno de vetores v(i,j) onde i linhas e j colunas
# multiplicação de matrizes -> A(m,n).B(q,p) = C(m,p), se n = q
# x(1,3).w1(3,4) = x.w1(1,4) = x' -> x'(1,4).w2(4,1) = x'.w2(1,1) = saida da func ativação


for i in xrange(10000):
    #forward propagation
    l0 = x # layer 0
    
    z1 = np.dot(l0, w1)
    l1 = nonlin(z1) # dot product between the input and the weights
    
    z2 = np.dot(l1, w2)
    l2 = nonlin(z2)
    
    
    # error test(how much it missed?)
    l2_error = y - l2
    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2, True) # reducing the error of high confidence predictions.
    w2 += l1.T.dot(l2_delta)
    
    # ACTUALLY, ABOVE ITS JUST THE GRADIENT DESCENT:
    # dJ/dw2 = d(y-sig(z2(w2))/dw2 = 
    # -(y - sig(z2))*dz2(w2)/dw2 = 
    # -(y-sig(z2(w2))*sig(z1)*dw2/dw2 =
    # -(y-sig(z2(w2))*sig(z1)*dw2/dw2
    # -(y-sig(z2(w2))*sig(z1) =    , takes out the minus sign to go to the direction of decrease of the error
    # -(y-l2)*l1
    # where y = expected output, z2=sig(z1)*w2 = l1*w2
    
    #how much did l1 values contributed to l2 error(according to the weights)???
    l1_error =  l2_delta.dot(w2.T)  
    l1_delta = l1_error*nonlin(l1,deriv=True)
    #update weights
    w1 += l0.T.dot(l1_delta)
    
    # print "error\n", l1_error, "\nl1\n ", l1,"\nderiv\n",nonlin(l1, True),  "\nl1 delta\n", l1_delta, "\npesos atualizados\n", w
    
print "output after training", l2   

# print "new prediction for input [[0,1,1],[1,1,1]] should give 0 and 0 (aproximately) of output"

# l0  = np.array([[0,1,1],[1,1,1]])
# print nonlin(np.dot(l0, w)) # final weights

