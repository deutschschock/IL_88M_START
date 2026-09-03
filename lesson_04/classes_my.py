class Fruit:
    def __init__(self, name, weight ):
        self.name = name
        self.weight = weight

fruit1 = Fruit("apple", 5)
fruit2 = Fruit("banana", 4)
print(fruit1)
print(fruit1.name)


class Fruit:
    def __init__(self, name, day_ripe ):
        self.name = name
        self.day_ripe = day_ripe

    def describe(self):
        print(f'This is a {name}')

    def wait_a_day(self):
        self.day_ripe -= 1
        print(f"{self.name} day ripe: {self.day_ripe}")

    def is_ripe(self):
        return self.day_ripe <=0

class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return Circle.pi * self.radius**2
    def perimeter(self):
        return 2 * Circle.pi * Circle.radius

c1 = Circle(2)
print(c1.area())

print(Circle.pi)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise print("Invalid amount error.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Invalid amount error.")
        else:
            self.__balance -= amount
        print(f"Withdraw {amount}. Balance:  {self.__balance}")



account = BankAccount("John", 100)
print(account)
account.deposit(100)
account.withdraw(10)

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f'{self.name} is eating')
    def makeSound(self ):
        print(f'{self.name} is making sound')

class Dog(Animal):
    def makeSound(self ):
        print(f'{self.name} is making sound: Gauuu!')
    def jump(self   ):
        print("jumps")

class Cat(Dog):
    def makeSound(self ):
        print(f'{self.name} is making sound: Meau!')
    def jump(self   ):
        print("not jumps")

cat1 = Cat("John")
cat1.eat()
cat1.makeSound()
cat1.jump()

dog1 = Dog('Farik')
dog1.eat()
dog1.makeSound()
dog1.jump()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    def __str__(self):
        return (f"Name: {self.name}, " 
        f"Age: {self.age}, Marks: {self.marks}")

student = Student("John", 25, 100)
print(student)

class Thermometer:
    def __init__(self):
        self.__temperature = -273

        def set_temperature(self, t):
            if t > -273:
                self.__temperature = t
            else:
                print("Invalid temperature error.")

        def get_temperature(self):
            return self.__temperature

term = Thermometer()
term.temperature = 10
print(term.temperature)
