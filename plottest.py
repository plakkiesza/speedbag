import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math

tmp = 0

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-100, +100), ylim=(-1500, 1500))
lines = ax.plot( *([[], []]*4),lw=2 )#.plot([], [], lw=2)

import time
start_time = time.time()

filer = open('3-77hits.csv', 'r')
#filer = open('4-81hits.csv', 'r')
#filer = open('5-93hits.csv', 'r')
dtax = []
dtay = []
dtaz = []
dtat = []

for fline in filer:
    smpl = fline.split(',')
    dtax.append(int(smpl[1]))
    dtay.append(int(smpl[2]))
    dtaz.append(int(smpl[3]))
    dtat.append(math.sqrt(int(smpl[1])*int(smpl[1])+int(smpl[2])*int(smpl[2])+int(smpl[3])*int(smpl[3])))


# initialization function: plot the background of each frame
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# animation function.  This is called sequentially
def animate(i):
    global tmp
    x = np.linspace(-100, +100, 100)
    for j,line in enumerate(lines):
        if (j == 0):
            line.set_data([x, dtax[i:i+100]])
        if (j == 1):
            line.set_data([x, dtay[i:i+100]])
        if (j == 2):
            line.set_data([x, dtaz[i:i+100]])
        if (j == 3):
            line.set_data([x, dtat[i:i+100]])
    return lines


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
           frames=len(dtax)-101, interval=4, blit=True)

plt.show()
