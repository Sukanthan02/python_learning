# ============================================================
# LESSON 09: Object-Oriented Programming (OOP)
# ============================================================
# 🎯 Goal: Model real-world things using Classes & Objects

# ─────────────────────────────────────────────
# 1. WHAT IS OOP?
# ─────────────────────────────────────────────
# A CLASS is a blueprint. An OBJECT is an instance of that blueprint.
# Example: Car (class) → my_honda, your_toyota (objects)

# ─────────────────────────────────────────────
# 2. DEFINING A CLASS
# ─────────────────────────────────────────────

class Dog:
    """A simple Dog class."""
    
    # Class variable — shared by ALL instances
    species = "Canis familiaris"
    
    # __init__ — constructor, called when creating an object
    def __init__(self, name, breed, age):
        # Instance variables — unique to each object
        self.name = name
        self.breed = breed
        self.age = age
    
    # Instance method
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def describe(self):
        print(f"{self.name} is a {self.age}-year-old {self.breed}.")
    
    # __str__ — called when you print(object)
    def __str__(self):
        return f"Dog({self.name}, {self.breed}, {self.age}yrs)"


# Create objects (instances)
dog1 = Dog("Rex", "German Shepherd", 3)
dog2 = Dog("Bella", "Golden Retriever", 5)

dog1.bark()
dog2.describe()
print(dog1)              # calls __str__
print(dog1.species)      # class variable
print(dog2.species)      # same class variable


# ─────────────────────────────────────────────
# 3. REALISTIC EXAMPLE — BankAccount
# ─────────────────────────────────────────────

class BankAccount:
    """A bank account class."""
    
    bank_name = "Python National Bank"
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance    # _ prefix = "private by convention"
        self.transactions = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self._balance += amount
        self.transactions.append(f"+{amount}")
        print(f"  ✅ Deposited ₹{amount}. Balance: ₹{self._balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive!")
        if amount > self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount
        self.transactions.append(f"-{amount}")
        print(f"  💸 Withdrew ₹{amount}. Balance: ₹{self._balance}")
    
    def get_balance(self):
        return self._balance
    
    def get_statement(self):
        print(f"\n  📄 Statement for {self.owner}:")
        for t in self.transactions:
            print(f"     {t}")
        print(f"     Current balance: ₹{self._balance}")
    
    def __str__(self):
        return f"Account({self.owner}, ₹{self._balance})"


print("\nBank Account Demo:")
account = BankAccount("Sukanthan", 5000)
account.deposit(1500)
account.withdraw(800)
account.deposit(3000)
account.get_statement()
print(f"\n  {account}")


# ─────────────────────────────────────────────
# 4. INHERITANCE — Child class inherits from Parent
# ─────────────────────────────────────────────

class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print(f"{self.name} says: {self.sound}!")
    
    def __str__(self):
        return f"{type(self).__name__}({self.name})"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # Call parent __init__
        self.breed = breed
    
    def fetch(self, item):
        print(f"{self.name} fetches the {item}!")


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor
    
    def purr(self):
        location = "indoor" if self.indoor else "outdoor"
        print(f"{self.name} is a happy {location} cat. Purrr...")


class Parrot(Animal):
    def __init__(self, name, phrase):
        super().__init__(name, phrase)
    
    def speak(self):
        # Override parent method
        print(f"{self.name} says: '{self.sound}! {self.sound}!'")


print("\nInheritance Demo:")
rex = Dog("Rex", "German Shepherd")
whiskers = Cat("Whiskers", indoor=True)
polly = Parrot("Polly", "Pretty bird")

animals = [rex, whiskers, polly]
for animal in animals:
    animal.speak()    # Polymorphism! Each calls own speak()

rex.fetch("ball")
whiskers.purr()


# ─────────────────────────────────────────────
# 5. ENCAPSULATION — Hide internal data
# ─────────────────────────────────────────────

class Person:
    def __init__(self, name, age):
        self._name = name         # Protected (by convention)
        self.__age = age          # Private (name-mangled)
    
    @property
    def name(self):
        """Getter for name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name — with validation."""
        if not isinstance(value, str) or len(value) < 2:
            raise ValueError("Name must be a string of at least 2 chars.")
        self._name = value.title()
    
    @property
    def age(self):
        """Getter for age."""
        return self.__age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.__age = value
    
    def __str__(self):
        return f"Person({self._name}, {self.__age})"


print("\nEncapsulation Demo:")
person = Person("sukanthan", 25)
print(person)              # Person(Sukanthan, 25)

person.name = "alice"      # Uses setter (auto title-cases)
print(person.name)         # Alice

try:
    person.age = -5        # Triggers ValueError in setter
except ValueError as e:
    print(f"  ❌ {e}")

person.age = 30
print(person)


# ─────────────────────────────────────────────
# 6. CLASS METHODS & STATIC METHODS
# ─────────────────────────────────────────────

class Temperature:
    
    def __init__(self, celsius):
        self.celsius = celsius
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Alternative constructor — create from Fahrenheit."""
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
    @staticmethod
    def is_freezing(celsius):
        """Utility function — doesn't need self or cls."""
        return celsius <= 0
    
    def __str__(self):
        return f"{self.celsius:.1f}°C / {self.fahrenheit:.1f}°F"


print("\nTemperature Demo:")
t1 = Temperature(100)          # Normal constructor
t2 = Temperature.from_fahrenheit(212)   # Class method constructor
print(t1)
print(t2)
print(Temperature.is_freezing(-5))    # True
print(Temperature.is_freezing(20))    # False


# ─────────────────────────────────────────────
# 7. DUNDER / MAGIC METHODS
# ─────────────────────────────────────────────

class Vector:
    """A 2D vector class demonstrating magic methods."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


print("\nVector Math:")
v1 = Vector(2, 3)
v2 = Vector(1, 4)
print(v1 + v2)       # Vector(3, 7)
print(v1 - v2)       # Vector(1, -1)
print(v1 * 3)        # Vector(6, 9)
print(len(v1))       # magnitude ≈ 3
print(v1 == Vector(2, 3))  # True


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Create a class Rectangle with width and height.
#    Methods: area(), perimeter(), is_square()
#    Use @property for area and perimeter.

# 2. Create a class hierarchy:
#    Shape (base) → Circle, Rectangle, Triangle
#    Each shape: area(), perimeter(), __str__()

# 3. Create a class Stack (data structure):
#    Methods: push(item), pop(), peek(), is_empty(), size()

# 4. Create a class Employee:
#    Attributes: name, salary, department
#    Methods: give_raise(percent), get_annual_salary()
#    Create class Manager(Employee) that can manage a team list.

# YOUR CODE HERE:
