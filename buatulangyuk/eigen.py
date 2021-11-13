import numpy as np
from numpy.core.fromnumeric import transpose
import math

def createEigen(A):
    eig_normalize = np.eye(A.shape[0])
    eig_value=A.copy()
    for i in range(5):
            Q,R = np.linalg.qr(eig_value)
            eig_normalize = eig_normalize @ Q
            eig_value = R @ Q
    return eig_value, eig_normalize

def createSigma(eigenvalue):
    sigma = np.absolute(np.diag(eigenvalue))
    sigma = np.sqrt(sigma)
    return sigma

def createLeft(A, eig_normalize, sigma):
    return A @ eig_normalize / sigma

def createSVD(image_array):
    rows, cols = image_array.shape
    if rows < cols:
        less = rows
    else:
        less = cols
    
    sing_kanan = transpose(image_array) @ image_array
    eigenvalue, norm_kanan = createEigen(sing_kanan)
    sigma = createSigma(eigenvalue)
    left = createLeft(image_array, norm_kanan, sigma)

    return transpose(left)[0:less].T, sigma[0:less], transpose(norm_kanan)[0:less] 
