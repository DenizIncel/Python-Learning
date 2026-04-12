# Object-Oriented Programming (OOP)
# OOP (Nesne Tabanlı Programlama)

# Creating a class
# Sınıf (Class) oluşturma
class Car:
    pass

# Creating an object (Instantiation)
# Nesne (Object) oluşturma
car1 = Car()  # Created an object from the Car class. / Car sınıfından bir nesne oluşturduk.
car2 = Car()

# Adding attributes dynamically
# Özellik (Attribute) ekleme
car1.brand = "Toyota"
car1.color = "Red"
print(car1.brand + " " + car1.color)
# But this method is messy. Instead, we use a constructor method in the class.
# Ama bu yöntem dağınık olur. Bunun yerine sınıfa kurucu metot (constructor) koyarız.


# Constructor (__init__): Initializes the object. It's a special method that runs automatically when an object is created.
# Yapıcı (Constructor) __init__: Nesne kurulumunu yapar. Nesne oluşturulduğunda otomatik çalışan özel metottur.
class CarV2:
    # self: The first parameter of every class method must be self. It refers to the object itself.
    # self: Her sınıf metodunun ilk parametresi self olmalıdır. Bu, nesnenin kendisi anlamına gelir.
    def __init__(self, brand, color):  
        self.brand = brand  # Assigning the brand to this specific car / Bu arabaya ait marka demiş oluyoruz
        self.color = color


# class: Kimlik tasarım şablonu
# __init__: İsim, numara gibi bilgilerin yazıldığı aşamadır.
# self: "Bu kimlik kime ait?" sorusunun cevabıdır.

car3 = CarV2("BMW", "White")
car4 = CarV2("Mercedes", "Black")

print(car3.brand, car3.color)