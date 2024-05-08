#Resim Birleştirme İşlemi
import cv2
import numpy as np
circle = np.zeros((512, 512, 3), np.uint8) + 255
#np.zeros sıfırlardan oluşan matrisler açar. yani dokuyu oluşturur
#3 kaç renk katmanı olacağını belirler
# + 255 tüm bu sıfırlara 255 ekler ve beyaz yapar
cv2.circle(circle,(256, 256), 50, (255, 0, 0), -1)# -1 içini doldurmak için

square = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(square,(150, 150), (350, 350), (0, 255, 0), -1)

topla = cv2.add(circle, square)#Bu işlem kesişimlerini alır
print(topla[256, 256])

cv2.imshow("daire", circle)
cv2.imshow("kare", square)
cv2.imshow("toplam", topla)

cv2.waitKey(0)
cv2.destroyAllWindows()