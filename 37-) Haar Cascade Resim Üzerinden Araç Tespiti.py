import cv2  # OpenCV kütüphanesini içe aktarın.

# "trafik_araclar.jpg" adlı görüntü dosyasını okuyun.
img = cv2.imread("trafik_araclar.jpg")

# Araba tespiti için CascadeClassifier sınıfından bir nesne oluşturun.
araba = cv2.CascadeClassifier("cars.xml")

# Görüntüyü gri tonlamaya dönüştürün.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# araba nesnesi ile arabaları algılayın.
# detectMultiScale fonksiyonuyla, gri tonlama görüntüsündeki arabaları tespit edin.
# scaleFactor: Tespit algoritmasının her ölçekte ne kadar küçüleceğini belirler.
# minNeighbors: Bir nesnenin yakınında kaç tane komşu dikdörtgenin bulunması gerektiğini belirler.
cars = araba.detectMultiScale(gray, 1.1, 2)

# Tespit edilen her araba için bir döngü başlatın.
for x, y, w, h in cars:
    # Her arabaya bir dikdörtgen çizin.
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Görüntüyü ekranda göstermek için imshow fonksiyonunu kullanın.
cv2.imshow("1", img)

# Bir tuşa basılana kadar bekleyin.
cv2.waitKey(0)

# Tüm pencereleri kapatın.
cv2.destroyAllWindows()
