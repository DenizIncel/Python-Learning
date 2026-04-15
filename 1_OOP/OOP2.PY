# OOP 2

# Types of Methods: instance methods, class methods, and static methods.
# Metot Çeşitleri: normal metotlar, classmethod ve staticmethod.

# Instance method -> Belongs to the object (instance).       --> "Show information belonging to the student."
# Normal metot -> Nesneye bağlıdır.                          --> "Öğrenciye ait bilgi göster."
# Class method -> Belongs to the class itself.               --> "All students are in the same school, give school info."
# Class method -> Sınıfın kendisine bağlıdır.                --> "Tüm öğrenciler aynı okulda, okul bilgisi ver."
# Static method -> Related to the class but independent.     --> "Helper operations, e.g., taking the square, calculating percentages, etc."
# Static method -> Sınıfla ilgili ama bağımsızdır.           --> "Yardımcı işlemler örneğin: kare alma, yüzdelik hesaplama vs."

# INSTANCE METHOD / NORMAL METOT
class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number

    def show_info(self):  # Instance method / Normal metot
        print(f"Name: {self.name}\nNumber: {self.student_number}")

student1 = Student("Deniz", 101)
student1.show_info()


# CLASS METHOD
class Bicycle:
    bike_color = "Red"  # Class variable
    
    def __init__(self, name):
        self.name = name

    @classmethod
    def show_bike_info(cls):  # cls: the class itself / cls: class'ın kendisi
        print(f"The bicycle is {cls.bike_color}") # Bisiklet {cls.bsk_renk} renginde

Bicycle.show_bike_info()  # This bicycle is red


# STATIC METHOD
class Mathematics:
    @staticmethod
    def calculate_square(number):
        return number * number
    
print(Mathematics.calculate_square(5))