#Track Bar ile Maskeleme İşlemi
'''Renk Uzayına Dönüşüm: Görüntü, işlem yapmak için uygun bir renk uzayına dönüştürülür. Özellikle,
 HSV (Ton, Doyma, Parlaklık) veya LAB (Renk Uzayı, A ve B bileşenleri) renk uzayları, renklerin belirgin bir
 şekilde tanımlanmasına ve işlenmesine olanak tanır.
Alt ve Üst Sınırların Belirlenmesi: İlgilenilen rengin alt ve üst sınırları belirlenir. Bu sınırlar, maskeleme
işlemi sırasında hangi renklerin seçileceğini belirler.
Maskenin Oluşturulması: Belirlenen renk aralığına sahip pikselleri içeren bir maske oluşturulur. Bu maske,
ilgilenilen renk aralığındaki her pikseli belirli bir değere (genellikle 255 veya beyaz) ayarlar ve geri kalan
 pikselleri diğer bir değere (genellikle 0 veya siyah) ayarlar.
Maske Uygulaması: Oluşturulan maske, orijinal görüntüye uygulanır. Bu, maskeleme işlemi sonucunda sadece
ilgilenilen renk aralığına sahip piksellerin vurgulanmasını veya seçilmesini sağlar.
Sonuç Görselleştirme veya İşleme: Maske uygulandıktan sonra, sonuç genellikle görüntülenir veya daha fazla
işleme adımına tabi tutulabilir. Bu adımlar, belirli bir nesne veya özelliklerin izole edilmesi, takibi veya
tanımlanması gibi görsel bilgi işleme uygulamalarında kullanılabilir.'''
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

def fonks(x):
    pass

cv2.namedWindow("bar")
cv2.resizeWindow("bar", 600, 600)

cv2.createTrackbar("alh-h", "bar", 0, 180, fonks)
cv2.createTrackbar("alh-s", "bar", 0, 255, fonks)
cv2.createTrackbar("alh-v", "bar", 0, 255, fonks)

cv2.createTrackbar("ust-h", "bar", 0, 180, fonks)
cv2.createTrackbar("ust-s", "bar", 0, 255, fonks)
cv2.createTrackbar("ust-v", "bar", 0, 255, fonks)

cv2.setTrackbarPos("ust-h", "bar", 150)
cv2.setTrackbarPos("ust-s", "bar", 200)
cv2.setTrackbarPos("ust-v", "bar", 200)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)#Burda videonun sağ-sol aynalamasını yaptık
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# Burda renk uzayı değiştirdik

    alt_h = cv2.getTrackbarPos("alh-h", "bar")
    alt_s = cv2.getTrackbarPos("alh-s", "bar")
    alt_v = cv2.getTrackbarPos("alh-v", "bar")

    ust_h = cv2.getTrackbarPos("ust-h", "bar")
    ust_s = cv2.getTrackbarPos("ust-s", "bar")
    ust_v = cv2.getTrackbarPos("ust-v", "bar")

    alt_renk = np.array([alt_h, alt_s, alt_v])
    ust_renk = np.array([ust_h, ust_s, ust_v])

    mask = cv2.inRange(frame_hsv, alt_renk, ust_renk)

    cv2.imshow("original", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()