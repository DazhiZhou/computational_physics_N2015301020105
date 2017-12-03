# Three body simulation (Problem 4.16)
## Abstract
Carry out a true three-body simulation in which the motion of Earth, Jupiter, and the Sun are all calculated. Since all three bodies are 
now in motion, it is useful to take the center of mass of the three-bodies system as the origin, rather than the position of Sun. We also
suggest that you give Sun an initial velocity which makes the total momentum of the system exactly zero (So that the center of the mass 
will remain fixed). Study the motion of Earth with different initial conditions Also, try increasing the mass of Jupiter to 10, 100, and 
1000 times its true mass.
# Method
As we discussed before, the Eular method is not a good choice for oscillatory problems, and planetary motion is just such a problem. If we 
were to use the Eular method here we would find that the energy of the planet would grow with time, and it would spiral away from the Sun.
This difficulty is avoided with the Eular=Cromer method, since it converses energy exactly over the course of each orbit.
## Output
### Normal condition.(The mass of Jupiter is its real mass)
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic10-1.png)    
Plot the orbit with time t.   
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic10-2.png)    
### The mass of Jupiter is 10 times its real mass.    
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic10-3.png)    
Plot the orbit with time t.   
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic10-4.png)
### The mass of Jupiter is 100 times its real mass.   
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic10-5.png)    
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic10-6.png)
### The mass of Jupiter is 1000 times its real mass.    
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic10-7.png)
## Conclusion
    In normal condition, the orbit is stable.   
    As the mass of Jupiter increases, the orbit gradually becomes unstable.   
    When the mass of Jupiter is large enough, Jupiter will escape from the Sun. 
