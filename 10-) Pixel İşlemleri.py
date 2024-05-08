#Pixel İşlemleri
import cv2
import numpy as np

img = cv2.imread("img.jpg")
cv2.imshow("araba", img)

renk = img[200, 300]#200x300 pikselinin rengini aldık
print(renk)#Şimdide konsola yazdırıcaz
print(img.shape)# Bu işlem bize resmin boyutunu ve kaç renk katmanı olduğunu söyler. shape numpy kütüphanesinden geliyo
#renkleri teker teker de alabiliriz

blue_of_pixel = img[200, 300, 0]
print("Mavi", blue_of_pixel)

green_of_pixel = img[200, 300, 1]
print("Yeşil", green_of_pixel)

red_of_pixel = img[200, 300, 2]
print("Kırmızı", red_of_pixel)
#Örneğin bir pikselin mavi si ni sıfır yapalım
img[200, 300, 0] = 0
print(img[200, 300])#[  0 123 221] şu şekilde çıktı alırız

#bir başka yöntemde şu
mavi = img.item(150, 150, 0)
print(mavi)

img.itemset((150, 150, 0), 200)#burdaki 200 mavi değeri olarak atadık [200 255 255] ilk yani mavi değer 200 oldu
print(img[150, 150])

cv2.waitKey(0)
cv2.destroyAllWindows()