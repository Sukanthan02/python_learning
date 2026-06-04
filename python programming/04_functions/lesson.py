# ============================================================
# LESSON 04: Functions
# ============================================================
# 🎯 Goal: Write reusable blocks of code

# ─────────────────────────────────────────────
# 1. DEFINING A FUNCTION — basic syntax
# ─────────────────────────────────────────────

def greet():
    """This function prints a greeting."""
    print("Hello! Welcome to Python!")

# Call the function
greet()


# ─────────────────────────────────────────────
# 2. PARAMETERS — pass data into a function
# ─────────────────────────────────────────────

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Sukanthan")
greet_user("Alice")

# Multiple parameters
def introduce(name, age, city):
    print(f"I am {name}, {age} years old, from {city}.")

introduce("Bob", 30, "Chennai")


# ─────────────────────────────────────────────
# 3. RETURN — send a value back from a function
# ─────────────────────────────────────────────

def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([3, 1, 9, 5, 2])
print(f"Min: {minimum}, Max: {maximum}")


# ─────────────────────────────────────────────
# 4. DEFAULT PARAMETERS — optional arguments
# ─────────────────────────────────────────────

def greet(name, message="Good Morning"):
    print(f"{message}, {name}!")

greet("Alice")                      # Uses default "Good Morning"
greet("Bob", "Good Evening")       # Overrides default


# ─────────────────────────────────────────────
# 5. KEYWORD ARGUMENTS — pass by name
# ─────────────────────────────────────────────

def create_profile(name, age, role):
    print(f"Name: {name}, Age: {age}, Role: {role}")

# Order doesn't matter when using keyword args!
create_profile(role="Developer", name="Sukanthan", age=25)


# ─────────────────────────────────────────────
# 6. *args — variable number of arguments
# ─────────────────────────────────────────────
# *args collects extra positional arguments into a TUPLE

def total_price(*prices):
    total = sum(prices)
    print(f"Total: ₹{total}")

total_price(100, 250, 75)           # 3 arguments
total_price(500, 200, 150, 80, 70) # 5 arguments


# ─────────────────────────────────────────────
# 7. **kwargs — variable number of keyword arguments
# ─────────────────────────────────────────────
# **kwargs collects extra keyword arguments into a DICT

def display_info(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

print("User Info:")
display_info(name="Alice", age=28, city="Mumbai", role="Backend Dev")


# ─────────────────────────────────────────────
# 8. LAMBDA FUNCTION — anonymous one-line functions
# ─────────────────────────────────────────────

# Regular function
def square(x):
    return x ** 2

# Same thing as lambda
square_lambda = lambda x: x ** 2

print(square(5))         # 25
print(square_lambda(5))  # 25

# Lambda is great for sorting
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students.sort(key=lambda student: student[1], reverse=True)
print("\nTop students:", students)

# Lambda with multiple params
multiply = lambda a, b: a * b
print(multiply(4, 7))    # 28


# ─────────────────────────────────────────────
# 9. SCOPE — Where variables live
# ─────────────────────────────────────────────

global_var = "I am global"   # Can be accessed anywhere

def my_function():
    local_var = "I am local"     # Only inside this function
    print(global_var)            # Can access global
    print(local_var)

my_function()
print(global_var)               # Works!
# print(local_var)              # ❌ ERROR: local_var not defined here


# Using global keyword (use sparingly!)
counter = 0

def increment():
    global counter    # Tell Python we want the GLOBAL counter
    counter += 1

increment()
increment()
print(f"Counter: {counter}")   # 2


# ─────────────────────────────────────────────
# 10. DOCSTRINGS — document your functions
# ─────────────────────────────────────────────

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The area of the rectangle.
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

area = calculate_area(5, 3)
print(f"Area: {area}")

# View the docstring
print(calculate_area.__doc__)


# ─────────────────────────────────────────────
# 11. PRACTICAL EXAMPLE — Mini Calculator
# ─────────────────────────────────────────────

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator(a, operator, b):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    
    if operator not in operations:
        return "Unknown operator!"
    
    return operations[operator](a, b)

# Test the calculator
print(calculator(10, "+", 5))    # 15
print(calculator(10, "-", 3))    # 7
print(calculator(6, "*", 7))     # 42
print(calculator(10, "/", 0))    # Error message
print(calculator(15, "/", 3))    # 5.0


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Write a function `is_even(number)` that returns True if even, False if odd.

# 2. Write a function `celsius_to_fahrenheit(c)`:
#    Formula: F = (C × 9/5) + 32

# 3. Write a function `count_vowels(text)` that counts vowels (a,e,i,o,u).
#    Example: count_vowels("Hello World") → 3

# 4. Write a function `factorial(n)` that calculates n! = n × (n-1) × ... × 1
#    Example: factorial(5) = 120

# 5. Write a function `*args` version: `average(*numbers)` 
#    that returns the average of any number of values.

# YOUR CODE HERE:
