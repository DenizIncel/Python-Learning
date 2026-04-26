import sqlite3

#! LIKE arama motoru gibidir. Bat yazdığında Batman, Batmobile gibi sonuçları getirir.
# SQL'de % işareti "öncesinde veya sonrasında ne olduğu umurumda değil" demektir.
#Örnek: WHERE title LIKE '%The%' (Başlığın neresinde olursa olsun içinde "The" geçenleri getirir).

#! MAX,MIN,COUNT,AVG,SUM gibi fonksiyonlar da SQL'de kullanılabilir.



#! Dışardan keyword alıp kullanalım.

def search_movie(keyword):
    connection = sqlite3.connect("data/movies.db")
    cursor = connection.cursor()

    search_term = f"%{keyword}%"

    cursor.execute(f"SELECT * FROM Movies WHERE title LIKE ?", (search_term, )) # virgül olmazsa hata veriyor.
    
    results = cursor.fetchall()
    connection.close()
    return results

print(search_movie("The"))


#! Hazır fonksiyonları deneyelim.

def get_movie_stats():
    connection = sqlite3.connect("data/movies.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            MAX(rating),
            AVG(rating)
            FROM Movies
    """)

    movie_stats = cursor.fetchone()

    print("Movie Statistics")
    print(f"Number of movies: {movie_stats[0]}")
    print(f"Highest rating: {movie_stats[1]}")
    print(f"Average rating: {movie_stats[2]:.2f}")  # :.2f ile virgülsen sonra 2 basamak yazdırdık.

    connection.close()

get_movie_stats()