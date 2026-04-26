# Fonksiyonları kullanalım.

import sqlite3

# Tablo ve database yoksa oluşturan fonksiyon
def create_table():
    connection = sqlite3.connect("data/movies.db")
    cursor = connection.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Movies
            (
            title TEXT,
            rating REAL
            )
        """
    ) # REAL, SQLite'daki FLOAT'dır.
    connection.commit()
    connection.close()

def add_movie(movie_title, movie_rating):
    connection = sqlite3.connect("data/movies.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Movies (title,rating) VALUES (?,?)", (movie_title,movie_rating))

    connection.commit()
    connection.close()

# Fonksiyonları çağıralım
create_table()
add_movie("Prestige",8.5)
add_movie("Inception",8.8)
add_movie("Titanic",7.9)
add_movie("Wenom",6.6)
add_movie("Black Adam",6)
add_movie("LOTR: The Return of the King",9)
add_movie("The Dark Knight",9.1)
add_movie("Cats",2.8)
add_movie("The Room",3.7)