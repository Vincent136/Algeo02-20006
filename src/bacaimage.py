from PIL import Image
import imageio
import numpy as np
import os

def bacaImage(path):
    try:
        return imageio.imread(path)
    except:
        return "File tidak ditemukan."

def arrayToImage3Channel(first, second, third, path):   
    # program menerima input 3 buah matriks yaitu matriks first, second, dan third dan string yang mengandung path dari file yang ingin disimpan

    # proses menggabungkan komponen rgb
    image = []
    for i in range(len(first)):
        outer = []
        for j in range(len(first[i])):
            inner=[]
            inner.append(first[i][j])
            inner.append(second[i][j]) 
            inner.append(third[i][j])
            outer.append(inner)
        image.append(outer)
    image = np.array(image)

    #save image ke file
    image = image/255
    image = np.clip(image,0,1)
    image = np.uint8(image*255)
    image_out = Image.fromarray(image)

    image_out.save(path)

def arrayToImage4Channel(first, second, third, fourth, path):   
    # program menerima input 3 buah matriks yaitu matriks first, second, dan third dan string yang mengandung path dari file yang ingin disimpan

    # proses menggabungkan komponen rgb
    image = []
    for i in range(len(first)):
        outer = []
        for j in range(len(first[i])):
            inner=[]
            inner.append(first[i][j])
            inner.append(second[i][j]) 
            inner.append(third[i][j])
            inner.append(fourth[i][j])
            outer.append(inner)
        image.append(outer)
    image = np.array(image)

    #save image ke file
    image = image/255
    image = np.clip(image,0,1)
    image = np.uint8(image*255)
    image_out = Image.fromarray(image)

    image_out.save(path)

def arrayToImageSingleChannel(image, path):   
    # program menerima input 3 buah matriks yaitu matriks first, second, dan third dan string yang mengandung path dari file yang ingin disimpan

    # proses menggabungkan komponen rgb

    #save image ke file
    image = image/255
    image = np.clip(image,0,1)
    image = np.uint8(image*255)
    image_out = Image.fromarray(image)

    image_out.save(path)