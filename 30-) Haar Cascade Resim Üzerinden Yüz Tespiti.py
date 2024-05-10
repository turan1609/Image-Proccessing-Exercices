import cv2

# Giriş resmini yükle
img = cv2.imread("frontal_face.png")

# Frontal yüz tespiti için Haar kaskadını yükle
face_cascade = cv2.CascadeClassifier("frontal_face.xml")

# Resmi gri tonlamaya dönüştür (Haar kaskadı için gereklidir)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı görüntüde yüzleri tespit et
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

# Tespit edilen yüzlerin etrafına dikdörtgenler çiz
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Sonucu görüntüle
cv2.imshow("Tespit Edilen Yüzler", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
