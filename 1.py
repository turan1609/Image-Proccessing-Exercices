#İMG açma kaydetme 
import cv2
#img = cv2.imread("img.jpg") #img değişkenine resmi atadık
img = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)# resmi gri tonlamalı alır
#print(img) matris değerleri gösterir
cv2.namedWindow("image", cv2.WINDOW_NORMAL)#açılan pencereyi boyutlandırabilmeyi sağlar
cv2.imshow("image", img)#ilk parametre pencerenin ismi , ikinci parametre nesnenin ismi
cv2.imwrite("copy.jpg", img)
cv2.waitKey(0)#delay yi içine yazarız