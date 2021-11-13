import numpy as np
from scipy.linalg import lu
from numpy.linalg import qr
from numpy.core.fromnumeric import transpose
import math

# def QR(x):

#     # proses membentuk matrix Q R dengan metode Gram Schmidt

#     A = []
#     length = x.shape[0]
#     for i in range(length):
#         A = np.append(A , x[:,i], axis = 0)
#     A = np.reshape(A, (length, length))

#     e = []
#     sum = 0
#     for i in range(length):
#         sum += A[0][i] * A[0][i]
#     e = np.append(e, np.multiply(A[0], (1 / np.sqrt(sum))))
#     e = np.reshape(e, (1, length))

#     for i in range(1, length):
#         temp = A[i]
#         for j in range(i):
#             temp = np.subtract(temp , e[j] * np.dot(A[i], e[j]))


#         sum = 0
#         for k in range(length):
#             sum += temp[k] * temp[k]
#         norm = np.multiply(temp, (1 / np.sqrt(sum)))

#         e = np.append(e, [norm])
#         e = np.reshape(e, (i+1, length))

#     r = np.zeros((length, length))
#     for l in range(length):
#         for m in range(l, length):
#             r[l][m] = np.dot(A[m], e[l])

#     return e.transpose(), r


# def eigenvalue(x):
#     eigen = []
#     a = x
#     for i in range(50):
#         q, r = qr(a)
#         a = np.dot(r, q)
#     for j in range(a.shape[0]):
#         eigen.append(np.round(a[j][j], 6))

#     return np.unique(eigen)[::-1]

def eigenvalue(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(100):
            Q,R = np.linalg.qr(X)
            pQ = pQ @ Q
            X = R @ Q
    return np.unique(np.diag(X)), pQ


def normalizeVector(z):
    normalize = z / np.linalg.norm(z)
    return normalize


def svd(A):
    mat = []
    kiri = A @ transpose(A)
    kanan = transpose(A) @ A
    mat.append(kanan)
    mat.append(kiri)

    mat_svd = []
    for item in mat:
        ei, U1 = np.linalg.eig(item)
        matUV = []

        for i in range(len(U1)):
            ev = U1[i]
            # b = normalizeVector(ev)
            matUV.append(ev)
        mat_svd.append(matUV)

    U = transpose(mat_svd[1])
    V = np.matrix(mat_svd[0])

    sigma = [[0 for i in range(len(V))] for j in range(len(U))]
    if len(U) < len(V):
        for p in range(len(U)):
            sigma[p][p] = math.sqrt(ei[p])
    else:
        for p in range(len(V)):
            sigma[p][p] = math.sqrt(ei[p])

    return np.array(U), np.array(sigma), np.array(V)

# A = [[10, 0, 2],[0,10,4],[2,4,2]]
# A = np.array(A)
# ei, ev = np.linalg.eig(A)
# print(ev)

# matriks = [[3, -2, 0], [-2, 3, 0], [0, 0, 5]]
# matriks = np.array(matriks)
# ei = eigenvalue(matriks)
# print(ei)
# print(eigenvector(matriks, ei))

matriks = [[3, 1, 1], [-1, 3, 1]]
matriks = np.array(matriks)
U, S, V = svd(matriks)
print(U)
print(S)
print(V)
print(U @ S @ V)
