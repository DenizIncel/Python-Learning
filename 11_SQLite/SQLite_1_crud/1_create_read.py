#SQL (Structured Query Language - Yapılandırılmış Sorgu Dili)

#? SQLite
#Sunucu gerektirmeyen, kurulum yapılmasına ihtiyaç duymayan, hafif ve dosya tabanlı bir veritabanı yönetim sistemidir


import sqlite3

#! 1. Adım: Bağlantı kurma

connection = sqlite3.connect("data/game_data.db") # "game_data.db" dosyasına bağlanıyoruz. Eğer klasörde yoksa otomatik oluşturur.
cursor = connection.cursor()  # cursor: Veri tabanıyla konuşmamızı sağlayan araç.

#! 2. Adım: Tablo oluşturma

# cursor.execute(): SQL emrini depoda uygula demektir.
# 3 tırnak kullanmamızın sebebi daha okunur yapmak.

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Players(
            name TEXT,
            level INTEGER
            )
""")

#! 3. Adım: Veri ekleme

# Tabloya yeni oyuncular ekleyelim.
cursor.execute("INSERT INTO Players (name, level) VALUES ('Faker', 30)")
cursor.execute("INSERT INTO Players (name, level) VALUES ('Caps', 28)")
cursor.execute("INSERT INTO Players (name, level) VALUES ('Toxic Teemo', 20)")

# Yapılan eklemeleri veritabanına kalıcı olarak kaydedelim.
connection.commit()

#! 4. Adım: Veri okuma

# Players tablosundaki tüm verileri (*) getirmesini istiyoruz.
cursor.execute("SELECT * FROM Players")

# Depodan getirilen tüm sonuçları bir değişkene atalım.
all_players = cursor.fetchall()  
# fetchall() : Herşeyi alıp getir demek.
# fetchone():  Tek satır getirir.

print("Players fetched from the database:")

for player in all_players:
    print(player)

#! 5. Adım: Kapıyı kapatma
# Güvenlik ve performans için connection.close() kullanırız.
connection.close()