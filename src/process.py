from eigen import *
from bacaimage import *
import time


def percentage(height, width, rate):
    # rate = int(input("Image compression rate: "))
    k = round(rate * 0.01 * height * width / (height + width + 1))
    return k


def Process(input_file, output_file, rate):

    start_time = time.time()
    image = bacaImage(input_file)

    print(rate)

    k = percentage(image.shape[0], image.shape[1], rate)

    print(k)

    singular = int(k)
    red = image[:, :, 0].astype(float)
    green = image[:, :, 1].astype(float)
    blue = image[:, :, 2].astype(float)
    rgb = [red, green, blue]

    output_image = []
    for item in rgb:

        U, sigma, V = createSVD(item)

        U = U.T[0:singular].T

        # potong s
        sigma = sigma[0:singular]

        # potong vh
        V = V[0:singular]

        hasil = U @ np.diag(sigma) @ V

        output_image.append(hasil)

    arrayToImage(output_image[0], output_image[1], output_image[2], output_file)

    return time.time() - start_time


# start_time = time.time()
# Process("../test/miniont10%.jpg")
# print("execution time:  %s seconds" % (time.time() - start_time))

# start_time = time.time()
# Process("minion.jpg", "static/downloads/compressed_minion.jpg", 12)
# print("execution time:  %s seconds" % (time.time() - start_time))
