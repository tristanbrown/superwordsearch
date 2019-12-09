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

def out_of_bounds(coord, shape):
    neg = np.where(coord < 0, True, False)
    greater = np.where(coord >= np.array(list(shape)), True, False)
    if any(neg) or any(greater):
        return True
    else:
        return False

def wrap(coord, shape):
    coord = np.where(coord < 0, coord + shape, coord)
    return np.where(coord >= shape, coord - shape, coord)
