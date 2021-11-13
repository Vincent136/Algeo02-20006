from bacaimage import *
import numpy as np
from eigen import *

array = bacaImage("test/fotokecil.png")
k = 10
height = array.shape[0]
width = array.shape[1]

red = array[:, :, 0]
green = array[:, :, 1]
blue = array[:, :, 2]
rgb = [red, green, blue]

res = []
for i in rgb:
    U, s, VT = np.linalg.svd(i)

    Sigma = np.zeros((height, width))

    # fill Sigma with diagonal s

    if height < width:
        Sigma[:height, :height] = np.diag(s)
    else:
        Sigma[:width, :width] = np.diag(s)

    Sigma = Sigma[:, :k]
    VT = VT[:k, :]

    # reconstruct
    B = U.dot(Sigma.dot(VT))

    res.append(B)

arrayToImage(res[0], res[1], res[2], "test/gambarsvd10.png")
