import cv2

# Video dosyasını yükle
cap = cv2.VideoCapture("crowded_people.mp4")

# Yüz algılama modelini yükle
yuz = cv2.CascadeClassifier("frontal_face.xml")

while True:
    # Video çerçevesini oku
    ret, frame = cap.read()
    
    # Çerçeveyi gri tona dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = yuz.detectMultiScale(gray, 1.2, 4)

    # Algılanan her yüz için dikdörtgen çiz
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Çerçeveyi göster
    cv2.imshow("1", frame)

    # Video sonuna gelindiğinde döngüyü kır
    if ret == 0:
        break
    
    # Çıkış için 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Video kaynağını serbest bırak ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
