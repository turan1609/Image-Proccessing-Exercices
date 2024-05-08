#Bitwise İşlemleri
import cv2
import numpy as np
img1 = cv2.imread("black_white.jpg")
img2 = cv2.imread("crossed_black_white.jpg")

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1, img2)

cv2.imshow("first image", img1)
cv2.imshow("second image", img2)
'''cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not", bit_not)'''

cv2.waitKey(0)
cv2.destroyAllWindows()