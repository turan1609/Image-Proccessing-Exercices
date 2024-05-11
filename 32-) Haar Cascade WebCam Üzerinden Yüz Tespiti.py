import cv2

# Bilgisayar kamerasını aç
cap = cv2.VideoCapture(0)

# Yüz algılama modelini yükle
yuz = cv2.CascadeClassifier("frontal_face.xml")

while True:
    # Kameradan bir çerçeve al
    ret, frame = cap.read()
    
    # Çerçeveyi yatay olarak çevir (aynalama)
    frame = cv2.flip(frame, 1)
    
    # Çerçeveyi gri tona dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = yuz.detectMultiScale(gray, 1.2, 4)

    # Algılanan her yüz için dikdörtgen çiz
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Çerçeveyi göster
    cv2.imshow("1", frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Kamera kaynağını serbest bırak ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
