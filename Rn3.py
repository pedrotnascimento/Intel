#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as  plt
import numpy  as np 

# R = [ rnd() for _ in range(10000)]
# X = [ 2*x*rnd()-x for x in R]
# Y = [ (rnd()-0.5)*np.sqrt(-(x)**2+r**2) for x,r in zip(X,R)]
# plt.plot(X,Y,'ro')
# plt.show()

def phony_circle_data(radius=1, shift_x=0,shift_y=0, size=10000, plot=False):
    rnd = np.random.rand
    R = [ radius*rnd() for _ in range(size)]
    X = [ 2*x*rnd()-x+shift_x for x in R]
    Y = [(rnd()-0.5)*np.sqrt(-(x-shift_x)**2+r**2) + shift_y for x,r in zip(X,R)]
    if plot:
        plt.plot(X,Y,'ro')
        plt.show()
    else:
        return X,Y


x1,y1 = phony_circle_data(2,shift_x=1, shift_y=1, size=100)
x2,y2 = phony_circle_data(3,shift_x=2, shift_y=2, size=100)
# plt.plot(x1,y1,'ro',x2,y2,'bo')
# plt.show()

def nonlin(x, deriv=False):
    if deriv:
        return x*(1-x)
    return 1/(1+np.exp(-x))

rnd = np.random.rand
tam = 100
w = [(2*rnd()-1, 4*rnd()-2) for i in range(tam)]

min = 99999
for i in range(tam):
    error_1 = []
    error_2 = []
    for j in range(len(x1)):
        error_1 += [y1[j] - (w[i][0]*x1[j] +w[i][1])> 0]
        error_2 += [y2[j] - (w[i][0]*x1[j] +w[i][1])  < 0]
    min_temp = sum(error_1) + sum(error_2)
    if min > min_temp:
        print(min_temp)
        min = min_temp
        min_w1 = w[i][0]
        min_w2 = w[i][1]
else:
    print "iterações:", i 
    

# estimativa feita a mão
#reta = [ -0.25*x+1.8  for x in xrange(5)] # insumo para pesquisa de pesos
reta = [ min_w1*x+min_w2  for x in xrange(5)] # calculado pela rede
plt.plot(x1,y1,'ro',x2,y2,'bo', xrange(5), reta, '-g')
print("coeficiente angular:", min_w1, "coeficiente linear", min_w2)
plt.show()


