import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 


img = cv.imread(cv.samples.findFile("./assets/ballons.png"),0) # get picture grayscale = 0

if img is None:  
    sys.exit("Could not read the image.")

img_modify = img.copy()

H = img_modify[0:255, 0:255] + 1 
print(h)
plt.plot(231),plt.imshow(img, 'gray'),plt.title('ORIGINAL')
plt.show()
