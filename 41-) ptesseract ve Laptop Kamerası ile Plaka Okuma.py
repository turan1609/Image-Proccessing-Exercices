#En büyük dikdörtgeni algılar ve içinerkini okur
import cv2
import numpy as np
import imutils
import pytesseract

# Kamera bağlantısını aç
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Kare boyutunu küçült (isteğe bağlı, performansı artırabilir)
   # frame = cv2.flip(frame, 0)
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

# Kamera bağlantısını ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
