import cv2
import matplotlib.pyplot as plt


img = cv2.imread('img1.jpg') # reading an image, loads in BGR format

# cv2.imshow('COlor riot', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

gray = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE) # converts an image to grayscale version
# cv2.imshow('Color Riot Ended', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

negative = 255 - gray
# cv2.imshow('Negative', negative)
# cv2.watershed(0)
# cv2.destroyAllWindows()

images = [img, gray, negative]
titles = ["Original", "Gray", "Negative"]

plt.figure(figsize=(12, 3))
n = len(images)
for i in range(n):
  plt.subplot(1, n, i + 1)
  plt.imshow(images[i])
  plt.title(titles[i])
  plt.axis('off')

plt.tight_layout()
plt.show()






