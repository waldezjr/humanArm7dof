import trajUtils
import spatialmath as sm
import spatialgeometry as sg
import matplotlib.pyplot as plt

Tr_start = sm.SE3(0,0,0) # x, y, z
Tr_end = sm.SE3(0.5,-0.2,1.7) # x, y, z

T_mj = trajUtils.minJerkGen3D(Tr_start,Tr_end,15.4, 0.1)

T_mj.animate()
plt.show()