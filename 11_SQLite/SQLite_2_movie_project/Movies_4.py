import sqlite3

#! JOIN ile birden fazla tabloyu birleştirebiliriz.
# Örneğin filmler ve aktorler tablolarını birleştirebiliriz.


def test_join():
    connection = sqlite3.connect("data/movies.db")
    cursor = connection.cursor()

    # Yeni tablo kuralım. Hasılat bilgileri ekleyelim.
    cursor.execute("CREATE TABLE IF NOT EXISTS BoxOffice (movie_title TEXT, revenue_millions INTEGER)")

    cursor.execute("DELETE FROM BoxOffice") # üst üste eklenmemesi için siliyoruz.

    cursor.execute("INSERT INTO BoxOffice VALUES ('The Dark Knight', '1004')")
    cursor.execute("INSERT INTO BoxOffice VALUES ('Inception', '836')")
    cursor.execute("INSERT INTO BoxOffice VALUES ('Titanic', '2200')")

    connection.commit()

    # JOIN kullanarak birleştirelim. ( ON şartıyla isimleri aynı olanları)

    cursor.execute("""
        SELECT Movies.title, Movies.rating, BoxOffice.revenue_millions
        FROM Movies
        INNER JOIN BoxOffice ON Movies.title = BoxOffice.movie_title
""")
    
    joined_data = cursor.fetchall()
    
    for row in joined_data:
        print(f"Movie: {row[0]} \nRating: {row[1]} \nRevenue: ${row[2]} Millions")

    connection.close()

test_join()


#! SANAL DOSYA KAYDETME

# Eğer birleştirdiğimiz dosyayı kaydetmek istersek JOIN kullandığımız yerde SELECT öncesine şunun gibi bir kod yazmalıyız:

# CREATE VIEW IF NOT EXISTS Box_Office_Report AS