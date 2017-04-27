#!/usr/bin/env python
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand as rnd
from numpy.linalg import norm

def phony_circle_data(radius=1, shift_x=0,shift_y=0, size=100, plot=False):
    rnd = np.random.rand
    R = [ radius*rnd() for _ in range(size)]
    X = [ 2*x*rnd()-x+shift_x for x in R]
    Y = [(rnd()-0.5)*np.sqrt(-(x-shift_x)**2+r**2) + shift_y for x,r in zip(X,R)]
    if plot:
        plt.plot(X,Y,'ro')
        plt.show()
    else:
        return X,Y

X1,Y1 = phony_circle_data(2,shift_x=-1, shift_y=1, size=30)
X2,Y2 = phony_circle_data(2,shift_x=1, shift_y=1, size=30)
# X1 = [(rnd()*2-2) for _ in range(30)]
# Y1 = [(rnd()*2-1) for _ in range(30)]
# X2 = [(rnd()*2) for _ in range(30)]
# Y2 = [(rnd()*2-1) for _ in range(30)]
X = X1 + X2
Y = Y1 + Y2
C = [1]*(100) + [-1]*(100)
inputs = []
for i in range(len(X1)):
    inputs.append([X1[i],Y1[i],1])
    inputs.append([X2[i],Y2[i],-1])
    


# def phony_line_data(coef_ang=1, coef_lin=0, interval=(0,4),standard_deviation=2, size=100, plot=False, random=False):
    # rnd = np.random.rand
    # if random:
        # coef_ang = 10*rnd() -5
        # coef_lin = 10*rnd() -5
        # interval = (5*rnd() -5, 5*rnd())
        # standard_deviation = 5*rnd()
    # interval_range = interval[1] -interval[0]
    # X = [ interval_range*rnd() + interval[0] for _ in range(size)]
    # Y = [ coef_ang*y + coef_lin + standard_deviation*rnd() - standard_deviation/2 for y in X]
    # if plot:
        # plt.plot(X,Y,'rx')
        # plt.show()
    # else:
        # return X,Y
    
# X, Y = phony_line_data(random=True)

#np.random.seed(1)
W = [ 2*rnd()-1 for _ in range(2)] # using bias, that means threshould set to 0
e_epoch= 100
alpha = 0.1
epoch =0

while e_epoch != 0 and epoch < 100:
    epoch+=1
    e_list = 0
    for x in inputs:
        l0 = W[0]*x[0] + W[1]*x[1] 
        e = 1 if l0 >= 0 else -1
        if x[2] !=  e:
            E = x[2] - e # #localError
            e_list+= E**2 
            W[1] = W[1] + alpha*E*x[1]
            W[0] +=  alpha*E*x[0]
    print e_list
    # e_epoch = np.sqrt(e_list/len(X))
    # print e_epoch

print epoch


reta = [ W[1]*x+W[0]  for x in list(np.arange(-1,1,0.2))] # calculado pela rede
print W[1], W[0]
# plt.plot(X1,Y1,'ro',X2,Y2,'bo', xrange(int(min(X)), int(max(X))), reta, '-g')

# plot of the separation line.
# The separation line is orthogonal to w
W_array =np.array(W) 
n = norm(W_array)
ww = W_array/n
ww1 = [ww[1],-ww[0]]
ww2 = [-ww[1],ww[0]]
# plot([ww1[0], ww2[0]],[ww1[1], ww2[1]],'--k')
# show()

# Perceptron test
Tx1,Ty1 = phony_circle_data(2,shift_x=-1, shift_y=1, size=30)
Tx2,Ty2 = phony_circle_data(2,shift_x=1, shift_y=1, size=30)
tests = []
for i in range(len(X1)):
    tests.append([Tx1[i],Ty1[i],1])
    tests.append([Tx2[i],Ty2[i],-1])

for x in tests:
 t = W[1]*x[1]  + W[0]*x[0]
 r = 1 if t >=0 else -1
 if r != x[2]: # if the response is not correct
  print 'error'
 
plt.plot(X1,Y1,'ro',X2,Y2,'bx', [ww1[0], ww2[0]],[ww1[1], ww2[1]], '-g')
plt.show()
