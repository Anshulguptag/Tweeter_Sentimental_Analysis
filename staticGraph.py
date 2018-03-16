import matplotlib.pyplot as plt
import numpy as np
import sys
import math
file=open("C:\\Users\\anshul\\jupyter\\sample.txt",'r').read()

lines=file.split('\n')
x=0
y=0
Y=[]
X=[]
for l in lines:
    x+=1
    X.append(x)
    if 'Positive' in l:
        y+=1
        Y.append(y)
    elif 'Negative' in l:
        y-=1
        Y.append(y)
    else:
        y=0
        Y.append(y)
X=np.array(X)
Y=np.array(Y)
C=[]
for i in range(len(X)):
    if i%1300==0:
        C.append(Y[i])
iter=np.arange(0,len(C),1)
plt.plot(iter,C,'o-',color='r')
plt.show()
