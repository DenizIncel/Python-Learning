# Hata Yönetimi ve İstisnalar (Exceptions) #



#*      try / except → hatayı yakala

#!      except HataTipi → sadece belli hatayı yakala

#?      finally → her durumda çalış

#TODO   raise → kendin hata fırlat

#!      param Özel exception → kendi hata türünü yaz


#Python’da hata olunca program durur ama büyük projelerde bu kabul edilemez → “hata olsa bile program düzgün davransın” isteriz.
#Bunun için try / except yapısı var.

#? Basit try/except

try:
    sayi = int("abc")  # hata: string -> int dönüşemez.
except:
    print("Bir hata olustu")

#Normalde program kırılırdı ama except yakaladığı için devam eder.



#!  Hata Türünü Belirtmek
#Her hatanın bir türü vardır (ValueError, ZeroDivisionError, FileNotFoundError vs.).

try:
    x = 10/0
except ZeroDivisionError:        #sadece bu hata için çalışır.
    print("Sifira bolme hatasi")



#*  finally

try:
    f = open("dosya.txt")
except FileNotFoundError:
    print("Dosya bulunamadi")
finally:                    # hata olsa da çalışır
    print("Islem bitti")


 
#? raise

#kendi hatanı oluşturabilirsin
#Kütüphane, API ya da büyük program yazıyorsan, kullanıcının anlaması için özel hata mesajı fırlatabilirsin.


def bolme(a,b):
    if b==0:
        raise ZeroDivisionError("Bolen sifir olamaz!")
    return a/b

print(bolme(10,2)) # Output: 5
print(bolme(5,0)) # Hata fırlatır.




#! Özel Exception Sınıfı
#kendi hata tipini tanımlayabilirsin.

class NegatifSayiHatasi(Exception):
    pass

def karekok(sayi):
    if sayi < 0:
        raise NegatifSayiHatasi("Negatif sayının karekökü alınamaz!")
    return sayi ** 0.5

print(karekok(9))   # 3.0
print(karekok(-4))  # hata fırlatır
