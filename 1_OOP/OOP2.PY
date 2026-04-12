# OOP2 #

# Metot Çeşitleri: normal metotlar, classmethod ve staticmethod.

#Normal metot -> Nesneye bağlıdır.                  --> "Öğrenciye ait bilgi göster."
#Class method -> Sınıfın kendisine bağlıdır.        --> "Tüm öğrenciler aynı okulda,okul bilgisi ver."
#Static method -> Sınıfla ilgili ama bağımsızdır.   --> "Yardımcı işlemler örneğin: kare alma,yüzdelik hesaplama vs."

# NORMAL METHOD
class ogrenci:
    def __init__(self,isim,numara):
        self.isim = isim
        self.numara = numara

    def bilgi_goster(self): #normal metot
        print(f"Isim: {self.isim}\nNumara: {self.numara}")

o1 = ogrenci("Deniz",101)
o1.bilgi_goster()

# CLASS METHOD
class bisiklet:
    bsk_renk = "Kirmizi" #sınıf değişkeni
    def __init__(self,isim):
        self.isim = isim

    @classmethod
    def bsk_bilgi(cls):  #cls: class'ın kendisi
        print(f"Bisiklet {cls.bsk_renk} renginde")

bisiklet.bsk_bilgi()  # Bu bisiklet kırmızı


class Matematik:
    @staticmethod
    def kare_al(sayi):
        return sayi * sayi
    
print(Matematik.kare_al(5))