import numpy as np
from SolverCell_1D import cell_solver_1D


def ExecFunc(cell_params, geometry, num_iter = 100, dt = 0.01):

    # Solve the system
    iter=0

    while iter < num_iter:
        cell_params['cell_distribution'] = cell_solver_1D(cell_params['cell_distribution'], vn=np.zeros(geometry['nx']), D=cell_params['diffusion_rate'], nx=geometry['nx'], dx=geometry['dx'], dt=dt)
        iter+=1     

    return cell_params['cell_distribution']