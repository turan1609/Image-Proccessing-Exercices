import cv2
# Resmi oku
img = cv2.imread("ucgen.jpg")

# Resmi gri tonlamaya dönüştür
# 2. parametre: Eşik değeri.
# Gri tonlamalı resimdeki pikseller, bu eşik değerine göre sınıflandırılır.
# Eşik değerinden düşük olan pikseller 0 (siyah) olarak kabul edilir,
# eşik değerinden büyük olanlar ise 255 (beyaz) olarak kabul edilir.

# 3. parametre: Maksimum değer.
# Eşikleme türüne bağlı olarak, bu parametre eşiklenmiş pikselin maksimum değerini belirler.
# Örneğin, cv2.THRESH_BINARY eşikleme türünde, bu parametre, eşik değerini geçen piksellerin alacağı
# maksimum değeri belirler.
# Bu örnekte, eşik değerinden büyük olan pikseller 200 olarak atanır.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı resmi eşik değerine göre ikili bir resme dönüştür
ai, thresh = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)

# Resmin momentlerini hesapla
m = cv2.moments(thresh)
print(m)

# Ağırlık merkezini bul
x = int(m["m10"] / m["m00"])
y = int(m["m01"] / m["m00"])

# Ağırlık merkezini daireyle işaretle
cv2.circle(img, (x, y), 10, (255, 0, 0), -1)

# İşaretlenmiş resmi göster
cv2.imshow("s", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
