import sqlite3

connection = sqlite3.connect("data/game_data.db")
cursor = connection.cursor()


#! Veri tabanında deeğişiklik yapalım.

cursor.execute("UPDATE Players SET level = 31 WHERE name='Caps' ")


#! Kullanıcıdan aldığımız bilgiye göre veri tabanını değiştirelim.

print("Update the user's information\n")

target_player = input("Enter the name of the user: ").title()
new_level = int(input("Enter the user's new level: "))

cursor.execute("UPDATE Players SET level = ?  WHERE name = ? ",(new_level, target_player))


connection.commit() 

connection.close()
