#Video çekme
import cv2
cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    if ret == 0 :
        break

    frame = cv2.flip(frame,1)
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q") :
        break

cap.release()
cv2.destroyAllWindows()