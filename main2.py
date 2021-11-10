from bacaimage import *
from eigen import *

k = 10
array = bacaImage("test/gambar.jpg")

red = array[:,:,0]
green = array[:,:,1]
blue = array[:,:,2]
rgb = [red, green, blue]

image = []
for i in rgb:
    U,E,V = svd(i)

    E = E[:, :k]
    V = V[:k, :]
    img = U.dot(E.dot(V))
    image.append(img)


arrayToImage(image[0],image[1],image[2], "test/gambarSVD10.jpg")


