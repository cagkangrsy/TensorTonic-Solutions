import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)
    
    if np.sum(p) != 1:
        raise ValueError("Probabilites do not make up to 1.")

    if x.shape != p.shape:
        raise ValueError("Variable and probability shpaes do not match.")

    return np.dot(x,p) 
    pass
