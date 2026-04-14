# JSON (JavaScript Object Notation) #

#! JSON Nedir?

#*  Hafif, insan tarafından okunabilir veri formatı.
#*  Web API’lerinden gelen yanıtların %90’ı JSON’dur.
#*  Python’daki karşılığı: dict (sözlük)

#? dict = key-value tabanlı veri yapısı
#? JSON = dict'in dosyahaline getirilmiş versiyonu



#Örnek bir JSON dosyası oluşturalım:  ogrenci.json
#dosyanın içi: 
"""
{
    "isim": "Deniz",
    "yas": 20,
    "ogrenci": true,
    "dersler": ["Matematik,Fizik,Kimya"]
}
"""

#! Python'da JSON ile çalışmak

#JSON dosyasını okumak
import json

with open("ogrenci.json", "r", encoding="utf-8") as ogr:
    veri = json.load(ogr)   #load: dosyadan oku
print(veri["isim"])  # Output:  Deniz
print(veri["yas"])   # Output:  20
print(veri["ogrenci"])   # Output:  True


#JSON dosyasına yazmak

import json

kisi = {
    "isim": "Ayse",
    "yas": 19,
    "ogrenci": False,
    "dersler": ["Programlama","Kalkulus"]
}

with open("yeni.json", "w", encoding="utf-8") as f:
    json.dump(kisi, f, indent=2)  #dump: dosyaya yaz  #indent=2: daha okunabilir olması için zorunlu değil.

