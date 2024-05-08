#Şekil oluşturma
import cv2
import numpy as np

canvas = np.zeros((500, 500, 3), np.uint8) + 255
#Line oluşturma
cv2.line(canvas, (100, 100), (300, 300), (0, 0, 255), thickness = 5)

cv2.line(canvas, (300, 100), (100, 300), (0, 255, 0), thickness = 5)
#Rectngle oluşturma
cv2.rectangle(canvas, (100, 100), (300, 300), (0, 255, 0), 4)#4 ü -1 yaparsan karenin içini doldurur
#Daire Oluşturma
cv2.circle(canvas, (200, 200), 100, (255, 0, 0), 4)
# Üçgen oluşturma
u1 = (200, 100)
u2 = (100, 300)
u3 = (300, 300)

cv2.line(canvas, u1, u2, (0, 0, 0), 4)
cv2.line(canvas, u2, u3, (0, 0, 0), 4)
cv2.line(canvas, u1, u3, (0, 0, 0), 4)

cv2.imshow("pencere", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()