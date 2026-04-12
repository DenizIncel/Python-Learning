# OOP (Nesne Tabanlo Programlama) #

#Class oluşturma
class Araba:
    pass

#Nesne(Object) oluşturma
a1 = Araba()  #Araba sınıfından bir nesne oluşturduk.
a2 = Araba()

#Özellik(Attribute) ekleme
a1.Marka = "Toyota"
a1.Renk = "Kirmizi"
print(a1.Marka + " " +a1.Renk)
#Ama bu yöntem dağınık olur. Bunun yerine sınıfa kurucu metot koyarız.


#Yapıcı(Constructor)  __init__ : nesne kurulumunu yapar. Nesne oluşturulduğunda otomatik çalışan özel metottur.
class Araba2:
    def __init__(self,marka,renk):  #self: Her sınıf metodunun ilk parametresi self olmalıdır..bu nesnenin kendisi anlamına gelir.
        self.marka = marka  #bu arabaya ait marka demiş oluyoruz
        self.renk = renk

# class: kimlik tasarım şablonu,init: isim,numara gibi bilgilerin yazıldığı aşamadır.
# self:bu kimlik kime ait sorusunun cevabıdır.

a3 = Araba2("BMW","Beyaz")
a4 = Araba2("Mercedes","Siyah")

print(a3.marka, a3.renk)