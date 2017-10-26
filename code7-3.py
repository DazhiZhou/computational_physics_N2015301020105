import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
fig=pl.figure()
ax=fig.add_subplot(111,projection='3d')

from math import pi,cos,sin,exp
from scipy import constants
from scipy.constants import g


#FD=0.1
FD=1.5
T=60
dt=T/1000
theta=['a']*1001
theta[0]=0.2
y=['a']*1001
z=['a']*1001
y[0]=sin(theta[0])
z[0]=-cos(theta[0])
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
    y[i0]=sin(theta[i0])
    z[i0]=-cos(theta[i0])
    i=i+1
plot1,=pl.plot(t,y,z,'r')



#FD=0.1
FD=1.5
T=60
dt=T/1000
theta=['a']*1001
theta[0]=0.21
y=['a']*1001
z=['a']*1001
y[0]=sin(theta[0])
z[0]=-cos(theta[0])
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
    y[i0]=sin(theta[i0])
    z[i0]=-cos(theta[i0])
    i=i+1
plot1,=pl.plot(t,y,z,'b')




pl.show()

