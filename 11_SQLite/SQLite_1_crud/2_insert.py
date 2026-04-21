import sqlite3

connection = sqlite3.connect("data/game_data.db")
cursor = connection.cursor()

#! Kullanıcıdan veri alıp veri tabanına kaydedelim.

new_player = input("Enter the new player name: ")
new_level = int(input("Enter the player's level: "))

# VALUES kısmına ? koyuyoruz. Virgülden sonra değişkenlerimizi sırasıyla yazıyoruz.
cursor.execute(f"INSERT INTO Players (name, level) VALUES (?,?)", (new_player, new_level))

connection.commit()  # Değişikliği kaydeder.

print(f"{new_player} added successfully.")


connection.close()   # Bağlantıyı kapatır.