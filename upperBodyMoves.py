import roboticstoolbox as rtb
import spatialmath as sm
import spatialgeometry as sg
import numpy as np
from trajUtils import minJerkGen3D
from upperBody import upperBody
from roboticstoolbox.backends.swift import Swift  # instantiate 3D browser-based visualizer

# Define target
Tr_target = sm.SE3(0.35,-0.2,1.2) # x, y, z


dhm = upperBody()
print(dhm)

env = Swift()
env.launch(realtime=True)            # activate it

# show target
axes = sg.Axes(length=0.1, base=Tr_target)
env.add(axes)

# show robot
dhm.q=dhm.qz
env.add(dhm)
# move to target (min jerk trajectory)

# rtb-m already has a cool way of handling trajectories so lets give it a go...
time = np.arange(0, 2, 0.01) # 2 seconds, 0.01sec timestep

Tr0 = dhm.fkine(dhm.q); # fast is the C-wrapped implementation (like in Matlab)
print(Tr0)
# create min jerk trajectory (Cartesian)
Tr_start = sm.SE3(Tr0)

Tr_target = dhm.fkine(dhm.q)* sm.SE3.Tx(0.15) * sm.SE3.Ty(-0.1) * sm.SE3.Tz(0.2)
print(Tr_start)
# Tr_target.o(Tr_start.o)
Ts = rtb.tools.trajectory.ctraj(Tr_start, Tr_target, len(time))
# traj = minJerkGen3D(Tr_start,Tr_target,2,0.01)
# # solve for IK
# maskDhm= [1, 1, 1, 0, 0, 0]
# sol_qtraj = dhm.ikine_LMS(Ts, mask=maskDhm)
# # print(sol_qtraj)
# print(sol_qtraj.q.shape)

# # dhm.q = sol_qtraj.q[0]
# # env.step()

# i=0
# for t in time:
#     print('stepping')
#     dhm.q = sol_qtraj.q[i]
#     i=i+1
#     env.step(0.1)



env.hold() # hold browse open

# # # go to initial position
# # # dhm.plot(dhm.q)
# # # dhm.plot(dhm.qz, block=True)



