# Exercise 4:Use Python to imitate the population growth
## Abstract
Population growth problems often give rise to rate equations that are first-order, like this one
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/exercise4-1.png)
The first problem is solving it with b=0 using Euler method.    
    The second problem is solving it respectively with a=10,b=3 and a=10,b=0,01
## Method 
It is clear that we use the same method to solve the problems.    
Here is the step.   
First we get the initial data from outside.
Second make two vacant lists with 10000001 sits each, which will be used to store data for the graph.   
Third, with the hlep of Do loop, we can use Euler method to calculate the population incessantly, which will be stored inthe list we creat 
before.
At last, just plot the graph.
## Output
### When b=0 a=10 initial data N0=1 T=1 [source code4-1](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/code4-1.py)
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/exercise4-2.png)
### When b=3 a=10 initaldata: N0=1 T=1  [source code4-2](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/code4-2.py)
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/exercise4-3.png)
### When b=0.01 a=10 N0=1000 
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/exercise4-4.png)
It is strange, isn't? If we make a simple calculation, we will find that the poplulation won't change when we use Euler method. It is attributed 
the initial data. if we change the data as N0=100, we wii get a graph like the last one 
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/exercise4-5.png)
