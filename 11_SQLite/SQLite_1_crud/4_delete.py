import sqlite3

connection = sqlite3.connect("data/game_data.db")
cursor = connection.cursor()

#! Veri tabanından birini silelim.

# Hile yapan bir oyuncu olsun ve onu silelim.

suspected_player = input("Enter the player suspected cheater or toxic: ").title()

cursor.execute("DELETE FROM Players WHERE name=? ",(suspected_player,))

# suspected_player 'dan sonra , olmazsa hata veriyor.


connection.commit()

connection.close()