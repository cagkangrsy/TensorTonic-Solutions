import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    if len(x) != len(y):
        raise ValueError
    else:
        return np.sqrt(np.sum([(i-j)**2 for i, j in zip(x, y)]))
    pass