# Motion of a Battle Ball(Problem2.8)
## Abstract
Use the Euler method to calculate cannon shell tracjetories ibnoring both air drag and effect of air density.   
In our model of cannon shell trajectory we have assumed that the acceleration due to the gravity, g, is a constant. It will, of course, 
depend on altitude. Add this to the model and calculate how much it affects the range.
## Method
In general, we use Euler method to sove the secod-order differential equations, which is similar to the the first-order differential 
equations when it comes to the solving method.    
It is clear that we can solve a second-order differential equation by deviding it into two fisrt-order differential equations.Then, 
use Euler equation twice, like this way.    
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic5-1.png)
Where 'a' is the acceleration of the cannon shell
Then, we have 
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic5-2.png)
## The Pseudocode.   
    Declare necessary variables, including list y and x to store the data
    Use the formula above to do the real calculation where the acceleration is related to the altitude, y.
    Use the formula above to do the real calculation where the acceleration is a constant,g. 
    Sketch the graph to make a comparison.
## Output
Firt we use the intial volocity v0 300/s, alpha 1
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic5-3.png)
In fact we can only see one graph, which means the altitude is not high enough to let the variable acceleration change the trajectory
we choose a faster volocity.
![](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/pic5-4.png)
## Conclusion
When the altitude is not high enough, the difference of trajectories caused by the altitude is not conspious. However, when it reaches 
about 600km, we can recognize the difference caused by altitude.    
By the way, in fact, if without a comparision, it is hard to recognize whether it is the graph where the accelration is related to altitude.
## Appendix the source code 
[Source code 05](https://github.com/yyx1996/computational_physics_N2015301020105/blob/master/code%205.py)
