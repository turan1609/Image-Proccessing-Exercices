import cv2
img = cv2.imread("C:/Users/turan/Desktop/Yusuf/IMG-20211212-WA0005")
img = cv2.resize(img,(400,300))#resmi boyutlandırdık
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.imwrite("copy.jpg", img)
cv2.waitKey(0)