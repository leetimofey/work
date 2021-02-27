from numpy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x0=61000
y0=45000
t0=0
tmax=1
dt=0.05
t=arange(t0, tmax, dt)
v0=[x0, y0]
print("Какую модель вывести (1 или 2)?")
check=int(input())
if check==1:
    #первая модель
    a=0.22
    b=0.82
    c=0.45
    h=0.67
    def P(t):
        return sin(4*t)
    def Q(t):
        return cos(4*t)
    def DU(y, t):
        dy1=-a*y[0]-b*y[1]+P(t)
        dy2=-c*y[0]-h*y[1]+Q(t)
        return [dy1, dy2]
    y=odeint(DU,v0,t)
    res1=[i[0] for i in y]
    res2=[j[1] for j in y]
    plt.plot(t, res1, 'blue', label='X') #первая армия
    plt.plot(t, res2, 'red', label='Y') #вторая армия
    plt.title('Первая модель')
    plt.xlabel('время')
    plt.ylabel('численность армий')
    plt.ylim(0, None)
    plt.grid(True)
    plt.show()
elif check==2:
    #вторая модель
    a2=0.28
    b2=0.83
    c2=0.31
    h2=0.75
    def P2(t):
        return 1.5*sin(t)
    def Q2(t):
        return 1.5*cos(t)
    def DU2(y, t):
        dy3=-a2*y[0]-b2*y[1]+P2(t)
        dy4=-c2*y[0]*y[1]-h2*y[1]+Q2(t)
        return [dy3, dy4]
    y2=odeint(DU2,v0,t)
    res3=[i[0] for i in y2]
    res4=[j[1] for j in y2]
    plt.plot(t, res3, 'blue', label='X') #первая армия
    plt.plot(t, res4, 'red', label='Y') #вторая армия
    plt.title('Вторая модель')
    plt.xlabel('время')
    plt.ylabel('численность армий')
    plt.ylim(0, None)
    plt.grid(True)
    plt.show()