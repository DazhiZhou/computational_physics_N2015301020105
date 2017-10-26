# Oscillatory Motion and Chaos(Problem 3.10, 3.13)
## Abstract
Caculate the angular of the pendulum for different amplitudes of the driving force (0.1,0.5, and 0.99), with the other parameters as in 
Figure 3.6 in the textbook 'Computational Physics'. Compare the waveforms, with special attention  to the deviations from a purely
sinusolidal form at high drive.   
Write a program to caculate and compare the behavior of two, nearly identical pendulums. Use it to caculate the divergence of two nearby 
trajectories in the chaotic regime.
## Method
### Eular Cromer method
Until now, we have used Eular method solved a series of differential equations. However, when it comes to the problem of pendulum, it 
turns out that the difficulty lies with our use of the Eular method. As was emphasized when we first introduced this method, it proves 
us with an approximate estimate of the solution to our differential equations. Again, the emphasize is the word approximate. We have 
already mentioned that the errors involved in using the Eular method become smaller as the step is made smaller. At this point you 
might sense a contradiction. The reasults calculated by Eular metod show that both the amplitude of the oscillations and the total energy
increase with time.   
We are thus led to consider other method for solving ordinary differential equations. Its turns out that a simple modification of the 
Eular metod yields an algorithm that is also quite suitable. This modification yields what is known as the Eular Cromer metod. To 
appreciate the Eular Cromer metod, we reconsider our program. Given below is a modified version of the calculate subroutine.

![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic7-1.png)
## Output
### Compare graphs of the pendulums with different FD
[source code7-1](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/code7-1.py)    
With different amplitudes of the driving force, the waveforms is also different.    
And if it is at high drive, chaos will come.
    
    The initial theta=0.2   
    The initial angular velocity=0    
    FD1=0.1 FD2=0.5 FD3=0.99 
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic7-2.png)

When drive is high enough, chaos will come
    
    The initial theta=0.2   
    The initial angular velocity=0    
    FD=1.5
    
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic7-4.png)

Expand the trajectory by t axis
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic7-5.png)

### Compare the behavior of two, nearly identical pendulums.(Make a comparision in 2d canvas)
[source code7-2](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/code7-2.py)
    
    The initial theta=0.2,0.21   
    The initial angular velocity=0 
    FD=1.5    
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic7-3.png)
### Compare the behavior of two, nearly identical pendulums.(Make a comparision in 3d canvas)
[sorce code 7-3](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/code7-3.py)
    
    The initial theta=0.2   
    The initial angular velocity=0    
    FD=1.5    
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic7-6.png)
## Conclusion
If the drive is high enough, our system is thus both deterministic and unpredictable. Put another way, a system can obey certain 
deterministic laws of physics, but still exhibit behavior that is unpredictable due to an extreme sensitivity to initial conditions.
