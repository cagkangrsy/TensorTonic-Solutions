import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """

    param = np.asarray(param)
    grad = np.asarray(grad)
    m = np.asarray(m)
    v = np.asarray(v)
    
    # Write code here
    m_new = np.dot(beta1, m) + np.dot((1 - beta1), grad)
    v_new = np.dot(beta2, v) + np.dot((1 - beta2), grad ** 2)

    m_new_h = m_new / (1 - beta1 ** t)
    v_new_h = v_new / (1 - beta2 ** t)

    param_new = param - lr * (m_new_h / (np.sqrt(v_new_h) + eps))

    return (param_new, m_new, v_new)
    pass