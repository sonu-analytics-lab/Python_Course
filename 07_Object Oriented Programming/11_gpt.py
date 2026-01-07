# Class & Object

from abc import ABC, abstractmethod


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def Display(self):
        print(self.name, self.roll_no)


s1 = Student("Amit", 11)
s1.Display()


# 2️⃣
print("Class Variable vs Instance Variable")


class School:
    school_name = "ABC School"

    def __init__(self, student):
        self.student = student


s1 = School("Rahul")
s2 = School("Neha")

print(s1.school_name, s1.student)
print(s2.school_name, s2.student)


# 3️⃣
print("Method Inside Class")


class car:
    def drive(self):
        print("Car is driving")


a = car()
a.drive()


# 4️⃣

print("Constructor Example.........................................")


class Book():

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print(self.title, self.author)


a = Book("Python", "Guido")
a.show()

# 5️⃣
print("Inheritance.........................................")


class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


d = Dog()
d.sound()


#
print("6️⃣ Method Overriding....................................")


class Parent:

    def child(self):
        print("Parent Class")


class Child(Parent):

    def show(self):
        print("Child Class")


c = Child()
c.show()


#
print("7️⃣ Encapsulation....................................")


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, Amount):
        self.__balance += Amount

    def show_balance(self):
        print("Balance", self.__balance)


acc = BankAccount()
acc.deposit(5000)
acc.show_balance()


print("8️⃣ Polymorphism....................................")


class Bird:
    def fly(self):
        print("Some birds fly")


class Sparrow:
    def fly(self):
        print("Sparrow flies")


class Ostrich:
    def fly(self):
        print("Ostrich cannot fly")


for bird in (Sparrow(), Ostrich()):
    bird.fly()


print("9️⃣ super() Keyword")


class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id


e = Employee("Ravi", 201)
print(e.name, e.emp_id)


print("🔟 Abstraction")


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area:", self.side * self.side)


s = Square(4)
s.area()


print("1️⃣1️⃣ Multiple Inheritance")


class Father:
    def skill(self):
        print("Driving")


class Mother:
    def skill(self):
        print("Cooking")


class Child1(Father, Mother):
    pass


c = Child1()
c.skill()


print("1️⃣2️⃣ MRO")

print(Child1.__mro__)

print("1️⃣3️⃣ Magic Method __str__")


class Student1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


s = Student1("Ankit")
print(s)

# 🔥 REAL-LIFE PROGRAMS (INTERVIEW FAVORITE)
print("1️⃣4️⃣ Library Management (Mini)")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for b in self.books:
            print(b)


lib = Library()
lib.add_book("Python")
lib.add_book("Java")
lib.show_books()


print("1️⃣5️⃣ ATM Program (Encapsulation)")


class ATM:
    def __init__(self):
        self.__balance = 10000

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.__balance)


atm = ATM()
atm.withdraw(2000)
atm.check_balance()
