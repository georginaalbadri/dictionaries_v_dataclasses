import numpy as np





def InputGeometry(L = 1, nx = 100):
    """
    Makes dictionary of geometry parameters

    Parameters
    ----------
    L : Length of the domain (float)
    nx : Number of grid points (int)
    """

    geometry = {'L': L, 'nx': nx, 'dx': L/nx}
    
    return geometry


def InputCellParameters(initial_volume_fraction = 0.1, diffusion_rate = 1e-3, cell_scaffold_drag = 1e-3, proliferation_rate = 0.0, death_rate = 0.0, cell_viscosity = 1e4, contact_inhibition = 0.0, cell_scaffold_traction = 0.0):
    """
    Makes dictionary of cell parameters

    Parameters
    ----------
    initial_volume_fraction : Initial volume fraction of the cells (float)
    diffusion_rate : Diffusion rate of the cells (float)
    cell_scaffold_drag : Drag coefficient of the cells (float)
    proliferation_rate : Proliferation rate of the cells (float)
    death_rate : Death rate of the cells (float)
    cell_viscosity : Viscosity of the cells (float)
    contact_inhibition : Contact inhibition of the cells (float)
    cell_scaffold_traction : Scaffold traction of the cells (float)
    
    """
    
    cell_parameters = {'initial_volume_fraction': initial_volume_fraction, 'diffusion_rate': diffusion_rate, 'cell_scaffold_drag': cell_scaffold_drag, 
                        'proliferation_rate': proliferation_rate, 'death_rate': death_rate, 'cell_viscosity': cell_viscosity, 
                        'contact_inhibition': contact_inhibition, 'cell_scaffold_traction': cell_scaffold_traction}

    return cell_parameters


def MakeInitialDistribution(geometry, cell_parameters, cell_distribution_option = 'uniform'):
    """
    Makes initial cell distribution 

    Parameters
    ----------
    geometry : Dictionary of geometry parameters (dict)
    cell_parameters : Dictionary of cell parameters (dict)
    cell_distribution_option : Initial cell distribution option, either uniform or noisy (str)

    Returns
    -------
    cell_distribution : Initial cell distribution (array)
    
    """

    if cell_distribution_option == 'uniform':
        initial_distribution = cell_parameters['initial_volume_fraction'] * np.ones(geometry['nx'])
    elif cell_distribution_option == 'noisy':
        np.random.seed(0) #fix noise distribution to be the same every time
        initial_distribution = cell_parameters['initial_volume_fraction'] + np.random.normal(0, cell_parameters['initial_volume_fraction']*0.1, geometry['nx'])
    else:
        print('cell_distribution_option not recognised')
    
    return initial_distribution
    



