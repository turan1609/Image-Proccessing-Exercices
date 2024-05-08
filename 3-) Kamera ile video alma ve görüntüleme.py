#Kamera ile video alma ve görüntüleme
import cv2
cap = cv2.VideoCapture(0)
dosyaadi = "C:/video/1.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
framerate = 30
resolution = (640, 480)
output = cv2.VideoWriter(dosyaadi, codec, framerate, resolution)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    output.write(frame)
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q") :
        break
    cv2.waitKey(30)
output.release()
cap.release()
cv2.destroyAllWindows()