import numpy as np
from dataclass_setup import Geometry1D, CellType
from SolverCell_1D import cell_solver_1D
from dataclass_exec import ExecFunc
import matplotlib.pyplot as plt
import time



start = time.time()

# Define the geometry
geometry = Geometry1D

# Define the cell type
endothelial = CellType(name='endothelial', diffusion_rate=1e-3, initial_volume_fraction=0.1)

# Set the initial conditions
endothelial.distribution = endothelial.noisy_cell_distribution(geometry)

initial_endothelial_distribution = endothelial.distribution

# Solve the system
endothelial.distribution = ExecFunc(endothelial, geometry, num_iter=100)

end = time.time()

print('time taken:', end - start)

plt.plot(initial_endothelial_distribution, label='initial endothelial distribution')
plt.plot(endothelial.distribution, label = 'endothelial distribution')
plt.legend()
plt.savefig('cell_diff_dataclass_output.png', dpi = 300)
plt.show()

