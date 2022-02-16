from numpy import block
import roboticstoolbox as rtb
from sqlalchemy import true
robot = rtb.models.DH.Panda()
print(robot)

T = robot.fkine(robot.qz)  # forward kinematics
print(T)

from spatialmath import SE3


# We can solve inverse kinematics very easily. We first choose an SE(3) pose defined in terms of position and orientation (end-effector z-axis down (A=-Z) and finger orientation parallel to y-axis (O=+Y)).
T = SE3(0.7, 0.2, 0.1) * SE3.OA([0, 1, 0], [0, 0, -1])
sol = robot.ikine_LM(T)         # solve IK
print(sol)

q_pickup = sol.q
print(robot.fkine(q_pickup))    # FK shows that desired end-effector pose was achieved

qt = rtb.jtraj(robot.qz, q_pickup, 50)
# robot.plot(qt.q, movie='panda1.gif', limits = [-1,1,-0.5,0.5,0,1])
robot.teach(q_pickup,limits = [-1,1,-0.5,0.5,0,1])