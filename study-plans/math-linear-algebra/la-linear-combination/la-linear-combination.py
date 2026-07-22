import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """
    return (np.sum([c * np.asarray(v, dtype=np.float64) for v, c in zip(vectors, coefficients)],axis=0))
    pass