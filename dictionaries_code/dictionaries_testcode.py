import numpy as np
from dictionaries_setup import InputGeometry, InputCellParameters, MakeInitialDistribution
from SolverCell_1D import cell_solver_1D
from dictionaries_exec import ExecFunc
import matplotlib.pyplot as plt
import time



start = time.time()

# Make the geometry dictionary
geometry = InputGeometry()

# Make the cell type dictionary
cell_parameters = InputCellParameters(initial_volume_fraction = 0.1, diffusion_rate = 1e-3)

# Set the initial conditions
cell_parameters['cell_distribution'] = MakeInitialDistribution(geometry, cell_parameters, cell_distribution_option = 'noisy')

initial_cell_distribution = cell_parameters['cell_distribution']

# Solve the system
cell_parameters['cell_distribution'] = ExecFunc(cell_parameters, geometry, num_iter=100)

end = time.time()

print('time taken:', end - start)

plt.plot(initial_cell_distribution, label='initial cell distribution')
plt.plot(cell_parameters['cell_distribution'], label='cell distribution')
plt.legend()
plt.savefig('cell_diff_dictionaries_output.png', dpi = 300)
plt.show()