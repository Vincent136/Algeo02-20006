from bacaimage import *

# baca gambar ubah ke array 3 dimensi yang isinya matriks red, green, blue

array = bacaImage("test/gambar.jpg")

#pisah komponen masing-masig rgb

red = array[:,:,0]
green = array[:,:,1]
blue = array[:,:,2]


# save ke image
red = red.transpose()
green = green.transpose()
blue = blue.transpose()

arrayToImage(red, green, blue, "test/gambarTranspose1.jpg")

red = red.transpose()
green = green.transpose()
blue = blue.transpose()

red = np.fliplr(red)
green = np.fliplr(green)
blue = np.fliplr(blue)


arrayToImage(red, green, blue, "test/gambarflip1.jpg")