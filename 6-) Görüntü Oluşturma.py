#Görüntü Oluşturma
import cv2
import numpy as np

img_with_three_trial = np.zeros((20,20,3), np.uint8) + 255


img_with_three_trial[0,0] = (0, 0, 0)
img_with_three_trial[0,1] = (50, 0, 0)
img_with_three_trial[0,2] = (100, 0, 0)
img_with_three_trial[0,3] = (150, 0, 0)
img_with_three_trial[0,4] = (200, 0, 0)

img_with_three_trial = cv2.resize(img_with_three_trial, (500, 500), interpolation = cv2.INTER_AREA)
cv2.imshow("pencere1", img_with_three_trial)

img_with_one_trial = np.zeros((20, 20), np.uint8) + 255
img_with_one_trial[0,0] = 255
img_with_one_trial[0,1] = 200
img_with_one_trial[0,2] = 150
img_with_one_trial[0,3] = 100
img_with_one_trial[0,4] = 50
img_with_one_trial[0,5] = 0

img_with_one_trial = cv2.resize(img_with_one_trial, (500, 500), interpolation = cv2.INTER_AREA)




cv2.imshow("pencere2", img_with_one_trial)
cv2.waitKey(0)
cv2.destroyAllWindows()