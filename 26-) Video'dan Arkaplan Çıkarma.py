import cv2
import numpy as np

# Video dosyasını okumak için VideoCapture nesnesi oluşturulur.
cap = cv2.VideoCapture("footbridge.mp4")

# Arka plan çıkarıcı (background subtractor) oluşturulur.
# MOG2 algoritması kullanılır. Bu algoritma, bir pikselin arka plana ait olup olmadığını belirlemek için bir karmaşık bir olasılık modeli kullanır.
# history: Arka plan modelinin geçmiş kare sayısı.
# varThreshold: Bir pikselin arka plana ait olup olmadığını belirlemede kullanılan varyans eşik değeri.
# detectShadows: Gölge pikselleri algılanıp algılanmayacağını belirler.
sub = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=75, detectShadows=True)

while True:
    # Video akışından bir kare okunur.
    ret, frame = cap.read()

    # Arka plan çıkarıcı kullanılarak maske oluşturulur.
    mask = sub.apply(frame)

    # Klavyeden "q" tuşuna basıldığında döngüden çıkılır.
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

    # Orijinal kare ve maske ekranda gösterilir.
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

# Video akışı serbest bırakılır ve pencereler kapatılır.
cap.release()
cv2.destroyAllWindows()
