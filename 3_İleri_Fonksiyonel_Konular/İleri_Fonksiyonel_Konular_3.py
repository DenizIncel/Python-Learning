# Generator ve yield #

#Normal fonksiyon: fonksiyon çalışır,return ile sonucu döndürür ve sonra biter

def kareler(n):
    sonuc = []
    for i in range(n):  #range varsayilan 0 dan başlar.
        sonuc.append(i*i)
    return sonuc
print(kareler(6))

#? Generator Fonksiyon (yield)

#return yerine yield kullanırsan, fonksiyon listeyi tamamen üretmek yerine, ihtiyaç oldukça tek tek eleman üretir.
#Bu sayede bellek (RAM) tasarrufu olur.

def kareler_generator(n):
    for i in range(n):
        yield i*i      # her seferinde bir değer üretir.
g = kareler_generator(5)
print(next(g)) #0         #next: sıradaki değeri listeler.
print(next(g)) #1
print(next(g)) #4
# bitince StopIteration hatası verir

#Neden Kullanılır?
#Büyük veriyle çalışırken tüm listeyi hafızada tutmaz.
#Mesela 1 milyar sayının karesini hesaplamak generator ile mümkün, listeyle imkânsız olur.


#! Iterator
#Üzerinde sırayla gezilebilen nesne. Yani Python’da for döngüsü ile gezebildiğin her şey aslında bir iterator kullanır.

liste = [10,20,30]
it = iter(liste)  # listeden iterator oluşturur.
print(next(it))
print(next(it))   # next: sıradaki elemanı alır
print(next(it))

# for döngüsü aslında arka planda bunu kullanır. for = iter + next + StopIteration.


#* Kendi Iterator’unu Yazmak

class Sayilar:
    def __init__(self,n):
        self.n = n
        self.current = 0

    def __iter__(self): #iterator döndürür(genelde self).
        return self
    
    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        else:
            raise StopIteration
        
it2 = Sayilar(3)
for x in it2:
    print(x) #1,2,3


#TODO ÖZETLE

#iterable → üzerinde gezilebilen nesne (liste, string, tuple…).
#iterator → bu gezinmeyi sağlayan mekanizma (iter(), next()).
#for döngüsü aslında iterator protokolünü kullanıyor.
#İstersen kendi sınıfını da iterator yapabilirsin (__iter__, __next__).