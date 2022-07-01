import numpy as np
from dataclasses import dataclass



@dataclass
class Geometry1D:

    L: float = 1.0
    nx: int = 100
    dx: float = L/nx

    

@dataclass
class CellType:

    name: str
    diffusion_rate: float
    proliferation_rate: float = 0.0
    death_rate: float = 0.0
    initial_volume_fraction: float = 0.1

    def uniform_cell_distribution(self, geometry):
        """
        Makes uniform cell distribution

        Parameters
        ----------
        geometry : Dictionary of geometry parameters (dict)

        Returns
        -------
        cell_distribution : Initial cell distribution (array)

        """
        distribution = self.initial_volume_fraction * np.ones(geometry.nx)
        return distribution

    def noisy_cell_distribution(self, geometry):
        """
        Makes noisy cell distribution

        Parameters
        ----------
        geometry : Dictionary of geometry parameters (dict)

        Returns
        -------
        cell_distribution : Initial cell distribution (array)
        
        """
        np.random.seed(0) #fix noise distribution to be the same every time
        distribution = self.initial_volume_fraction + np.random.normal(0, 0.1*self.initial_volume_fraction, geometry.nx)
        return distribution





