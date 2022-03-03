# from trajUtils import *
import spatialmath as sm
import spatialgeometry as sg
import numpy as np
from trajUtils import minJerkGen3D
from upperBody import upperBody


import qpsolvers
class upperBodyQP:

    
    def __init__(self, methodName, dhmERbt ):

        # somehow i have to pass dhmERbt as a reference like a pointer in C... 
        self.isSet = False
        self.eRbt = dhmERbt  
        self.qpMethod = methodName
        self.nEq = 0
        self.nIneq = 0

        print("Trying to solve QP with method: "+ self.qpMethod)

        if(not(self.qpMethod in qpsolvers.available_solvers) ):
            expMsg = "method not available: "+ self.qpMethod            
            raise Exception(expMsg)

        # get joint position limits
        # get joint speed limits
        # get joint torque limits

        # create inequalities (upper and lower bounds)

        # create EoM equality
        self.createEoMEquality()
    
    def createEoMEquality(self):

        self.nEq = self.eRbt.n * 2 # the opt variable here is [q_dot_dot,tau] (with all joints actuated)

        self.A = np.array((self.nEq,self.nEq))

        self.A[:,0:self.eRbt.n] = self.eRbt.inertia(self.eRbt.q)
        return

