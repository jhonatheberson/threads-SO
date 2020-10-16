import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 
import sys

def enlargement():

    # Load image
    img = cv.imread("./assets/balloons.png", 0) 
    if img is None:  
        sys.exit("Could not read the image.")

    # Get image dimensions and create new
    width, height = img.shape
    new_img = np.zeros((width, height))

    # Get the highest and lowest value of brightness (0 <= I <= 255)
    Imin = 9999
    Imax = 0
    for i in range(width):
      for j in range(height):
        if(img[i,j] > Imax):
            Imax = img[i,j]
        if(img[i,j] < Imin):
            Imin = img[i,j]

    print("Highest : " + str(Imax) + " Lowest : " + str(Imin))        

    # Build new image
    for i in range(width):
      for j in range(height):
          num = (255 / ( Imax - Imin )) * ( img[i, j] - Imin )
          new_img[i, j] = int(num)

    # # Print and save image
    # plt.subplot(231),plt.imshow(img, 'gray'),plt.title('ORIGINAL')
    # plt.subplot(232),plt.imshow(new_img, 'gray'),plt.title('Alargamento de Contraste')
    # plt.show()

    cv.imwrite("./assets/enlargement.png", new_img) 

if __name__ == "__main__":
    enlargement()