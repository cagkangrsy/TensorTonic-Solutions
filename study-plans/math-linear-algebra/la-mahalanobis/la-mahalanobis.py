import numpy as np

def mahalanobis_distance(x, mean, cov):
    """
    Returns: float, the Mahalanobis distance from x to the distribution.
    """
    x = np.array(x, dtype=float)
    mean = np.array(mean, dtype=float)
    cov = np.array(cov, dtype=float)

    return np.sqrt((x - mean).T @ np.linalg.inv(cov) @ (x - mean))
    pass