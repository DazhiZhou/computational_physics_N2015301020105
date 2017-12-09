# Laplace's equation(Problem 5.3)
## Abstract
Use the symmetry of the capacitor problem to write a program that obtains the results by calculating the potential in only one quadrant of 
the x-y plane.
## Method 
As we solve the Laplace's equation    
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic11-1.png)    
we can reduce it as   
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic11-2.png)
We now require a numerical strategy for determining this function, assuming only that V is known at boundaries. We can't just start one of 
the boundaries and work our way into and across the system, since according to the laat equation we need to know V at all of the neighbors 
in order to calculate its value at any particular point. The approach we take is to begin with some initial guss for the sollution; call 
it V0(i,j,k). In general, unless we are extramely clever, the guss we make will not satify the Laplace' equation everywhere. To obtain a 
improved guss, we use the last equation to calculate new values of V, V1, using V0 on the right-hand side. We then repeat the procedure 
with V1 to obtain an even better guss, V2. This iterative procee is continued until our result satisfies some convergence criteri, which 
we will discuss shortly. The main point is that we can we can iterate the procedure to obtain a better and better solution. This general 
approach is called the ralaxation method, as is a useful way to deal wirh several important classes of partial defferential equations.
## Output
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic11-3.png)
