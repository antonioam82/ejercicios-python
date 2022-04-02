import matplotlib.pyplot as plt
import cv2
import numpy as np

image = cv2.imread("lenna.jpg",cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(10,10))
plt.imshow(image,cmap="gray")
plt.show()

hist = cv2.calcHist([image],[0], None, [256], [0,256])
intensity_values = np.array([x for x in range(hist.shape[0])])
plt.bar(intensity_values, hist[:,0], width=5)
plt.title("Bar histogram·")
plt.show()

PMF = hist / (image.shape[0] * image.shape[1])
plt.plot(intensity_values,hist)
plt.title("Histogram")
plt.grid()
plt.show()
