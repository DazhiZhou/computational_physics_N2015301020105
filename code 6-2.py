import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
fig=pl.figure()
ax=fig.add_subplot(111,projection='3d')
#creat a 3d canvas

from math import pi,cos,sin,exp
from scipy import constants as const
from numpy import power
#import the tools that will help

#w1 
vx=10
vy=0
vz=10
T=10
dt=T/1000
x=['a']*1001
y=['a']*1001
z=['a']*1001
x[0]=0
y[0]=0
z[0]=1.5
i=0#will be used in circle
w=0.2*2*const.pi #the angular velocity
theta=0
theta=(theta*const.pi)/180 #the intial angular orientation
ay=5*(sin(4*theta)-0.25*sin(8*theta)+0.08*sin(12*theta)-0.025*sin(16*theta))
az=-10
#initial the varibles

while i<1000:
    if z[i]>0:
        i0=i+1
        x[i0]=x[i]+vx*dt
        y[i0]=y[i]+vy*dt
        z[i0]=z[i]+vz*dt
        a=x[i0]
        b=y[i0]
        vx=vx
        vy=vy+ay*dt
        vz=vz+az*dt
        ax=0
        ay=5*(sin(4*theta)-0.25*sin(8*theta)+0.08*sin(12*theta)-0.025*sin(16*theta))
        az=-10
        theta=theta+w*dt
        i=i+1
    else:
        i=i+1
        z[i]=0
        x[i]=a
        y[i]=b
plot1,=pl.plot(x,y,z,'r')




#w2
vx=10
vy=0
vz=10
T=10
dt=T/1000
x=['a']*1001
y=['a']*1001
z=['a']*1001
x[0]=0
y[0]=0
z[0]=1.5
i=0#will be used in circle
w=0.2*2*const.pi #the angular velocity
theta=20
theta=(theta*const.pi)/180 #the intial angular orientation
ay=5*(sin(4*theta)-0.25*sin(8*theta)+0.08*sin(12*theta)-0.025*sin(16*theta))
az=-10
#initial the varibles

while i<1000:
    if z[i]>0:
        i0=i+1
        x[i0]=x[i]+vx*dt
        y[i0]=y[i]+vy*dt
        z[i0]=z[i]+vz*dt
        a=x[i0]
        b=y[i0]
        vx=vx
        vy=vy+ay*dt
        vz=vz+az*dt
        ax=0
        ay=5*(sin(4*theta)-0.25*sin(8*theta)+0.08*sin(12*theta)-0.025*sin(16*theta))
        az=-10
        theta=theta+w*dt
        i=i+1
    else:
        i=i+1
        z[i]=0
        x[i]=a
        y[i]=b
plot2,=pl.plot(x,y,z,'b')


#w3
vx=10
vy=0
vz=10
T=10
dt=T/1000
x=['a']*1001
y=['a']*1001
z=['a']*1001
x[0]=0
y[0]=0
z[0]=1.5
i=0#will be used in circle
w=0.2*2*const.pi #the angular velocity
theta=40
theta=(theta*const.pi)/180 #the intial angular orientation
ay=5*(sin(4*theta)-0.25*sin(8*theta)+0.08*sin(12*theta)-0.025*sin(16*theta))
az=-10
#initial the varibles

while i<1000:
    if z[i]>0:
        i0=i+1
        x[i0]=x[i]+vx*dt
        y[i0]=y[i]+vy*dt
        z[i0]=z[i]+vz*dt
        a=x[i0]
        b=y[i0]
        vx=vx
        vy=vy+ay*dt
        vz=vz+az*dt
        ax=0
        ay=5*(sin(4*theta)-0.25*sin(8*theta)+0.08*sin(12*theta)-0.025*sin(16*theta))
        az=-10
        theta=theta+w*dt
        i=i+1
    else:
        i=i+1
        z[i]=0
        x[i]=a
        y[i]=b
plot3,=pl.plot(x,y,z,'g')

#w4
vx=10
vy=0
vz=10
T=10
dt=T/1000
x=['a']*1001
y=['a']*1001
z=['a']*1001
x[0]=0
y[0]=0
z[0]=1.5
i=0#will be used in circle
w=0.2*2*const.pi #the angular velocity
theta=60
theta=(theta*const.pi)/180 #the intial angular orientation
ay=5*(sin(4*theta)-0.25*sin(8*theta)+0.08*sin(12*theta)-0.025*sin(16*theta))
az=-10
#initial the varibles

while i<1000:
    if z[i]>0:
        i0=i+1
        x[i0]=x[i]+vx*dt
        y[i0]=y[i]+vy*dt
        z[i0]=z[i]+vz*dt
        a=x[i0]
        b=y[i0]
        vx=vx
        vy=vy+ay*dt
        vz=vz+az*dt
        ax=0
        ay=5*(sin(4*theta)-0.25*sin(8*theta)+0.08*sin(12*theta)-0.025*sin(16*theta))
        az=-10
        theta=theta+w*dt
        i=i+1
    else:
        i=i+1
        z[i]=0
        x[i]=a
        y[i]=b
plot4,=pl.plot(x,y,z,'y')

first_legend=pl.legend([plot1,plot2,plot3,plot4],['theta1','theta2','theta3','theta4'])
pl.show  
  





