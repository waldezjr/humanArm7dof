import roboticstoolbox as rtb
import spatialmath as sm
import spatialgeometry as sg
import numpy as np

from roboticstoolbox.backends.swift import Swift  # instantiate 3D browser-based visualizer
env = Swift()
env.launch(realtime=True)            # activate it


# Make a panda model and set its joint angles to the ready joint configuration
panda = rtb.models.Panda()
panda.q = panda.qr

# Set a desired and effector pose an an offset from the current end-effector pose
env.add(panda, robot_alpha=0.5)
Tep = panda.fkine(panda.q) * sm.SE3.Tx(0) * sm.SE3.Ty(-0.1) * sm.SE3.Tz(0) * sm.SE3.Rz(30,'deg')

axes = sg.Axes(length=0.1, base =Tep)

# Add the robot to the simulator
env.add(axes)


# Simulate the robot while it has not arrived at the goal
arrived = False
while not arrived:

    # Work out the required end-effector velocity to go towards the goal
    v, arrived = rtb.p_servo(panda.fkine(panda.q), Tep,gain=0.1, threshold=0.01)
    
    # Set the Panda's joint velocities
    panda.qd = np.linalg.pinv(panda.jacobe(panda.q, fast=True)) @ v
    
    # Step the simulator by 50 milliseconds
    env.step(0.05)

env.hold()