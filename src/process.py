from eigen import *
from bacaimage import *
import time


def percentage(height, width, rate):
    # rate = int(input("Image compression rate: "))
    k = round(rate * 0.01 * height * width / (height + width + 1))
    return k


def Process(input_file, output_file, rate):

    start_time = time.time()

    print("Time started")

    image = bacaImage(input_file)

    print("Compress Rate: ",rate,"%")

    rate_k = rate

    k = percentage(image.shape[0], image.shape[1], rate_k)

    print("Singular:", k)

    singular = int(k)
    if (singular == 0):
        singular = 1
    
    
    if (len(image.shape) == 3):
        rgb = []

        for i in range(image.shape[2]):
            rgb.append(image[:,:,i].astype(float))

        print("Processing SVD...")

        output_image = []
        for item in rgb:
     
            U, sigma, V = createSVD(item)
           

            U = U.T[0:singular].T

            sigma = sigma[0:singular]

            V = V[0:singular]

            hasil = U @ np.diag(sigma) @ V

            output_image.append(hasil)

        if (image.shape[2] == 4) :
            arrayToImage4Channel(output_image[0], output_image[1], output_image[2], output_image[3], output_file)
        elif (image.shape[2] == 3):
            arrayToImage3Channel(output_image[0], output_image[1], output_image[2], output_file)
    else:
        U, sigma, V = createSVD(image)

        U = U.T[0:singular].T

        sigma = sigma[0:singular]

        V = V[0:singular]

        hasil = U @ np.diag(sigma) @ V

        arrayToImageSingleChannel(hasil, output_file)


    print("Finished")

    return time.time() - start_time

# Process("gambar.jpg", "gambar2.jpg",98)
# start_time = time.time()
# Process("../test/miniont10%.jpg")
# print("execution time:  %s seconds" % (time.time() - start_time))

# start_time = time.time()
# Process("minion.jpg", "static/downloads/compressed_minion.jpg", 12)
# print("execution time:  %s seconds" % (time.time() - start_time))
