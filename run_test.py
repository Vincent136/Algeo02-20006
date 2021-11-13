from bacaimage import *
from eigen2 import *

def Process(output_file, singular_v):

    singular_v = int(singular_v)

    main_image, image_m, split_image= bacaImage("test/susah.jpg")

    print("Image type is ", image_m)
   
    output_image = []
    for item in split_image:
        arr = np.array(item)
        print("array: ",arr)
        
        U, sigma ,V = svd(arr)
        print(U)

        U2, sigma2, V2 = np.linalg.svd(arr)
        print(U2)

        hasil = U[:,:singular_v] @ sigma[:singular_v,:singular_v] @ V[:singular_v,:]
        hasil2 = U2[:,:singular_v] @ sigma2[:singular_v,:singular_v] @ V2[:singular_v,:]

        print("hasil: ",hasil)
        print("hasil2: ",hasil2)

        
        output_image.append(hasil)
    
    # print(output_image)
    arrayToImage(output_image[0], output_image[1], output_image[2], output_file)

Process("test/output.jpg", 5)