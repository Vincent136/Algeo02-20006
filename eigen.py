import numpy as np
from numpy.linalg import qr

def QR(x):

    # proses membentuk matrix Q R dengan metode Gram Schmidt

    A = []
    length = x.shape[0]
    for i in range(length):
        A = np.append(A , x[:,i], axis = 0)
    A = np.reshape(A, (length, length))

    e = []
    sum = 0
    for i in range(length):
        sum += A[0][i] * A[0][i]
    e = np.append(e, np.multiply(A[0], (1 / np.sqrt(sum))))
    e = np.reshape(e, (1, length))

    for i in range(1, length):
        temp = A[i]
        for j in range(i):
            temp = np.subtract(temp , e[j] * np.dot(A[i], e[j]))
            

        sum = 0
        for k in range(length):
            sum += temp[k] * temp[k]
        norm = np.multiply(temp, (1 / np.sqrt(sum)))

        e = np.append(e, [norm])
        e = np.reshape(e, (i+1, length))

    r = np.zeros((length, length))
    for l in range(length):
        for m in range(l, length):
            r[l][m] = np.dot(A[m], e[l])

    return e.transpose(), r

def eigenvalue(x):
    eigen = []
    a = x
    for i in range(100):
        q, r = QR(a)
        a = np.dot(r, q)
    for j in range(a.shape[0]):
        eigen.append(np.round(a[j][j],12))

    return np.unique(eigen)[::-1]

def switchrow(x,a,b):
    for i in range(x.shape[1]):
        temp = x[a][i]
        x[a][i] = x[b][i]
        x[b][i] = temp

def makeone(x,a):
    first = x[a][a]
    for i in range(a, x.shape[1]):
        x[a][i] = x[a][i] / first

def eigenvector(x):
    ei = eigenvalue(x)
    size = x.shape[0]
    for i in range(ei.size):
        a = np.copy(x) * -1
        for j in range(size):
            a[j][j] += ei[i]
            np.append(a[j], 0)
        b = np.zeros((size, size+1))
        for j in range(size):
            for k in range(size):
                b[j][k] = a[j][k]

        # echelon process
        for j in range(size):
            if (b[j][j] == 0):
                for k in range(j+1, size):
                    if(b[k][j] != 0):
                        switchrow(b, j, k)
            if (b[j][j] != 0):
                makeone(b,j)
                for k in range(j+1,size):
                    num = b[k][j]
                    for l in range(j, size+1):
                        b[k][l] -= num * b[j][l]


# A = [[3,-2,0],[-2,3,0],[0,0,5]]
# A = np.array(A)
# eigenvector(A)


