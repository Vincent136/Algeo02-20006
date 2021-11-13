import numpy as np
from scipy.linalg import lu
from numpy.linalg import qr
from numpy.core.fromnumeric import transpose
import math

def eigenvalue(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(200):
            Q,R = np.linalg.qr(X)
            pQ = pQ @ Q
            X = R @ Q
    return np.unique(np.absolute(np.diag(X)))[::-1], pQ

def normalizeVector(z):
    normalize = z / np.linalg.norm(z)
    return normalize


def svd(A):
    mat = []
    kiri = A@transpose(A)
    kanan = transpose(A) @ A
    mat.append(kanan)
    mat.append(kiri)

    mat_svd = []
    for item in mat:
        ei, U1 = eigenvalue(item)
        matUV = []

        for i in range (len(U1)):
            ev = U1[i]
            # b = normalizeVector(ev)
            matUV.append(ev)
        mat_svd.append(matUV)

    U = (np.array(mat_svd[1]))
    V = transpose(np.array(mat_svd[0]))
    
    sigma = np.zeros((U.shape[0],V.shape[0]))
    if (len(U)< len(V)):
        for p in range(len(U)):
            sigma[p][p] = math.sqrt(ei[p])
    else:
        for p in range(len(V)):
            sigma[p][p] = math.sqrt(ei[p])
    sigma = np.array(sigma)

    return U,sigma,V
    
matriks = [[3, 1, 1,3], [-1, 3, 1,5],[9,2,2,6],[6,6,6,1],[9,2,1,9],[1,2,3,11]]
matriks = np.array(matriks)
U, S, V = svd(matriks)
print(U)
print(S)
print(V)
print(U @ S @ V)

matriks2 = np.array(matriks)
U, s, V = np.linalg.svd(matriks2)


print()
print()


height = matriks2.shape[0]
width = matriks2.shape[1]

Sigma = np.zeros((height, width))

if height < width:
    Sigma[:height, :height] = np.diag(s)
else:
    Sigma[:width, :width] = np.diag(s)

print(U)
print(Sigma)
print(V)
print(U @ Sigma @ V)


