import cv2
import numpy as np
import imutils
import pytesseract
from picamera2 import Picamera2

# Tesseract OCR motorunun raspian üzerindeki yolunu belirtir
# Bu yol windows kullanıyorsanız elle girilmedilir.
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Plaka numarasını terminalden al
target_plate = input("Aranacak plaka numarasını ## ### ### formatında girin: ")

# Pi Camera yı başlatır. Burda Picamera2 yerine direk cv2 kullanmayı denedim
# fakat çalıştıramadım. cap = cv2.videoCapture(0) dediğimde kamerayı bulmuyor.
try:
    # Varsayılan kamera numarasını belirtir
    picam2 = Picamera2(camera_num=0)
    # Görüntü boyutunu ayarlar
    picam2.preview_configuration.main.size = (2304, 1296)
    # Görüntünün renk formatını ayarlar
    picam2.preview_configuration.main.format = "RGB888"
    # Hizalama yapaf
    picam2.preview_configuration.align()
    # Önizleme modunda yapılandırma yapar
    picam2.configure("preview")
    # Kamera başlatır
    picam2.start()
except Exception as e:
    # Kamera da hata çıkarsa düzgün takmayı dene. Aynı anda iki pine de bastırmalısın
    print(f"Camera initialization failed: {e}")
    exit(1)

# Bu fonksiyon plakanın tanımlandığını belirtir.
# Program artık plaka tanıması yapmaz
def captureFunction():
    print("Plate Has Been Founded!")

# Bu Area fonksiyonları drone nun hareketlerini kontrol eder.
# Uygulama alınan her bir kareyi 9 eşit parçaya böler. Her bir parça soldan sağa ve yukarıdan aşağıya 1-9 a kadar isimlendirilmiştir.
# Cismin merkezi 5 haricinde bir bölgeye giderse drone hareket eder
# Bu hareket kodları kullanılan drone'a göre değişik kütüphanelerden alınabilir.
def firstArea():
    print("Left-Up")


def secondArea():
    print("Up")


def thirdArea():
    print("Right-Up")


def fourthArea():
    print("Left")

# Aslında drone cismi her zaman 5 inci bölgede tutmaya çalışır
def fifthArea():
    print("Hold")


def sixthArea():
    print("Right")


def seventhArea():
    print("Left-Down")


def eigthArea():
    print("Down")


def ninethArea():
    print("Right-Down")

# Bu fonksiyon drone nun hangi bölgede olduğunu hesaplar ve gerek bölgenin fonksiyonunu çağırır
# Bu fonksiyonun parametreleri (Plakanın orta noktasının X ekseni değeri, Plakanın Y ekseni değeri, çerçevenin genişliği, çerçevenin uzunluğu)
def determineDroneRegion(cX, cY, width, height):
    region_width = width // 3
    region_height = height // 3

    row = cY // region_height
    col = cX // region_width

    region_number = row * 3 + col + 1

    if region_number == 1:
        firstArea()
    elif region_number == 2:
        secondArea()
    elif region_number == 3:
        thirdArea()
    elif region_number == 4:
        fourthArea()
    elif region_number == 5:
        fifthArea()
    elif region_number == 6:
        sixthArea()
    elif region_number == 7:
        seventhArea()
    elif region_number == 8:
        eigthArea()
    elif region_number == 9:
        ninethArea()


# Plaka eşleştiğinde bir daha plaka tarama işlemi yapılmaması için bir flag
plate_found = False

# Mevcut pencereyi takip etmek için değişken
current_window = "Frame"

# İlk frame'i gösterir ve değişik modlar arasında geçiş yapabilmek için gereken değerler tutulur
cv2.namedWindow(current_window)
show_frame = True
show_gray = False
show_edges = False
show_cropped = False

# Mazgalları göstermek için bir  bayrak
show_grilles = False

while True:
    # Kameradan görüntü alır
    frame = picam2.capture_array()

    # Kare boyutunu küçült (isteğe bağlı, performansı artırabilir)
    frame = imutils.resize(frame, width=800)
    # Kendi gözümüz gibi görebilmek için takla attırıyoruz
    # 0 değeri dikey, 1 değeri yatay, -1 değeri hem dikey hem yatay flip için kullanılır.
    frame = cv2.flip(frame, 0)

    # Kareyi gri tonlamalıya dönüştürür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Görüntüdeki gürültüyü azaltmak için bilateral filtre uygular
    gray = cv2.bilateralFilter(gray, 7, 200, 200)

    # Kenarları belirler
    edges = cv2.Canny(gray, 40, 200)

    # Kenar konturlarını bulur
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    # Plaka alanını bulmak için konturları dolaşır
    screen_contour = None
    for contour in contours:
        epsilon = 0.018 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            screen_contour = approx
            break

    cropped_plate = None
    text = ""
    if screen_contour is not None:
        # Plaka alanını gösterir
        cv2.drawContours(frame, [screen_contour], -1, (0, 255, 0), 2)
        # plate_found ilk başta false
        if not plate_found:
            # Plakayı maskesiyle kırpar
            mask = np.zeros(gray.shape, dtype=np.uint8)
            cv2.drawContours(mask, [screen_contour], -1, 255, -1)
            cropped_plate = cv2.bitwise_and(gray, gray, mask=mask)
            # Plakayı okumak için flipCode değeri 1 olmalı.
            cropped_plate = cv2.flip(cropped_plate, 1)

            # Plakadaki metni okur
            text = pytesseract.image_to_string(cropped_plate, lang="eng").strip()
            print(text)
            # Metni ekrana yazdır
            cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(gray, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(edges, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(cropped_plate, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Girilen plaka numarası ile eşleşme kontrolü yapar
            if text == target_plate:
                plate_found = True
                captureFunction()

        # Plakanın orta noktasını hesaplar
        M = cv2.moments(screen_contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0

        # Plakanın orta noktasına kırmızı bir nokta çizer
        cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)
        # Plakanın uçuş kontrollerini plakayı tanıdıktan sonra başlatır
        if plate_found:
            determineDroneRegion(cX, cY, frame.shape[1], frame.shape[0])
        # Görüntüyü 3x3 bölgelere ayırır
        height, width = frame.shape[:2]
        region_width = width // 3
        region_height = height // 3

        # Plakanın bulunduğu bölgeyi belirler
        region_number = (cY // region_height) * 3 + (cX // region_width) + 1

        # Bölge numarasını ekrana yazdırır
        region_text = f"Plate is at {region_number}. Region"
        cv2.putText(frame, region_text, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mazgalları çizer
    if show_grilles:
        for i in range(1, 10):
            row = (i - 1) // 3
            col = (i - 1) % 3
            x = col * region_width + region_width // 2
            y = row * region_height + region_height // 2
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
            # Dikey çizgileri çizer
            cv2.line(frame, (region_width, 0), (region_width, height), (0, 0, 255), 2)
            cv2.line(frame, (2 * region_width, 0), (2 * region_width, height), (0, 0, 255), 2)

            # Yatay çizgileri çizer
            cv2.line(frame, (0, region_height), (width, region_height), (0, 0, 255), 2)
            cv2.line(frame, (0, 2 * region_height), (width, 2 * region_height), (0, 0, 255), 2)

    # İlk frame'i gösterir
    if show_frame:
        cv2.imshow(current_window, frame)
    elif show_gray:
        cv2.imshow(current_window, gray)
    elif show_edges:
        cv2.imshow(current_window, edges)
    elif show_cropped and cropped_plate is not None:
        cv2.imshow(current_window, cropped_plate)

    # Klavye girişlerini kontrol eder
    key = cv2.waitKey(1) & 0xFF
    #  'g' ye basılırsa mevcut pencereyi kapatır, gray penceresini açar
    if key == ord('g'):
        cv2.destroyWindow(current_window)
        current_window = "Gray"
        show_frame = False
        show_gray = True
        show_edges = False
        show_cropped = False
    # 'e' ye basılırsa mevcut pencereyi kapatır, edges penceresini açar.
    elif key == ord('e'):
        cv2.destroyWindow(current_window)
        current_window = "Edges"
        show_frame = False
        show_gray = False
        show_edges = True
        show_cropped = False
    # 'c' ye basılırsa mevcut pencereyi kapatır, cropped_plate penceresini açar
    # Bu pencere sadece plakayı gösterir
    elif key == ord('c') and cropped_plate is not None:
        cv2.destroyWindow(current_window)
        current_window = "Cropped Plate"
        show_frame = False
        show_gray = False
        show_edges = False
        show_cropped = True
    # 'f' tuşuna basılırsa mevcut pencereyi kapatır, frame penceresini açar
    elif key == ord('f'):
        cv2.destroyWindow(current_window)
        current_window = "Frame"
        show_frame = True
        show_gray = False
        show_edges = False
        show_cropped = False
    # 'q' tuşuna basılırsa while döngüsünü kırar ve uygulama kapanır.
    elif key == ord('q'):
        break
    # 'k' tuşuna basılırsa mazgallar açılır.
    elif key == ord('k'):
        show_grilles = True
    # 'j' tuşuna basılırsa mazgallar kapanır.
    # Mazgallar en başta kapalı durumdadır.
    elif key == ord('j'):
        show_grilles = False

# Kaynakları serbest bırakır
cv2.destroyAllWindows()
picam2.stop()
