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


def eigenvalue(x):
    eigen = []
    a = x
    for i in range(50):
        q, r = qr(a)
        a = np.dot(r, q)
    for j in range(a.shape[0]):
        eigen.append(np.round(a[j][j], 6))

    return np.unique(eigen)[::-1]


def switchrow(x, a, b):
    for i in range(x.shape[1]):
        temp = x[a][i]
        x[a][i] = x[b][i]
        x[b][i] = temp


def makeone(x, a):
    first = x[a][a]
    for col in range(a, x.shape[1]):
        x[a][col] = x[a][col] / first


# def eigenvector(x, ei):
#     size = x.shape[0]
#     eva = []  # simpan x
#     for i in range(ei.size):
#         a = np.copy(x) * -1
#         for j in range(size):
#             a[j][j] += ei[i]
#         # b = np.zeros((size, size+1))
#         # for j in range(size):
#         #     for k in range(size):
#         #         b[j][k] = a[j][k]
#         pl, u = lu(a, permute_l=True)
#         for row in range(size):
#             if u[row][row] != 0:
#                 makeone(u, row)
#                 for k in range(row + 1, size):
#                     num = u[k][row]
#                     for l in range(row, size):
#                         u[k][l] -= num * u[row][l]
#         ev = []
#         for j in range(size):
#             if u[j][j] == 0:
#                 evv = []
#                 for k in range(size):
#                     if k != j:
#                         if u[k][j] != 0:
#                             evv.append(-u[k][j])
#                         else:
#                             evv.append(u[k][j])
#                     else:
#                         evv.append(1.0)
#                 ev.append(evv)
#         eva.append(ev)
#     return eva


# A = [[0,0,-2],[1,2,1],[1,0,3]]
# A = np.array(A)
# x = eigenvalue(A)
# print(x)
# print(eigenvector(A, x))


def normalizeVector(z):
    normalize = z / np.linalg.norm(z)
    return normalize


# print(normalizeVector(z))


def svd(A):
    mat = []
    kiri = A @ transpose(A)
    kanan = transpose(A) @ A
    mat.append(kanan)
    mat.append(kiri)

    mat_svd = []
    for item in mat:
        ei = eigenvalue(item)
        print(ei)
        # ei, U1 = np.linalg.eig(item)
        U1 = eigenvector(item, ei)
        matUV = []

        for i in range(len(U1)):
            ev = U1[i]
            for j in range(len(ev)):
                a = ev[j]
                b = normalizeVector(a)
                matUV.append(b)
        mat_svd.append(matUV)

    U = transpose(mat_svd[1])
    V = np.matrix(mat_svd[0])

    # sigma = [[0 for i in range(len(V))] for j in range(len(U))]
    # if len(U) < len(V):
    #     for p in range(len(U)):
    #         sigma[p][p] = math.sqrt(ei[p])
    # else:
    #     for p in range(len(V)):
    #         sigma[p][p] = math.sqrt(ei[p])

    return U, ei, V


def eigenvector(x, ei):
    size = x.shape[0]
    eva = []  # simpan x
    for i in range(ei.size):
        a = np.copy(x) * -1
        for j in range(size):
            a[j][j] += ei[i]
        # b = np.zeros((size, size+1))
        # for j in range(size):
        #     for k in range(size):
        #         b[j][k] = a[j][k]
        pl, u = lu(a, permute_l=True)
        for row in range(size):
            if u[row][row] != 0:
                makeone(u, row)

        thisRow = u.shape[0]
        for i in range(0, thisRow - 1):
            for j in range(i + 1, thisRow):
                ratio = u[i][j]
                for k in range(j, u.shape[1]):
                    u[i][k] -= ratio * u[j][k]

        ev = []
        for j in range(size):
            if u[j][j] == 0:
                evv = []
                for k in range(size):
                    if k != j:
                        if u[k][j] != 0:
                            evv.append(-u[k][j])
                        else:
                            evv.append(u[k][j])
                    else:
                        evv.append(1.0)  # memisalkan x yang variabel bebas jadi 1
                ev.append(evv)
        eva.append(ev)
    return eva


# def eigenvector(x, ei):
#     size = x.shape[0]
#     eva=[]
#     for i in range(ei.size):
#         a = np.copy(x) * -1
#         for j in range(size):
#             a[j][j] += ei[i]
#             np.append(a[j], 0)
#         b = np.zeros((size, size+1))
#         for j in range(size):
#             for k in range(size):
#                 b[j][k] = a[j][k]

#         # echelon process
#         for j in range(size):
#             if (b[j][j] == 0):
#                 for k in range(j+1, size):
#                     if(b[k][j] != 0):
#                         switchrow(b, j, k)
#             if (b[j][j] != 0):
#                 makeone(b,j)
#                 for k in range(j+1,size):
#                     num = b[k][j]
#                     for l in range(j, size+1):
#                         b[k][l] -= num * b[j][l]

#         for j in range(size-1, -1):
#             if (b[j][j] != 0):
#                 for k in range(j-1,-1):
#                     num = b[k][j]
#                     for l in range(j, size+1):
#                         b[k][l] -= num * b[j][l]

#         # turn into array of eigen vector
#         ev = []
#         for j in range(size):
#             if (b[j][j] == 0):
#                 evv = []
#                 for k in range(size):
#                     if k != j:
#                         if (b[k][j] != 0):
#                             evv.append(-b[k][j])
#                         else:
#                             evv.append(b[k][j])
#                     else:
#                         evv.append(1.0)
#                 ev.append(evv)
#         eva.append(ev)
#     return eva

# matriks = [[3, -2, 0], [-2, 3, 0], [0, 0, 5]]
# matriks = np.array(matriks)
# ei = eigenvalue(matriks)
# print(ei)
# print(eigenvector(matriks, ei))

# matriks = [[3, 1, 1], [-1, 3, 1]]
# matriks = np.array(matriks)
# U, S, V = svd(matriks)
# print(U)
# print(S)
# print(V)
