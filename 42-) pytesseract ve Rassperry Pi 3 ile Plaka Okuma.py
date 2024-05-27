import cv2
import numpy as np
import imutils
import pytesseract
from picamera2 import Picamera2

# Tesseract OCR motorunun yolunu belirtin (gerekli olabilir)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Picamera2'yi başlatmaya çalış
try:
    picam2 = Picamera2(camera_num=0)  # Varsayılan kamera numarasını belirtin
    picam2.preview_configuration.main.size = (640, 480)  # Görüntü boyutu ayarlanıyor
    picam2.preview_configuration.main.format = "RGB888"  # Görüntü formatı ayarlanıyor
    picam2.preview_configuration.align()  # Hizalama yapılıyor
    picam2.configure("preview")  # Önizleme modunda yapılandırma yapılıyor
    picam2.start()  # Kamera başlatılıyor
except Exception as e:
    print(f"Camera initialization failed: {e}")
    exit(1)

while True:
    # Kameradan görüntü al
    frame = picam2.capture_array()

    # Kare boyutunu küçült (isteğe bağlı, performansı artırabilir)
    frame = imutils.resize(frame, width=800)

    # Kareyi gri tonlamalıya dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Görüntüdeki gürültüyü azaltmak için bilateral filtre uygula
    gray = cv2.bilateralFilter(gray, 7, 200, 200)

    # Kenarları belirle
    edges = cv2.Canny(gray, 40, 200)

    # Kenar konturlarını bul
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    # Plaka alanını bulmak için konturları dolaş
    screen_contour = None
    for contour in contours:
        epsilon = 0.018 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            screen_contour = approx
            break

    if screen_contour is not None:
        # Plaka alanını göster
        cv2.drawContours(frame, [screen_contour], -1, (0, 255, 0), 2)

        # Plakayı maskesiyle kırp
        mask = np.zeros(gray.shape, dtype=np.uint8)
        cv2.drawContours(mask, [screen_contour], -1, 255, -1)
        cropped_plate = cv2.bitwise_and(gray, gray, mask=mask)

        # Plakadaki metni oku
        text = pytesseract.image_to_string(cropped_plate, lang="eng")
        print(text)
        # Metni ekrana yazdır
        cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Kareyi göster
    cv2.imshow("Frame", frame)
    cv2.imshow("Gray", gray)
    cv2.imshow("Edges", edges)

    # Çıkış için 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cv2.destroyAllWindows()
picam2.stop()
