import cv2

# Video dosyasını yükle
cap = cv2.VideoCapture("attila.mp4")

# Yüz ve göz algılama modellerini yükle
yuz = cv2.CascadeClassifier("frontal_face.xml")
goz = cv2.CascadeClassifier("eye.xml")

while True:
    # Video çerçevesini oku
    ret, frame = cap.read()
    
    # Video sonuna gelindiğinde döngüyü kır
    if not ret:
        break

    # Çerçeveyi gri tona dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = yuz.detectMultiScale(gray, 1.3, 4)

    # Her algılanan yüz için işlemleri yap
    for x, y, w, h in faces:
        # Yüzün etrafına bir dikdörtgen çiz
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Yüz bölgesini seç
        face_roi = gray[y : y + h, x : x + w]
        face_frame = frame[y : y + h, x : x + w]

        # Yüz bölgesindeki gözleri algıla
        eyes = goz.detectMultiScale(face_roi)

        # Her algılanan göz için işlemleri yap
        for ex, ey, ew, eh in eyes:
            # Gözün etrafına bir dikdörtgen çiz
            cv2.rectangle(face_frame, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    # Çerçeveyi göster
    cv2.imshow("Video", frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Video kaynağını serbest bırak ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
