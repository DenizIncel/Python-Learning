# ERROR HANDLING AND EXCEPTIONS
# Hata Yönetimi ve İstisnalar (Exceptions)

#*      try / except -> catch the error / hatayı yakala
#!      except ErrorType -> catch only a specific error / sadece belli hatayı yakala
#?      finally -> run in all cases / her durumda çalış
#TODO   raise -> throw an error yourself / kendin hata fırlat
#!      custom exception -> write your own error type / kendi hata türünü yaz


# When an error occurs in Python, the program stops, but in large projects this is unacceptable.
# Python’da hata olunca program durur ama büyük projelerde bu kabul edilemez.
# The try / except structure is used for this.
# Bunun için try / except yapısı var.

#? Basic try/except
#? Basit try/except

try:
    number = int("abc")  # error: string cannot be converted to int
except:
    print("An error occurred") # Bir hata olustu

# Normally the program would crash, but since 'except' catches it, it continues.
# Normalde program kırılırdı ama except yakaladığı için devam eder.



#! Specifying the Error Type
#! Hata Türünü Belirtmek

# Every error has a type (ValueError, ZeroDivisionError, FileNotFoundError, etc.).
# Her hatanın bir türü vardır (ValueError, ZeroDivisionError, FileNotFoundError vs.).

try:
    x = 10 / 0
except ZeroDivisionError:        # runs only for this error / sadece bu hata için çalışır.
    print("Division by zero error") # Sifira bolme hatasi



#* finally

try:
    file = open("file.txt")
except FileNotFoundError:
    print("File not found") # Dosya bulunamadi
finally:                    # runs even if there is an error / hata olsa da çalışır
    print("Process finished") # Islem bitti

 
 
#? raise

# Kendi hatanı oluşturabilirsin (fırlatabilirsin).
# If you are writing a library, API, or a large program, you can throw a custom error message for the user to understand.
# Kütüphane, API ya da büyük program yazıyorsan, kullanıcının anlaması için özel hata mesajı fırlatabilirsin.


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisor cannot be zero!") # Bolen sifir olamaz!
    return a / b

print(divide(10, 2)) # Output: 5.0
# print(divide(5, 0)) # Throws an error / Hata fırlatır.




#! Custom Exception Class
#! Özel Exception Sınıfı

# You can define your own error type.
# Kendi hata tipini tanımlayabilirsin.

class NegativeNumberError(Exception):
    pass

def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate the square root of a negative number!") # Negatif sayının karekökü alınamaz!
    return number ** 0.5

print(calculate_square_root(9))   # Output: 3.0
# print(calculate_square_root(-4)) # Error