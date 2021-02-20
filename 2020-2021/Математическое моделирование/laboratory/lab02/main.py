from math import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plot

n=3.5
s=11.5
fi=pi*3/4

def f(tetha, r):
    dr=r/sqrt(n**2 - 1)
    return dr

r0=s/(n+1) #первый случай
#r0=s/(n-1) #второй случай

tetha = np.arange(0, 2*pi, 0.01)
r = odeint(f, r0, tetha)

def f2(t): #лодка браконьеров
    xt = tan(fi+pi)*t
    return xt

t=np.arange(0.00000000000001, 20)
r1=np.sqrt(t**2 + f2(t)**2)
tetha1=np.arctan(f2(t)/t)

rx=np.arange(r0, s, 0.01)
rx1=np.arange(0, r0, 0.01)
rx2=np.arange(0, s, 0.01)

tetha2=[0]*len(rx)
tetha3=[0]*len(rx1)
tetha4=[pi]*len(rx2)

plot.polar(tetha2, rx, 'red') #первый случай
#plot.polar(tetha3, rx1, 'red') #второй случай
#plot.polar(tetha4, rx2, 'red') #второй случай
plot.polar(tetha, r, 'red')
plot.polar(tetha1, r1, 'green')

tmp=0
for i in range(len(tetha)):
    if round(tetha[i], 2) == round(fi+pi, 2):
        tmp=i
print("Тета:", tetha[tmp], "r:", r[tmp][0])
print("X:", r[tmp][0]/sqrt(2), "Y:", -r[tmp][0]/sqrt(2))

plot.show()