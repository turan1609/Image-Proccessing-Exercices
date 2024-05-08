#Resmi Döndürme
import cv2
import numpy as np

img = cv2.imread("img.jpg", 0)

sat, sut = img.shape
print(sat)#satır da kaç piksel var
print(sut)#sütunda kaç piksel var

m = cv2.getRotationMatrix2D((sut/2, sat/2), 180, 1)# /2 resmi görmemizi ssağlar
d = cv2.warpAffine(img, m, (sut, sat))

cv2.imshow("image", img)
cv2.imshow("converted_image", d)

cv2.waitKey(0)
cv2.destroyAllWindows()