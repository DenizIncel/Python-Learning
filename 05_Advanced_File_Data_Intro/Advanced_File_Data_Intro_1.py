# İleri Dosya ve Veri İşlemleri 1 #

#! Dosya Açma ve Kapama Mantığı

#Normalde open() ile açar veya oluştururuz, close() ile kapatırız. write() ve read() ile yazma/okuma yaparız.
#Ama genelde Python’da manuel kapatmak yerine güvenli yöntem kullanırız:  with open


with open("deneme.txt","r",encoding="utf-8") as f:
    veri = f.read()
    print(veri)

#with : iş bitince dosyayı otamatik kapatır (hata olsa bile).
#encoding="utf-8" : Türkçe karakter sorunu yaşamamak için.
#f.read : dosyanın tamamını okur.

#? Dosya Modları

#*  "r" → okuma (read)
#*  "w" → yazma (write) (varsa eski dosyayı siler, baştan yazar)
#*  "a" → ekleme (append) (eski içerik kalır, en sona ekler)
#*  "r+" → hem okuma hem yazma

# Yazma örneği
with open("deneme.txt", "w", encoding="utf-8") as f:
    f.write("Merhaba Python!\n")
    f.write("Bugün dosya işlemleri öğreniyorum.\n")


#!!! Pathlib (Dosya Yolu Yönetimi)

#Windows -> C:\Users\x\Desktop\dosya.txt
#Linux/Mac -> /home/x/dosya.txt

#Elle bu yolları yazmak zahmetli ama Python'da path ile çok temiz yapılabiliyor.

from pathlib import Path

p = Path("deneme.txt")  # dosya yolu artık bir Path nesnesi

with p.open("r",encoding="utf-8") as f:
    print(f.read())


#? Path sadece açmak için değil, aynı zamanda dosya/klasör kontrolü için de çok faydalı:

print(p.exists())      # Dosya var mı?
print(p.is_file())     # Bu bir dosya mı?
print(p.is_dir())      # Bu bir klasör mü?
print(p.name)          # dosya adı → deneme.txt
print(p.suffix)        # uzantı → .txt
print(p.stem)          # uzantısız adı → deneme
print(p.parent)        # üst klasör


#! Satır Satır Okuma (Büyük Dosyalar İçin)

with open("deneme.txt", "r", encoding="utf-8") as f:
    for satir in f:
        print(satir.strip())   # .strip() → boşluk/alt satır temizler