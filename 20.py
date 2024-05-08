#Corners Metodu ile köşe tespiti
import cv2
import numpy as np

img = cv2.imread("ucgen.jpg")

#önce gri tonlamaya çeviricez
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#floata çevirmemiz lazım ki sonraki adımda float değer girebilelim
gri = np.float32(gri)
#burda ayarlamaları yapıcaz
#(işlem yapılacak nesne, max köşe sayısı, kalite leveli, köşelr arası min uzaklık)
corner = cv2.goodFeaturesToTrack(gri, 40, 0.01, 10)
#şimdide floattan int a çeviricez
corner = np.int32(corner)
#corner üzerinde gezme işlemi yapıcaz
for c in corner:
    x, y = c.ravel()

    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

cv2.imshow("ucgen", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
