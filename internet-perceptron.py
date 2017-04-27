#Yes I have deleted. thanks a lot. I have the code . 
# My features are x, sin(x),cos(x),mean(x),sin(mean(x)),cos(mean(x)) 
# and same with standard deviation. you can replace the features. 


import numpy as np
import pandas as pd
import random as rn


a=pd.DataFrame
# a=pd.read_csv('F:\\ann\processed.csv')

earray=[]
mu=0.1

w11=rn.uniform(0,1)
w12=rn.uniform(0,1)
w13=rn.uniform(0,1)

w21=rn.uniform(0,1)
w22=rn.uniform(0,1)
w23=rn.uniform(0,1)

w31=rn.uniform(0,1)
w32=rn.uniform(0,1)
w33=rn.uniform(0,1)

length=len(a)

for j in range(0,250):
sum=0
for i in range(0,length):

x10=a.ix[i,1]/100
mean=a.ix[i,2]/100
dev=a.ix[i,3]/100
y=a.ix[i,4]/100



f11=x10
f12=np.sin(x10)
f13=np.cos(x10)

f21=mean
f22=np.sin(mean) 
f23=np.cos(mean)

f31=dev
f32=np.sin(dev)
f33=np.cos(dev)

y1=(w11*f11 + w12*f12 + w13*f13)+(w21*f21 + w22*f22 + w23*f23)+(w31*f31 + w32*f32 + w33*f33)

# print str(y)+" "+ str(y1)
# print "calculated result "+ str(y)
e=y-y1

# print "error "+str(e)

sum=sum+e
# print "error "+str(e)
avgerror=sum/998
earray.append(avgerror)
print avgerror
w11=w11 + mu*avgerror*f11
w12=w12 + mu*avgerror*f12
w13=w13 + mu*avgerror*f13

w21=w21 + mu*avgerror*f21
w22=w22 + mu*avgerror*f22
w23=w23 + mu*avgerror*f23

w31=w31 + mu*avgerror*f31
w32=w32 + mu*avgerror*f32
w33=w33 + mu*avgerror*f33


print w11
print w12
print w13 

print w21
print w22
print w23 

print w31
print w32
print w33 

x10=float(raw_input("x10: "))
mean=float(raw_input("mean: "))
dev=float(raw_input("dev: "))

f11=x10
f12=np.sin(x10)
f13=np.cos(x10)

f21=mean
f22=np.sin(mean) 
f23=np.cos(mean)

f31=dev
f32=np.sin(dev)
f33=np.cos(dev)
y1=(w11*f11 + w12*f12 + w13*f13)+(w21*f21 + w22*f22 + w23*f23)+(w31*f31 + w32*f32 + w33*f33) 
print y1
