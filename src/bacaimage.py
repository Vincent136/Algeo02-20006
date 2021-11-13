from PIL import Image
import imageio
import numpy as np
import os

def bacaImage(path):
    try:
        return imageio.imread(path)
    except:
        return "File tidak ditemukan."

def arrayToImage(red, green, blue, path):   
    # program menerima input 3 buah matriks yaitu matriks red, green, dan blue dan string yang mengandung path dari file yang ingin disimpan

    # proses menggabungkan komponen rgb
    image = []
    for i in range(len(red)):
        outer = []
        for j in range(len(red[i])):
            inner=[]
            inner.append(red[i][j])
            inner.append(green[i][j]) 
            inner.append(blue[i][j])
            outer.append(inner)
        image.append(outer)
    image = np.array(image)

    #save image ke file
    image = image/255
    image = np.clip(image,0,1)
    image = np.uint8(image*255)
    image_out = Image.fromarray(image)

    image_out.save(path)

