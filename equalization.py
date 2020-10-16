import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 
import sys


def equalization():

  H = np.zeros(256)
  p = np.zeros(256)
  P = []


  img = cv.imread("./assets/balloons.png",0) # get picture grayscale = 0

  if img is None:  
      sys.exit("Could not read the image.")



  data_image = img.shape
  print("data_image:",data_image)
  for i in range(data_image[0]):
    for j in range(data_image[1]):
      H[img[i,j]] += 1


  for i in range(256):
      P.append(H[i]/(data_image[0]*data_image[1]))


  for i in range(256):
    cont = 0
    for j in range(i):
      cont = cont + P[j]
    p[i] = cont

  img_modify = np.zeros((data_image[0], data_image[1]))

  for i in range(data_image[0]):
    for j in range(data_image[1]):
      img_modify[i,j]= int(255*p[img[i,j]])



  # plt.subplot(231),plt.imshow(img, 'gray'),plt.title('ORIGINAL')
  # plt.subplot(232),plt.imshow(img_modify, 'gray'),plt.title('Equalização de Histograma')

  # plt.show()
  cv.imwrite("assets/equalizarion.png", img_modify) #save picture


if __name__ == "__main__":
    equalization()