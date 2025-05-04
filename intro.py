import cv2


img = cv2.imread('img1.jpg') # reading an image, loads in BGR format

cv2.imshow('COlor riot', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE) # converts an image to grayscale version
cv2.imshow('Color Riot Ended', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()







