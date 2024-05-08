# IMG lerde Renk Uzayları ve dönüşümleri
import cv2
img_bgr = cv2.imread("img.jpg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)# mavi yeşil kırmızıyı kırmızı yeşil maviye dönüştürdük
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

cv2.imshow("araba", img_bgr)
cv2.imshow("rgb", img_rgb)
cv2.imshow("hsv", img_hsv)
cv2.imshow("gray", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()