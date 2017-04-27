#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

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
    
X, Y = phony_quadratic_data(plot=False, random=True)

rnd = np.random.rand # alias for random function
learn_rate = 0.0001
W = [10*rnd()-5, 10*rnd()-5,  10*rnd()-5] # starting with any weight

for i in range(100):
    y = [W[2]*Xi**2 +  W[1]*Xi + W[0] for Xi in X] # calculate every X with current Weights
    e_list = [(Yi - yi) for Yi, yi in zip(Y,y)]  # 
    W[0] += sum([learn_rate*e for e in e_list])
    W[1] += sum([learn_rate*e*x for e,x in zip(e_list,X)])
    W[2] += sum([learn_rate*e*x**2 for e,x in zip(e_list,X)])
else:
    print "iteractions:", i 
    min_w1 = W[0]
    min_w2 = W[1]
    min_w3 = W[2]

# print min_w1, min_w2
parabola = [ min_w3*x**2 +min_w2*x + min_w1 for x in X] # calculado pela rede
# print X, reta
plt.plot(X,Y,'ro', X, parabola, 'go')
# print("coeficiente angular:", min_w1, "coeficiente linear", min_w2)
# print min_list 

plt.show()



    

