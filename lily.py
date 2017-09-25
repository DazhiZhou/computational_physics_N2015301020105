 
 
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
 
 
def update_point(num):
    fig_points.set_data(data[:, 0:num])
    return fig_points,
 
fig1 = plt.figure()
 
num_point = 41
data = np.array([[0.01,0.01,0.01,0.01,0.01,0.01,0.1,0.2,0.4,0.4,0.4,0.4,
                  0.5,0.5,0.5,0.5,0.5,0.5,0.6,0.7,0.8,0.8,0.8,0.9,1,1,1,1,1,1,
                  0.9,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8],
                 [0.3,0.4,0.5,0.6,0.7,0.8,0.3,0.3,0.3,0.4,0.5,0.7,0.8,
                  0.7,0.6,0.5,0.4,0.3,0.3,0.4,0.5,0.4,0.3,0.3,0.3,0.5,0.4,0.2,
                  0.1,0,0,0,0,0,0,0,0,0,0,0,0]])
fig_points, = plt.plot([], [], 'ro')
 
plt.xlim(0, 1.1)
plt.ylim(-0.1, 1)
plt.xlabel('x')
plt.title('Animata Lily')
 
# interval
# repeat
# frames
# fargs
# init_func
anim = animation.FuncAnimation(fig1, update_point,num_point)
 
#anim = animation.FuncAnimation(fig1, update_point,frames=num_point, interval=50, blit=False, repeat=False)
 
plt.show()

