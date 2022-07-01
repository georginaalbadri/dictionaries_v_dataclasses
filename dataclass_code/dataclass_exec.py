import numpy as np
from SolverCell_1D import cell_solver_1D


def ExecFunc(endothelial, geometry, num_iter = 100, dt = 0.01):

    # Solve the system
    iter=0

    while iter < num_iter:
        endothelial.distribution = cell_solver_1D(endothelial.distribution, vn=np.zeros(geometry.nx), D=endothelial.diffusion_rate, nx=geometry.nx, dx=geometry.dx, dt=1e-2)
        iter+=1     

    return endothelial.distribution