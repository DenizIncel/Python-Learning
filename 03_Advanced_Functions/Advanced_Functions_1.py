# İleri Fonksiyonel Konular #

#Daha kısa, okunaklı ve verimli kod yazmayı öğreneceğin yer burası.


#!  Lambda Fonksiyonları 

#Normalde def ile fonksiyon yazıyoruz ama bazen tek satırlık, küçük bir fonksiyon lazım oluyor. İşte burada lambda devreye giriyor.

#Yazım şekli: lambda parametreler:ifade

kareal = lambda x : x*x
print(kareal(6))
topla = lambda a,b : a+b
print(topla(3,7))


#? map, filter, reduce
#Bunlar fonksiyonel programlama araçları → liste/sözlük gibi veriler üzerinde işlem yapmayı kısaltıyor.

#map → Her elemana fonksiyon uygular
#filter → Koşulu sağlayanları seçer
#reduce → Hepsini tek değere indirir

# map()          #Bir listedeki her elemana fonksiyon uygular.

sayilar = [1,2,3,4,5]
kareler = list(map(lambda x : x*x,sayilar))  #list kullanarak map in sonucunu tekrar list e çevirdik.
print(kareler)


# filter()      #Bir listedeki elemanları filtreler.
sayilar = [1,2,3,4,5,6]
ciftler = list(filter(lambda x : x%2 == 0, sayilar))
print(ciftler)


# reduce()      #Bir listeyi tek bir değere indirger.
#Bunun için functools kütüphanesinden import edilir.
from functools import reduce

sayilar = [1, 2, 3, 4, 5]
carpim = reduce(lambda a, b: a * b, sayilar)
print(carpim)   # 120 (1*2*3*4*5)
