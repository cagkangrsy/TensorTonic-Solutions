import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    N = len(A)
    M = len(A[0])
    
    B = np.zeros(shape=(M,N), dtype=float)
    
    for i in range(N):
        for j in range(M):
            B[j][i] = A[i][j]    

    return B
    pass
