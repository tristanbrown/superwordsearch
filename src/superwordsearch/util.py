"""Utility functions"""

import numpy as np

def get_coordinates(shape):
    """Get the coordinates of an ndarray in tuple (i, j) format.
    
    Takes:
        shape: (N, M), where N and M are integers
    Returns:
        A list of (i, j) tuples
    """
    idxs = np.indices(shape)
    return tuple_coords(idxs)

def tuple_coords(ndarr):
    """Converts a numpy representation of 2d coords into a list of tuples."""
    return list(zip(ndarr[0].flatten(), ndarr[1].flatten()))
