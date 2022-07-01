import numpy as np 
from scipy import sparse
from scipy.sparse.linalg import spsolve



# ------------------------------------------------------------------------

def cell_solver_1D(n, vn, D, nx, dx, dt): 

    """
    Solves 1D advection-diffusion equation using central-space and backward-time finite difference scheme.
    No flux boundary conditions.
    No cell proliferation or death included.

    Parameters
    ----------
    n0 : cell distribution (numpy array)
    vn : cell velocity (numpy array)
    D : cell diffusion rate (float)
    nx : number of grid points (int)
    dx : grid spacing (float)
    dt : time step (float)

    """

    #-- matrix A (An = B)

    diagonals = list((2 * D) + (dx / 2) * (vn[2:nx] - vn[0:nx-2]) + (dx**2 / dt))
    diagonals.insert(0, (2 * D) +  (dx / 2) * (-3*vn[0] + 4*vn[1] - vn[2]) + (dx**2 / dt))
    diagonals.append((2 * D) + (dx / 2) * (3*vn[nx-1] - 4*vn[nx-2] + vn[nx-3]) + (dx**2 / dt))

    below = list(- ((dx * vn[1:nx-1]) / 2) - D)
    below.append(- 2 * D)

    above = list(((dx * vn[1:nx-1]) / 2) - D)
    above.insert(0,  - 2 * D)

    A = sparse.diags([diagonals, below, above], [0, -1, 1])

    A = sparse.csr_matrix(A)

    #-- source terms B

    B = np.zeros((nx))
    
    B[:nx] =  (dx**2 * n[:nx] / dt)

    #-- solve matrix equation for n

    n = spsolve(A, B)
    
    return n

# ------------------------------------------------------------------------ 
