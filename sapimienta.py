import numpy as np
import cv2
import random

img_gs = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)

def salt_pepper(prob):
      row, col = img_gs.shape

      s_vs_p = 0.5
      output = np.copy(img_gs)

      num_salt = np.ceil(prob * img_gs.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in img_gs.shape]
      output[tuple(coords)] = 1

      num_pepper = np.ceil(prob * img_gs.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in img_gs.shape]
      output[tuple(coords)] = 0
      cv2.imshow("ima",output)

      return output

sp_05 = salt_pepper(0.5)

cv2.imwrite('lena_new.jpg', sp_05)
