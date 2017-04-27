#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def phony_line_data(coef_ang=1, coef_lin=0, interval=(0,4),standard_deviation=2, size=100, plot=False, random=False):
    rnd = np.random.rand
    if random:
        coef_ang = 10*rnd() -5
        coef_lin = 10*rnd() -5
        interval = (5*rnd() -5, 5*rnd())
        standard_deviation = 5*rnd()
    interval_range = interval[1] -interval[0]
    X = [ interval_range*rnd() + interval[0] for _ in range(size)]
    Y = [ coef_ang*y + coef_lin + standard_deviation*rnd() - standard_deviation/2 for y in X]
    if plot:
        plt.plot(X,Y,'rx')
        plt.show()
    else:
        return X,Y
    
X, Y = phony_line_data(random=True)

rnd = np.random.rand # alias for random function
learn_rate = 0.001
W = [10*rnd()-5,  10*rnd()-5] # starting with any weight

for i in range(100):
    y = [Xi*W[0] + W[1] for Xi in X] # calculate every X with current Weights
    e_list = [(Yi - yi) for Yi, yi in zip(Y,y)]  # 
    W[0] += sum([learn_rate*e*x for x,e in zip(X,e_list)])
    W[1] += sum([learn_rate*e for e in e_list])
else:
    print "iteractions:", i 
    min_w1 = W[0]
    min_w2 = W[1]


reta = [ min_w1*x+min_w2  for x in X] # calculado pela rede
# print X, reta
plt.plot(X,Y,'ro', X, reta, 'g-')
print("coeficiente angular:", min_w1, "coeficiente linear", min_w2)
# print min_list 

plt.show()



    

