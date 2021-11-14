import numpy as np
from numpy.core.fromnumeric import transpose
import math

def createEigen(A):
    
    #inisialisasi matriks berupa matriks identitas dengan ukuran sama dengan baris (matriks A harus persegi)
    eig_normalize = np.eye(A.shape[0])

    #inisialisasi matriks untuk mencari eigen value
    eig_value=A.copy()
    
    #mencari eigen value dan eigen vector yang sudah di normalize dengan menggunakan qr method
    for i in range(10):
            Q,R = np.linalg.qr(eig_value)
            eig_normalize = eig_normalize @ Q
            eig_value = R @ Q
    return eig_value, eig_normalize

def createSigma(eigenvalue):

    #mengambil diagonal dari suatu matriks
    sigma = np.absolute(np.diag(eigenvalue))

    #mengubah eigen value menjadi nilai singular dengan cara diakarkan
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
