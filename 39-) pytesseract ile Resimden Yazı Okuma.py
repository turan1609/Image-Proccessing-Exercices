from PIL import Image  # PIL kütüphanesinden Image modülünü içe aktarın.
import pytesseract  # pytesseract kütüphanesini içe aktarın.

# "yazi.png" adlı görüntü dosyasını açın.
img = Image.open("yazi.png")

# pytesseract.image_to_string() fonksiyonuyla görüntüdeki metni okuyun.
# lang parametresi, tanıma işlemi için kullanılacak dilin belirlenmesini sağlar.
# Bu örnekte "eng" (İngilizce) dili kullanılıyor.
text = pytesseract.image_to_string(img, lang="eng")

# Tanınan metni ekrana yazdırın.
print(text)
