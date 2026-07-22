import numpy as np

def outer_product(u, v):
    """
    Returns: float64 matrix of shape (m, n), the outer product u v^T.
    """
    u = np.asarray(u, dtype=np.float64).reshape(-1, 1)
    v = np.asarray(v, dtype=np.float64).reshape(-1, 1)
    M = u @ v.T
    return M
    pass