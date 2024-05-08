#Resim Filtreleme İşlemleri
# Bulurlama
import cv2
import numpy as np
img = cv2.imread("plaka.jpg")
img_bird_eye = cv2.imread("birdeye.jpg")

blr = cv2.blur(img, (5, 5))# Bulurlama
gb = cv2.GaussianBlur(img, (5,5), cv2.BORDER_DEFAULT)#Gaussian Blurlama. Burda sayılar tek olmalı
mb = cv2.medianBlur(img, 15)#Median Blur. Yine tek sayı girilmesi lazım
img_bird_eye_median_blur = cv2.medianBlur(img_bird_eye, 15)
img_bird_eye_bilateral_blur = cv2.bilateralFilter(img_bird_eye,9,75,75)

'''
cv2.imshow("normal", img)
cv2.imshow("blurlanmis", blr)
cv2.imshow("gaussian blur", gb)
cv2.imshow("median blur", mb)
cv2.imshow("birdeye", img_bird_eye_median_blur)
'''
cv2.imshow("bilateral blur", img_bird_eye_bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()