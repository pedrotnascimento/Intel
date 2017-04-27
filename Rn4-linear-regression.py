#!/usr/bin/env python
# -*- coding: utf-8 -*-

# baseado em
#https://pt.slideshare.net/MostafaGMMostafa/neural-networks-least-mean-square-lsm-algorithm
import matplotlib.pyplot as plt
import numpy as np

def phony_line_data(coef_ang=1, coef_lin=0, interval=(0,4),standard_deviation=2, size=100, plot=False, random=True):
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
    
X, Y = phony_line_data(random=True)

e_min= 9999
rnd = np.random.rand
tam = 100
W = [ (10*rnd()-5, 10*rnd()-5) for _ in range(tam)]
min_list =[]
for w,i in zip(W,range(tam)):
    y = [ Xi*w[0] + w[1] for Xi in X]
    
    # cost-function ref: https://pt.coursera.org/learn/machine-learning/lecture/rkTp3/cost-function
    e_list =  [ (Yi - yi)**2 for Yi, yi in zip(Y,y)]
    e = sum(e_list)/(2*len(Y)) 
    
    if e < e_min:
        e_min = e
        min_w1 = w[0]
        min_w2 = w[1]
        a = [e_min]
        min_list.append(a)
        print a 
else:
    print "iteractions:", i 


# estimativa feita a mão
#reta = [ -0.25*x+1.8  for x in xrange(5)] # insumo para pesquisa de pesos
reta = [ min_w1*x+min_w2  for x in X] # calculado pela rede
plt.plot(X,Y,'rx', X, reta, 'g-')
print("coeficiente angular:", min_w1, "coeficiente linear", min_w2)
print min_list 

plt.show()



    

