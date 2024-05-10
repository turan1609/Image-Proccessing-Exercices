import cv2
import numpy as np

# Resmi oku
img = cv2.imread("star.png")

# Gri tonlamaya dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı resmi eşik değerine göre ikili bir resme dönüştür
ret, thresh = cv2.threshold(gray, 75, 200, cv2.THRESH_BINARY)

# Konturları bul
contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Konturun dışındaki konveks kabuğu bul
convex_hulls = []

for i in range(len(contour)):
    convex_hulls.append(cv2.convexHull(contour[i], False))

# Çıktı resmi için boş bir matris oluştur
output_image = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# Her bir kontur için çizim yap
for i in range(len(contour)):
    # Orjinal konturu mavi renkte çiz
    cv2.drawContours(output_image, contour, i, (255, 0, 0), 3, 8)
    # Konveks kabuğu yeşil renkte çiz
    cv2.drawContours(output_image, convex_hulls, i, (0, 255, 0), 1, 8)

cnt = convex_hulls[0]

M = cv2.moments(cnt)
alan = cv2.contourArea(cnt)
print(alan)#Alanı verir

cevre = cv2.arcLength(cnt, True)
print(cevre)

# Son çıktı resmini göster
cv2.imshow("resim", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
