#ROİ işlemi img de daha spesifik(örn. plaka) bir yere odaklanma
import cv2
import numpy as np

img = cv2.imread("plaka.jpg")
roi = img[310:345, 125:259]#ilk kısım 291:350 dikey ; ikinci kısım 120:259 yatay

print(img.shape)
cv2.imshow("resim", img)
cv2.imshow("roi", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()