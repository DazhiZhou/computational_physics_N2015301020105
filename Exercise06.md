# Motion of a baseball(Problem2.17)
## Abstract
Investigate the trajectories of the knuckleballs as a function of the angular velocity w, the initial angular orientation, and the (center
of mass)  velocity.     
In fact, a well-thrown knuckleball might complete only half of a revolution om its way to the plate, so a stitch will be exposed for a 
significant amount of time. 
## Method
In general, we will use Euler method to sove the secod-order differential equations as we did before.   
Beside, for the sake of showing the deviation caused by the lateral force, we will use a 3d canva to sketch the graph of the 
trajectories.    
It is easy to realize it by mpl_toolkits.mplot3d
```python
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
fig=pl.figure()
ax=fig.add_subplot(111,projection='3d')
```
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic6-1.png)   
Then, lets talk about the mechanics in baseball.    
The difference between trajectories of the cannon shell and the base ball is the deviation casued by the lateral force. We just need
 to add a horizontal acceleration to the cannon shell's mechanics formula.
 ## The Pseudocode
    Creat a 3d canva
    Declare necessary variables, including list y and x to store the data
    Use the mechanics formula to do the calculation where the acceleration projected to y axis is related to the angular orientation w.
    Use several  sets of initial data to the calculation.
    Sketch the graph
## Output
### Make a comparision between trajectories of baseballs exerted lateral force or not.
    The initial variables
    x=0  y=0  z=1.5
    vx=30  vy=0  vz=30
    theta=30 w=0.4pi
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic6-2.png)
### Discuss the relations between the trajectories and w
![code 6-1](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/code%206-1.py)    
   
    x=0  y=0  z=1.5
    vx=30  vy=0  vz=30
    theta=30 w1=0.2pi w2=0.4pi w3=0.6pi w4=0.8pi
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic6-3.png)
### Discuss the relation between the trajectories and initial orientation
![code6-2](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/code%206-2.py)   

    The initial variables
    x=0  y=0  z=1.5
    vx=30  vy=0  vz=30
    theta1=0 theta2=20 theta3=40 theta4=60 w=0.4pi
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic6-4.png)
## Conclusion
Knuckleball's trajectories is significantly effected by the initial orientation and the angular velocity.
In fact, the picher can not control the angular velocity accurately enough, so nobady knows where the baseball will go.
    
