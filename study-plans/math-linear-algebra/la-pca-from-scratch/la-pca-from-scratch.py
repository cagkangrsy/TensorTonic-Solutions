import numpy as np

def pca_project(X, n_components):
    """
    Returns: ndarray of shape (n_samples, n_components), the projected data.
    """
    X = np.asarray(X, dtype=np.float64)
    X_bar = X - X.mean(axis=0)
    C = (X_bar.T @ X_bar) / (X.shape[0] - 1)

    eigenvalues, eigenvectors = np.linalg.eigh(C)  
    idx = np.argsort(eigenvalues)[::-1]
    V_k = eigenvectors[:, idx][:, :n_components]
    return X_bar @ V_k
    pass