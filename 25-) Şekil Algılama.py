import cv2
import numpy as np

# Font tanımla
font = cv2.FONT_ITALIC

# Resmi oku
img = cv2.imread("sekiller.jpg")

# Resmi gri tonlamaya dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı resmi eşik değerine göre ikili bir resme dönüştür
a, thresh = cv2.threshold(gray, 200, 300, cv2.THRESH_BINARY)

# Konturları bul
kontur, b = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Her bir kontur için işlemleri uygula
for i in kontur:
    # Konturun çevresini bul
    e = 0.01 * cv2.arcLength(i, True)
    # Konturu daha basitleştir
    approx = cv2.approxPolyDP(i, e, True)
    # Konturu çiz
    cv2.drawContours(img, [approx], 0, 5)

    # Konturun koordinatlarını al
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    print(approx)
    print(len(approx))

    # Konturun kenar sayısına göre şekil tespiti yap ve etiket ekle
    if len(approx) == 3:
        cv2.putText(img, "Üçgen", (x, y), font, 1, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img, "Dörtgen", (x, y), font, 1, 1, (0))
    elif len(approx) == 5:
        cv2.putText(img, "Beşgen", (x, y), font, 1, 1, (0))
    elif len(approx) == 6:
        cv2.putText(img, "Altıgen", (x, y), font, 1, 1, (0))
    else:
        cv2.putText(img, "Diğer", (x, y), font, 1, 1, (0))

# Son çıktı resmini göster
cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
