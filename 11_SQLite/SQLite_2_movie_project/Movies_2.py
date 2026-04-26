import sqlite3

#! SQLite'da filtreleme yapabilir ve sıralayabiliriz.

# Movies_1 de fonksiyonlarla oluşturduğumuz Database'den verileri çekelim.
def get_movies():
    connection = sqlite3.connect("data/movies.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Movies")
    all_movies = cursor.fetchall()

    connection.close()
    return all_movies

all_movies = get_movies()

for movie in all_movies:
    print(f"Title: {movie[0]}, Rating: {movie[1]}") # movie[0] title, movie[1] rating'e karşılık geliyor

print("-" * 30)

#! Puanı 8'den yüksek olan filmleri filtereyelim ve sadece en yüksek 2 tanesini gösterelim.

def read_top_movies():
    connection = sqlite3.connect("data/movies.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Movies WHERE rating > 8 ORDER BY rating DESC LIMIT 2")
    top_movies = cursor.fetchall()
    # WHERE koşulu belirler. 
    # ORDER BY sıralama yapar. 
    # DESC azalan sırada sıralar. 
    # LIMIT ise kaç sonuç getireceğini belirler.

    connection.close()
    return top_movies

top_movies = read_top_movies()

for movie in top_movies:
    print(f"Title: {movie[0]}, Rating: {movie[1]}")
