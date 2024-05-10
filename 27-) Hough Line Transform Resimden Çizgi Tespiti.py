import cv2
import numpy as np

# Resmi oku
img = cv2.imread("cizgiler.jpg")

# Gri tonlamalı görüntü elde etme
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Kenarları algılama
kenar = cv2.Canny(gray, 100, 250)

# Hough dönüşümü kullanarak çizgileri tespit etme
# İlk parametre: Kenar görüntüsü
# İkinci parametre: Çözünürlük (rho değeri)
# Üçüncü parametre: Radyan cinsinden açı çözünürlüğü (theta değeri)
# Dördüncü parametre: Eşik değeri, bir çizginin tespit edilmesi için gereken oy sayısı
cizgi = cv2.HoughLinesP(kenar, 1, np.pi / 180, 150)

# Tespit edilen çizgileri çizme
if cizgi is not None:
    for i in cizgi:
        x1, y1, x2, y2 = i[0]  # Çizginin koordinatları
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 5)  # Çizgiyi resme ekleme

# Sonuçları gösterme
cv2.imshow("Tespit Edilen Çizgiler", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
