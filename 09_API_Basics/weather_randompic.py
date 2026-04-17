import requests
import json

#! Rastgele köpek resmi alma

cevap = requests.get("https://dog.ceo/api/breeds/image/random", timeout=5)
rastgele_resim = cevap.json()
print(rastgele_resim)

#! Hava durumnu alma

hava_durumu = requests.get("https://api.open-meteo.com/v1/forecast?latitude=37.76&longitude=30.55&current_weather=true")
print(hava_durumu.status_code)
veriler = hava_durumu.json()

duzenli_veriler = json.dumps(veriler, indent=4) 
print(duzenli_veriler)


print("Sıcaklık:", veriler["current_weather"]["temperature"], "°C")


with open("hava_durumu.json", "w") as dosya:
    json.dump(veriler, dosya, indent=4)
