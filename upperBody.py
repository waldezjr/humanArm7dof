#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.ERobot import ERobot


class upperBody(ERobot):
    """
    Class that imports an upper body DHM

    ``upperBody()`` is a class which imports an Interbotix px100 robot definition
    from a URDF file.  The model describes its kinematic and graphical
    characteristics.



    Defined joint configurations are:

    - qz, zero joint angle configuration, 'L' shaped configuration
    - qr, vertical 'READY' configuration

    """

    def __init__(self):

        links, name, urdf_string, urdf_filepath = self.URDF_read(
            "/home/waldezjr/Projects/humanArm7dof/upperBody_description/upperBody.xacro"
        )

        super().__init__(
            links,
            name=name,
            manufacturer="dhm",
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )
        qzero = np.zeros(24)
        # left shoulder
        qzero[17] = -1.39626
        # left elbow
        qzero[20] = 0.610865
        # qzero[18] = 0.79
        # # right shoulder
        qzero[8] = 1.39626
        # left elbow
        qzero[11] = 0.523599
        self.addconfiguration("qz", qzero)
        # self.addconfiguration("qr", np.array([0, -0.3, 0, -2.2, 0, 2.0, np.pi / 4]))


if __name__ == "__main__":  # pragma nocover

    robot = upperBody()
    print(robot)