import cv2  # OpenCV kütüphanesini içe aktarın.
import numpy as np  # NumPy kütüphanesini içe aktarın.
import pytesseract  # Tesseract OCR kütüphanesini içe aktarın.
import imutils  # Imutils kütüphanesini içe aktarın.

# "plaka_2.jpg" adlı görüntü dosyasını okuyun.
img = cv2.imread("plaka_2.jpg")

# Görüntüyü gri tonlamaya dönüştürün.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için bilateral filtreleme uygulayın.
filter = cv2.bilateralFilter(gray, 7, 200, 200)

# Kenar tespiti için Canny kenar dedektörünü kullanın.
corner = cv2.Canny(filter, 40, 200)

# Konturları bulun.
# findContours fonksiyonu, kenar tespiti sonucu elde edilen köşeler üzerinde kontur tespiti yapar.
contour, a = cv2.findContours(corner, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = imutils.grab_contours((contour, a))
cnt = sorted(cnt, key=cv2.contourArea, reverse=True)[:10]

# Plaka alanını temsil eden konturu bulun.
screen = 0
for i in cnt:
    epsilon = 0.018 * cv2.arcLength(i, True)
    aprx = cv2.approxPolyDP(i, epsilon, True)
    if len(aprx) == 4:
        screen = aprx
        break

# Mask oluşturun ve konturu çizin.
mask = np.zeros(gray.shape, np.uint8)
newMask = cv2.drawContours(mask, [screen], 0, (255, 255, 255), -1)

# Maskeyi kullanarak plakayı ayıklayın.
word = cv2.bitwise_and(img, img, mask=mask)

# Plaka alanını temsil eden koordinatları alın.
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))

# Plakayı kesin.
crop = gray[topx:bottomx + 1, topy:bottomy + 1]

# Tesseract kullanarak plakadaki metni tanıyın.
text = pytesseract.image_to_string(crop, lang="eng")
print(text)

# Görüntüyü ve işlenmiş görüntüleri göstermek için imshow fonksiyonunu kullanın.
cv2.imshow("2", img)  # Orjinal görüntü
cv2.imshow("3", filter)  # Filtrelenmiş görüntü
cv2.imshow("4", corner)  # Kenar görüntüsü
cv2.imshow("5", newMask)  # Maske
cv2.imshow("6", word)  # Maske ile plaka
cv2.imshow("7", crop)  # Plaka
cv2.waitKey(0)
cv2.destroyAllWindows()
