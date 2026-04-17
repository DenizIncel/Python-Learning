import numpy as np

# 1. Python Listesi ile Deneme
liste = [1, 2, 3]
# Amacımız: Listedeki her sayıyı 10 ile çarpmak.
try:
    print(f"Liste Çarpımı: {liste * 10}") 
    # HATA! Matematik yapmaz, listeyi 10 kere yan yana yazar (Kopyalar).
except Exception as e:
    print(e)

print("-" * 30)

# 2. NumPy Dizisi (Array) ile Deneme
# Listeyi NumPy dizisine (vektöre) çeviriyoruz.
vektor = np.array([1, 2, 3])


print(f"NumPy Çarpımı: {vektor * 10}")
# SONUÇ: [10 20 30] -> Her elemanı tek tek çarptı!


# 1D Array (Vektör / Sinyal)
# Ses sinyali gibi tek sıra veri
sinyal = np.array([5, 10, 15, 20])
print(f"1D Sinyal Boyutu (Shape): {sinyal.shape}") 
# Çıktı: (4,) -> 4 elemanlı tek boyut.

# 2D Array (Matris / Gri Tonlamalı Resim)
# Excel tablosu veya siyah-beyaz resim gibi
# İç içe liste vererek matris oluştururuz.
matris = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(f"2D Matris Boyutu: {matris.shape}")
# Çıktı: (2, 3) = 2 Satır, 3 Sütun.

# Veriye Erişmek
# Matrisin 1. satır, 2. sütunundaki elemanı (Satır 0, Sütun 1)
print(f"Seçilen Eleman: {matris[0, 1]}") # Sonuç: 2


print("-" * 30)

# 1. SIFIR MATRİSİ (np.zeros)
# Görüntü işlemede boş siyah bir ekran oluşturmak için kullanılır.
siyah_ekran = np.zeros((3, 3)) 
print("Sıfırlar:\n", siyah_ekran)

# 2. BİR MATRİSİ (np.ones)
# Genelde maskeleme işlemlerinde veya ağırlık başlatmada kullanılır.
birler = np.ones((2, 4))
print("Birler:\n", birler)

# 3. ARANGE (Aralık)
# Belirli aralıklarla sayı üretir (for döngüsü için idealdir).
sayilar = np.arange(0, 10, 2) # 0'dan başla, 10'a kadar, 2'şer git.
print("Aralık:", sayilar)

# 4. LINSPACE (Linear Space)
# "0 ile 10 arasını eşit parçalara böl" demektir. Grafik çizerken X ekseni için kullanılır.
zaman = np.linspace(0, 10, 5) # 0 ile 10 arasında bana tam 5 tane sayı üret.
print("Eşit Bölünmüş Zaman:", zaman)