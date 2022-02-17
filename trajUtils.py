from anyio import current_time
import spatialmath as sm
import spatialgeometry as sg
import numpy as np
import matplotlib.pyplot as plt

def minJerkGen3D(Tr_start , Tr_end, t_end, stepSize):
    nSteps = int(t_end / stepSize)+1
    print("Generating min jerk trajectory POSITION with %d steps, ending at %d seconds" %(nSteps, t_end)) 
    print("Start point is: ")
    Tr_start.printline()

    print("End point is: ")
    Tr_end.printline()

    traj = sm.SE3(Tr_start)
    # traj.printline()


    # Tr_start = 3 *Tr_start
    # print(Tr_start.t)
    
    for i in range(0,nSteps):
        # print(i)
    # i = 154
        curTime = i * (stepSize)
        tau = curTime / t_end
        # print(tau)
        p0 = Tr_start.t
        pf = Tr_end.t
        pMJ = p0 + (p0-pf) * (15*np.power(tau,4)  -6*np.power(tau,5)  -10*np.power(tau,3)) # from Flash, and Hogan 1985
        # print(pMJ)
        aux = sm.SE3(pMJ)
        traj.append(aux)

    return traj
    
    # print(len(traj))
    # traj[0].printline()
    # traj[int(2*nSteps/3)].printline()
    # traj[nSteps].printline()

    
    # traj.animate( dims=[-0.5, 2])

    # plt.show()

    




    





    
