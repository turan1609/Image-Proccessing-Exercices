#Canny Kenar Tespiti
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#gray frame e çevirmek daha iyi çalışılmasını sağlar
    kenar = cv2.Canny(gray_frame, 50, 50)#son iki değeri azalttıkça daha fazla kenar görür

    cv2.imshow("o", frame)
    cv2.imshow("c", kenar)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()