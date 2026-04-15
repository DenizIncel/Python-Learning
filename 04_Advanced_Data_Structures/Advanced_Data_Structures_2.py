# İleri Veri Yapıları 2#
#önemli

#! bisect (Binary Search – sıralı listeler)

#Normalde listeye eleman eklediğinde → list.insert() kullanırsın, ama liste sıralı kalmaz.
#bisect → elemanı doğru sıraya ekler, böylece liste sıralı kalmaya devam eder.

import bisect

liste = [1,3,4,7,9]

bisect.insort(liste,5)  # 5'i uygun yere ekle.
print(liste)

#Sıralı listelerde hızlı arama ve ekleme için kullanışlıdır.


#! itertools (ileri döngü araçları)
#Python’un sonsuz döngü & kombinasyon araç kutusu.

#? count() → sonsuz sayaç

import itertools
for i in itertools.count(10,2):  #10dan başla 2şer artır.
    if i > 20:
        break
    print(i)     #Çıktı olarak 10dan 20ye doğru 2şer olarak artar.
#range gibidir ama sonsuz çalışır. Sen break koymazsan hiç durmaz.


#? cycle() → sonsuz tekrar
#döngü bitince baştan başlar

import itertools

sayi = 0
for c in itertools.cycle(["a","b","c"]):
    print(c)
    sayi += 1
    if sayi == 5:
        break
#Çıktı alt alta ' a b c a b  ' olur.


#? combinations() → kombinasyonlar

import itertools
liste = [1,2,3]
for c in itertools.combinations(liste,2):
    print(c)
#Çıktı alt alta: ' (1, 2) (1, 3) (2, 3) ' olur
#Bu sayede kolayda kombinasyonlar oluşturulabilir.


#TODO ÖZET

#Counter, defaultdict, deque → hazır yapılara kısayol
#heapq, bisect → sıralı veri ve öncelik işleri
#itertools → ileri döngü ve kombinasyon işleri