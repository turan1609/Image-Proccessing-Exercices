import cv2

# Resim dosyasını yükle
img = cv2.imread("frontal_face.png")

# Yüz ve göz algılama modellerini yükle
yuz = cv2.CascadeClassifier("frontal_face.xml")
goz = cv2.CascadeClassifier("eye.xml")

# Resmi gri tona dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Yüzleri algıla
faces = yuz.detectMultiScale(gray, 1.3, 4)

# Her algılanan yüz için işlemleri yap
for x, y, w, h in faces:
    # Yüzün etrafına bir dikdörtgen çiz
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Yüz bölgesini seç
    img2 = img[y : y + h, x : x + h]
    gray2 = gray[y : y + h, x : x + h]

    # Yüz bölgesindeki gözleri algıla
    gozler = goz.detectMultiScale(gray2)

    # Her algılanan göz için işlemleri yap
    for x1, y1, w1, h1 in gozler:
        # Gözün etrafına bir dikdörtgen çiz
        cv2.rectangle(img2, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)

# Sonuçları ekranda göster
cv2.imshow("1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
