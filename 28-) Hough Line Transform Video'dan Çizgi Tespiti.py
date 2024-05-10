import cv2
import numpy as np

# Video dosyasını aç
cap = cv2.VideoCapture("yellow_line.mp4")

while True:
    # Bir sonraki kareyi oku
    ret, frame = cap.read()

    # Eğer kare okunamıyorsa veya video bittiğinde döngüyü sonlandır
    if not ret:
        break

    # Kare boyutunu yeniden boyutlandır (isteğe bağlı)
    frame = cv2.resize(frame, (800, 600))

    # HSV renk uzayına dönüşüm yap
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Sarı rengi tanımla
    alt_sari = np.array([18, 94, 140], np.uint8)
    ust_sari = np.array([48, 255, 255], np.uint8)  # Üst sınırı düşürerek sadece daha parlak sarıları seç

    # Maske oluştur
    mask = cv2.inRange(hsv, alt_sari, ust_sari)

    # Kenar algılama
    kenar = cv2.Canny(mask, 75, 250)

    # Hough dönüşümü ile çizgileri tespit et
    cizgi = cv2.HoughLinesP(kenar, 1, np.pi / 180, 50, maxLineGap=5)

    # Tespit edilen çizgileri çiz
    if cizgi is not None:
        for i in cizgi:
            x1, y1, x2, y2 = i[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Görüntüyü göster
    cv2.imshow("a", frame)

    # Çıkış için "q" tuşuna basılmasını bekle
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Video akışını serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
