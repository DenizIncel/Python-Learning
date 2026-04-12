import json

# 1. ADIM: Elimizde Python formatında bir veri var (Sözlük/Dictionary)
sensor_verisi = {
    "cihaz_id": "SENSOR_001",
    "konum": "Fabrika_Giris",
    "olcumler": [
        {"zaman": "10:00", "sicaklik": 22.5, "nem": 45},
        {"zaman": "10:05", "sicaklik": 23.0, "nem": 46}
    ],
    "aktif_mi": True
}

print("--- 1. Veri Yazılıyor ---")
# 'w' modu (write) ile dosyayı açıyoruz.
# encoding='utf-8' Türkçe karakter sorunu olmasın diye önemlidir.
with open("sensor_log.json", "w", encoding="utf-8") as dosya:
    # Python sözlüğünü JSON formatına çevirip dosyaya döküyoruz (dump)
    # indent=4, dosyanın okunaklı (girintili) olmasını sağlar.
    json.dump(sensor_verisi, dosya, indent=4)
    print("Veri 'sensor_log.json' dosyasına kaydedildi!")

print("\n--- 2. Veri Okunuyor ---")
# Şimdi sanki başka bir programmışız gibi dosyayı okuyalım.
# 'r' modu (read) ile açıyoruz.
with open("sensor_log.json", "r", encoding="utf-8") as dosya:
    okunan_veri = json.load(dosya)

# Artık veri Python sözlüğü oldu, istediğimiz gibi kullanabiliriz.
print(f"Cihaz ID: {okunan_veri['cihaz_id']}")
print(f"Son Sıcaklık: {okunan_veri['olcumler'][-1]['sicaklik']} Derece")