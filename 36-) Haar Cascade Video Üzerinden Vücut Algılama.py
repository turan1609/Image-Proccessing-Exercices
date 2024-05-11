import cv2  # OpenCV kütüphanesini içe aktarın.

# Video dosyasını açmak için cv2.VideoCapture() fonksiyonunu kullanın.
cap = cv2.VideoCapture("crowded_people.mp4")

# Vücut tespiti için CascadeClassifier sınıfından bir nesne oluşturun.
vucut = cv2.CascadeClassifier("body.xml")

while True:  # Sonsuz bir döngü başlatın, video sonuna kadar devam edecek.
    # cap.read() fonksiyonuyla bir sonraki video karesini okuyun ve geri dönüş değerlerini alın.
    ret, frame = cap.read()

    # Görüntüyü gri tonlamaya dönüştürün.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # vucut nesnesi ile vücutları algılayın.
    # detectMultiScale fonksiyonuyla, gri tonlama görüntüsündeki vücutları tespit edin.
    # scaleFactor: Tespit algoritmasının her ölçekte ne kadar küçüleceğini belirler.
    # minNeighbors: Bir nesnenin yakınında kaç tane komşu dikdörtgenin bulunması gerektiğini belirler.
    bodies = vucut.detectMultiScale(gray, 1.1, 1)

    # Tespit edilen her vücut için bir döngü başlatın.
    for x, y, w, h in bodies:
        # Her vücut için bir dikdörtgen çizin.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Görüntüyü ekranda göstermek için imshow fonksiyonunu kullanın.
    cv2.imshow("1", frame)
    
    # Klavyeden "q" tuşuna basıldığında döngüyü kırın.
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Video akışını serbest bırakın.
cap.release()
# Tüm pencereleri kapatın.
cv2.destroyAllWindows()
