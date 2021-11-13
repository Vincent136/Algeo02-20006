from eigen import *
from bacaimage import *


def Process(output_file, k):

    singular = int(k)

    image= bacaImage("../test/gambar.jpg")
    
    red = image[:,:,0].astype(float)
    green = image[:,:,1].astype(float)
    blue = image[:,:,2].astype(float)
    rgb = [red, green, blue]
   
    output_image = []
    for item in rgb:
      
        print("processing")

        U, sigma ,V = createSVD(item)
        print(singular)

        U = U.T[0:singular].T

        # potong s
        sigma = sigma[0:singular]

        # potong vh
        V = V[0:singular]
        
        hasil = U @ np.diag(sigma) @ V

        output_image.append(hasil)
        print("kelar")
    
    arrayToImage(output_image[0], output_image[1], output_image[2], output_file)

Process("../test/output.jpg", 5)