import pylab as pl

from math import pi,cos,sin,exp
from scipy import constants
from scipy.constants import g


#FD=
FD=1.5
T=60
dt=T/1000
theta=['a']*1001
theta[0]=0.2
w=0
t=['a']*1001
t[0]=0
i=0

while i<1000:
    i0=i+1
    w=w-(sin(theta[i])+0.5*w-FD*sin((2/3)*t[i]))*dt
    theta[i0]=theta[i]+w*dt
    t[i0]=t[i]+dt
    if theta[i0]<-pi:
        theta[i0]=theta[i0]+2*pi
    elif theta[i0]>pi:
        theta[i0]=theta[i0]-2*pi
    else:
        theta[i0]=theta[i0]
    i=i+1
plot1,=pl.plot(t,theta,'r')


#FD=
FD=1.5
T=60
dt=T/1000
theta=['a']*1001
theta[0]=0.21
w=0
t=['a']*1001
t[0]=0
i=0

while i<1000:
    i0=i+1
    w=w-(sin(theta[i])+0.5*w-FD*sin((2/3)*t[i]))*dt
    theta[i0]=theta[i]+w*dt
    t[i0]=t[i]+dt
    if theta[i0]<-pi:
        theta[i0]=theta[i0]+2*pi
    elif theta[i0]>pi:
        theta[i0]=theta[i0]-2*pi
    else:
        theta[i0]=theta[i0]
    i=i+1
plot2,=pl.plot(t,theta,'b')

first_legend=pl.legend([plot1,plot2],['theta=0.2''theta=0.21'],bbox_to_anchor=(1.02, 1.3))