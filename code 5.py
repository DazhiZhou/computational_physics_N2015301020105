from math import pi,cos,sin
from scipy import constants as const
import pylab as pl
import numpy
v0=input('The intial velocity v0=')
v0=float(v0)
alpha=input('The initial angle of the cannon shell alpha=')
alpha=float(alpha)
vx1=v0*cos(alpha)
vy1=v0*sin(alpha)
T=input('Time limit T=')
T=float(T)
dt=T/100
x=['a']*101
y=['a']*101
x[0]=0
y[0]=0.0000001
i=0

while i<100:
    if y[i]>0:
        i0=i+1
        x[i0]=x[i]+vx1*dt
        y[i0]=y[i]+vy1*dt
        vx1=vx1
        vy1=vy1-6378000*6378000*10*dt/((y[i0]+6378000)*(y[i0]+6378000))
        a=y[i0]
        b=x[i0]
        i=i+1
    else:
        i=i+1
        y[i]=0
        x[i]=b
b=numpy.max(y)       
pl.plot(x,y)
pl.xlim(0,x[100])
pl.ylim(0,b )
pl.xlabel('x')
pl.ylabel('y')




vx1=v0*cos(alpha)
vy1=v0*sin(alpha)
dt=T/100
x=['a']*101
y=['a']*101
x[0]=0
y[0]=0.0000001
i=0
while i<100:
    if y[i]>0:
        i0=i+1
        x[i0]=x[i]+vx1*dt
        y[i0]=y[i]+vy1*dt
        vx1=vx1
        vy1=vy1-10*dt
        a=y[i0]
        b=x[i0]
        i=i+1
    else:
        i=i+1
        y[i]=0
        x[i]=b
b=numpy.max(y)       
pl.plot(x,y,'r')


pl.show()
