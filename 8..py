#Yazı Ekleme
import cv2
import numpy as np

canvas = np.zeros((600, 600, 3), np.uint8) + 255

font1 = cv2.FONT_ITALIC
font2 = cv2.FONT_HERSHEY_PLAIN
font3 = cv2.CAP_ANDROID

cv2.putText(canvas, "merhaba", (30, 200), font1, 4, (255, 0, 0), cv2.LINE_AA)

cv2.imshow("pencere", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()