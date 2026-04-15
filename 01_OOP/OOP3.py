# INHERITANCE
# MİRAS ALMA (INHERITANCE)

# Common features are kept in the parent class, while only the differences are written in the child class. This provides great convenience.
# Ortak özellikleri üst sınıfta tutarken alt sınıfa sadece farkları yazılır. Bu da çok fazla kolaylık sağlar.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Sound of an animal...") # Bir hayvanin sesi...


class Cat(Animal):
    def make_sound(self): # override
        # Fixed: using self.name instead of global variable 'kedi'
        # Düzeltme: global 'kedi' değişkeni yerine self.name kullanıldı
        print(f"{self.name}: Meow!") # Miyav!

class Dog(Animal):
    def make_sound(self):
        # Fixed: using self.name instead of global variable 'kopek'
        # Düzeltme: global 'kopek' değişkeni yerine self.name kullanıldı
        print(f"{self.name}: Woof woof!") # Hav hav!


rabbit = Animal("Den")
rabbit.make_sound()

cat = Cat("Maya")
dog = Dog("Einstein")

cat.make_sound()
dog.make_sound()


# POLYMORPHISM
# POLİMORFİZM (ÇOK BİÇİMLİLİK)

class Shape:
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius


shapes = [Square(4), Circle(3)]

for shape in shapes:
    print(shape.calculate_area())


# KAPSÜLLEME (ENCAPSULATION)

# It encapsulates the "insides" of the object and only exposes them through permitted methods.
# Nesnenin "içini" kapsülleyip sadece izin verilen yöntemlerle dışarı açar.
# There are no strict rules like (private, public, protected) in languages like C#. But there are naming conventions:
# C# dilindeki gibi (private, public, protected) katı kurallar yok. Ama isimlendirme kuralları var:

# Public: Accessible from anywhere
# Public: her yerden erişilebilir
class Student1:
    def __init__(self, name, student_number):
        self.name = name # public
        self.student_number = student_number # public

# Protected: Starts with a single underscore (_). Should not be accessed from the outside unless permitted.
# Protected: _ ile başlar. Dışardan izin verilmedikçe erişilemez.
class Student2:
    def __init__(self, x, y):
        self._grade = 85 # protected / _not

# Private: Starts with double underscores (__). Python hides it by changing the variable name (name mangling).
# Private: __ ile başlar. Python değişken adını değiştirerek gizler.
class Student3:
    def __init__(self, a, b):
        self.__national_id = "12345678910" # private / __tc (TC Kimlik)


# Get and Set Methods: Used to access special/private fields.
# Get ve Set Metotları: Özel alanlara erişmek için kullanılır.

class Student4:
    def __init__ (self, name, student_number):
        self.name = name
        self.__student_number = student_number

    def get_student_number(self):
        return self.__student_number
        
    def set_student_number(self, new_number):
         # Off-topic: You can ask if the variable is of this type using isinstance.
         # Konu dışı: isinstance ile değişkenin türü bu mu diye sorabilirsin.
         if isinstance(new_number, int):  
            self.__student_number = new_number
         else:
             print("The number can only be an integer.") # Numara sadece sayi olabilir.


student4 = Student4("Ali", 105)
print(student4.get_student_number())  # Output: 105

student4.set_student_number(205)
print(student4.get_student_number()) # Output: 205