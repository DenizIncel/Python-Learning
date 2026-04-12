# MİRAS ALMA (INHERITANCE) #

#Ortak özellikleri üst sınıfta tutarken alt sınıfa sadece farkları yazılır. Bu da çok fazla kolaylık sağlar.

class Hayvan:
    def __init__(self,isim):
        self.isim = isim
    
    def ses_cikar(self):
        print("Bir hayvanin sesi...")


class Kedi(Hayvan):
    def ses_cikar(self): #override
        print(f"{kedi.isim}: Miyav!")

class Kopek(Hayvan):
    def ses_cikar(self):
        print(f"{kopek.isim}: Hav hav!")


tavsan = Hayvan("Den")
tavsan.ses_cikar()
kedi = Kedi("Maya")
kopek = Kopek("Karabas")
kedi.ses_cikar()
kopek.ses_cikar()


# Polimorfizm #

class Sekil:
    def alan(self):
        pass

class Kare(Sekil):
    def __init__(self, kenar):
        self.kenar = kenar
    
    def alan(self):
        return self.kenar * self.kenar

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap
    
    def alan(self):
        return 3.14 * self.yaricap * self.yaricap


sekiller = [Kare(4), Daire(3)]

for s in sekiller:
    print(s.alan())


# KAPSULLEME (Encapsulation) #

#Nesnenin "içini" kapsülleyip sadece izin verilen yöntemlerle dışarı açar.
# C# dilindeki gibi (private,public,protected) katı kurallar yok.Ama isimlendirme kuralları var:

#Public: her yerden erişilebilir
class Ogrenci1:
    def __init__(self,isim,numara):
        self.isim = isim #public
        self.numara = numara #public

#Protected: _ ile başlar. Dışardan izin verilmedikçe erişilemez.
class Ogrenci2:
    def __init__(self,x,y):
        self._not = 85 #protected

#Private: __ ile başlar. Python değişken adını değiştirerek gizler.
class Ogrenci3:
    def __init__(self,a,b):
        self.__tc = "12345678910" #private


# Get ve Set Metotları #   özel alanlara erişmek için kullanılır.

class Ogrenci4:
    def __init__ (self,isim,numara):
        self.isim = isim
        self.__numara = numara

    def get_numara(self):
        return self.__numara
        
    def set_numara(self,yeninum):
         if isinstance(yeninum,int):  #konu dışı isintance ile değişkenin türü bu mu diye sorabilirsin.
            self.__numara = yeninum
         else:
             print("Numara sadece sayi olabilir.")


o4 = Ogrenci4("Ali",105)
print(o4.get_numara())  # Output: 105

o4.set_numara(205)
print(o4.get_numara()) # Output: 205