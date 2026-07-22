import numpy as np

def gram_schmidt(vectors):
    """
    Returns: float64 array of shape (k, n), orthonormal basis spanning the input space.
    """
    orthonormal = []
    for v in vectors:
        v = np.asarray(v, dtype=np.float64)
        u = v
        for q in orthonormal:
            projection = np.dot(u,q) / np.dot(q,q) * q
            u = u - projection
        orthonormal.append(u / np.linalg.norm(u))

    return orthonormal
    pass