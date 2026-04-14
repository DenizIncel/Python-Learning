# İleri Veri Yapıları #

#Python’un standart kütüphanesinde çok pratik araçlar var. Bunlar büyük projelerde işleri çok kolaylaştırıyor.

#! collections modülü:
#Counter → eleman sayma
#defaultdict → varsayılan değerli sözlük
#deque → hızlı kuyruk / stack yapısı

#? Counter   
#*Liste veya string içindeki elemanların kaç defa geçtiğini sayar.
from collections import Counter

sayilar = [1,1,2,2,2,3,3,3,3,3,4,] #listede eleman sayma
c = Counter(sayilar)
print(c)        #Output: Counter({3: 5, 2: 3, 1: 2, 4: 1})  Counter({Sayi:Kaç defa geçtiği,....})


kelime = "engineering"  #string içinde harf sayma
print(Counter(kelime))      #Output: Counter({'e': 3, 'n': 3, 'g': 2, 'i': 2, 'r': 1})

# Avantaj: Normalde bunu for döngüsü + sözlük ile uzun yazardın. Counter tek satırda hallediyor.


#* ORNEK: Bir cümledeki kelimelerin kaç defa geçtiğini Counter ile saymayı dener misin?

cumle = ["deniz", "gelmis", "deniz", "gitmis", "deniz", "nereye", "gitmis"] 
kel_sayisi = Counter(cumle)
print(kel_sayisi)   #Output: Counter({'deniz': 3, 'gitmis': 2, 'gelmis': 1, 'nereye': 1})



#? defaultdict

#Normal dict ile sorun
#d = {}
#d["elma"] += 1   #Hata verir çünkü elma anahtarı daha önce yok.


#Çözüm: defaultdict
from collections import defaultdict

d = defaultdict(int) #varsayilan değer: 0
d["elma"] += 1
d["armut"] += 2
print(d)  #Output: defaultdict(<class 'int'>, {'elma': 1, 'armut': 2})

#Normal dict + kontrol if’leri yerine daha kısa bir yoldur

#? deque   (double-ended queue)

#Normal listelerde baştan eleman silmek (pop(0)) yavaştır çünkü tüm elemanları kaydırır.
#deque ise baştan/sondan ekleme–silme işlemlerini çok hızlı yapar.

from collections import deque

d = deque([1,2,3])

d.append(4) #sona ekle
d.appendleft(0)
print(d)  #Output: deque([0, 1, 2, 3, 4])

d.pop()
d.popleft()
print(d)  #Output: deque([1, 2, 3])

#Yani: deque, list’in kuyruk versiyonu gibidir.


#! heapq (min-heap / öncelikli kuyruk)

#Heap = öncelikli kuyruk veri yapısı.
#Python’un heapq modülü listeyi heap gibi kullanmanı sağlar.

import heapq

liste = [5,7,3,9,1]
heapq.heapify(liste)  #listeyi heap yap.
print(liste)  #Output: [1, 5, 3, 9, 7]    (sıralı gibi değil, heap düzeninde)

print(heapq.heappop(liste))  # en küçük elemanı çıkar → 1
print(heapq.heappop(liste))  # sonraki küçük → 3


#*Eleman ekleme

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 7)
print(heap)                 #Output: [5, 10, 7]   (heap düzeni)
print(heapq.heappop(heap))  #Output: 5   (en küçük çıkar)

#Nerde kullanılır: En küçük / en büyük elemanı hızlı bulmak istediğinde.