import roboticstoolbox as rtb
import spatialmath as sm
import spatialgeometry as sg
import numpy as np
from upperBody import upperBody
from roboticstoolbox.backends.swift import Swift  # instantiate 3D browser-based visualizer

dhm = upperBody()
print(dhm)

env = Swift()
env.launch(realtime=True)            # activate it

axes = sg.Axes(length=0.1)
env.add(axes)

print(dhm.n)

dhm.q=dhm.qz
env.add(dhm)
env.hold()

