#Program to plot  the tangent of a circle
#Code by GVV Sharma
#Released under GNU GPL
#August 21, 2024

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')        #path to my scripts


#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
num= 100
#y = np.linspace(-2.5,2.5,num)

#Circle parameters
u = -e1
#u = np.array(([0,0])).reshape(-1,1)
f = -3
O,r = circ_param(u,f)
x_circ = circ_gen_num(O,r,num)

#tangent parameters
n = e2
q = circ_tang(n,u,r)

#Generate tangents
k1 = -1
k2 = 3 
c = (n.T@q).flatten()
x_A = line_norm(n,c[0],k1,k2)
x_B = line_norm(n,c[1],k1,k2)

plt.plot(x_A[0,:],x_A[1,:],label='Tangent 1')
plt.plot(x_B[0,:],x_B[1,:],label='Tangent 2')
plt.plot(x_circ[0,:],x_circ[1,:],label='Circle')

colors = np.arange(1,3)
#Labeling the coordinates
#tri_coords = np.block([A,B])
tri_coords = q
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['$\mathbf{A}$','$\mathbf{B}$']
#vert_labels = ['$\mathbf{D}$','$\mathbf{E}$']
for i, txt in enumerate(vert_labels):
#    plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-10,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

'''
#
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.legend(loc='lower right')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('chapters/12/6/3/19/figs/fig.pdf')
subprocess.run(shlex.split("termux-open chapters/12/6/3/19/figs/fig.pdf"))
#else
#plt.show()
