# List / Dict Comprehension # (İleri pratik)
#Tek satırda liste/sözlük üretme.
#Python’da çok kullanılan, kodu kısacık ve okunaklı hale getiren bir yazım tarzı.

#*Normal Yöntem

sayilar = [1,2,3,4,5]
kareler = []
for s in sayilar:
    kareler.append(s * s)
print(kareler)  # [1,4,9,16,25]


#! Comprehension #              #"Tek satırda bir şeyler üretme, türetme"

sayilar = [1,2,3,4]
kareler = [s*s for s in sayilar]
print(kareler)
#tek satırda for döngüsü gibi çalışıyor.


#? Koşullu Durumlar

sayilar = [1,2,3,4,5,6]
ciftler = [s for s in sayilar if s%2==0]
print(ciftler)


#* Dict Comprehension           #"sözlük türetme"

sayilar = [1,2,3,4,5]
kare_dict = {s: s*s for s in sayilar}
print(kare_dict)    # Output: {1: 1, 2: 4, 3: 9, 4: 16}


# [] -> liste üretir.
# {} -> sözlük üretir.


