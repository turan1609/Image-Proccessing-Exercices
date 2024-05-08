import cv2
import numpy as np

canvas = np.zeros((600, 600, 3), np.uint8) + 255

cv2.imshow("pencere", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()