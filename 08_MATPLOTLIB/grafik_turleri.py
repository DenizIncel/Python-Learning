import matplotlib.pyplot as plt
import numpy as np

# --- VERİ HAZIRLIĞI (Simülasyon) ---
# 1. Çizgi Grafik için (Sinyal)
zaman = np.linspace(0, 10, 100)
voltaj = np.sin(zaman) # Sinüs dalgası

# 2. Scatter için (Sınıflandırma Verisi)
boy = np.random.randint(150, 200, 50) # 150-200 arası rastgele boy
kilo = np.random.randint(50, 100, 50) # 50-100 arası rastgele kilo

# 3. Histogram için (Sensör Hataları - Normal Dağılım)
hatalar = np.random.randn(1000) # Ortalaması 0 olan 1000 tane rastgele sayı

# 4. Bar Grafik için (Model Performansı)
modeller = ['Model A', 'Model B', 'Model C']
basari_orani = [88, 95, 70]

# --- GÖRSELLEŞTİRME (Dashboard Yapımı) ---
# 2 Satır, 2 Sütunluk bir tablo oluşturuyoruz (toplam 4 grafik)
plt.figure(figsize=(12, 8)) # Pencere boyutu (Genişlik, Yükseklik)

# -- 1. Grafik: Sinyal (Sol Üst) --
plt.subplot(2, 2, 1) # 2x2'lik alanın 1.si
plt.plot(zaman, voltaj, color='blue', linewidth=2)
plt.title('1. Sinyal Analizi (Line Plot)')
plt.xlabel('Zaman (sn)')
plt.ylabel('Voltaj (V)')
plt.grid(True) # Izgara ekle (Okumayı kolaylaştırır)

# -- 2. Grafik: Boy-Kilo İlişkisi (Sağ Üst) --
plt.subplot(2, 2, 2) # 2x2'lik alanın 2.si
plt.scatter(boy, kilo, color='red', marker='x') # x işareti koy
plt.title('2. Veri Dağılımı (Scatter Plot)')
plt.xlabel('Boy (cm)')
plt.ylabel('Kilo (kg)')

# -- 3. Grafik: Hata Dağılımı (Sol Alt) --
plt.subplot(2, 2, 3) 
plt.hist(hatalar, bins=20, color='green', edgecolor='black')
plt.title('3. Üretim Hataları (Histogram)')
plt.xlabel('Hata Miktarı')

# -- 4. Grafik: Başarı Karşılaştırması (Sağ Alt) --
plt.subplot(2, 2, 4)
plt.bar(modeller, basari_orani, color=['orange', 'purple', 'cyan'])
plt.title('4. Model Performansları (Bar Chart)')
plt.ylim(0, 100) # Y eksenini 0-100 arası sabitle

# Başlıkların birbirine girmesini engeller
plt.tight_layout() 

plt.show()