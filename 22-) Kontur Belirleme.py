import cv2
import numpy as np

# Resmi oku
img = cv2.imread("counter.jpg")

# Gri tonlamaya dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı resmi eşik değerine göre ikili bir resme dönüştür
ret, thresh = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)

# Konturları bul
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Konturları ekrana yazdır
print(contours)

# İlk konturu (contours[0]) çiz
# 3. parametre: Kontur dizisinin indeksi.
# Bir resimde birden fazla kontur olabilir. Bu parametre, hangi konturun çizileceğini belirler.
# Örneğin, contours[0] ilk konturu temsil eder.

# Diğer parametreler:
# 4. parametre: Kontur rengi. Bu örnek için (0, 0, 255) yeşil renk kullanılıyor.
# 5. parametre: Kontur kalınlığı. Bu örnekte 2 piksel olarak belirlenmiş.
cv2.drawContours(img, contours, 1, (0, 0, 255), 2)

# Resmi göster
cv2.imshow("Counters", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
