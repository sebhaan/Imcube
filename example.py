# Simple Example
from __future__ import print_function
import numpy as np
import cubeshow as cs
from matplotlib import cm
import matplotlib.pyplot as plt
reload(cs)

Ncube = 10 # NUmber of voxels along each axis
Lcube = 100 # Lenght of cube in meters
voxsize = Lcube / Ncube # size of one voxel in meters

cgen = (np.linspace(1,Ncube,Ncube) - 0.5) * voxsize

# coordinate array for geophysical properties
x3, y3, z3 = np.meshgrid(cgen, cgen, cgen)

r = np.sqrt((x3-Lcube/2)**2 + (y3-Lcube/2)**2 + (z3-Lcube/2)**2)

zshift = Lcube/3. * 1. / (1 + np.exp(0.2*(-y3 + Lcube/2))) 
density = 1. + Lcube/10. * (1./(1+np.exp(-5*(z3 - Lcube * 4/10. + zshift) )) - 1./(1+np.exp(-5*(z3 - Lcube * 6/10. + zshift))))
magnetic = 10. * np.exp(-0.05*r)
mask = np.zeros_like(magnetic)
mask[density < 3] = 1

# plot voxel model
ic = cs.imcube()
ic.cubeshow(density, data_color=magnetic, mask = mask, colorscheme = cm.jet, voxelsize = (voxsize,voxsize,voxsize), offset = (0,0,-100), show = True, savefig = False)


