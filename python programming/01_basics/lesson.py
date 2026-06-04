# ============================================================
# LESSON 01: Python Basics — Variables, Data Types, Input/Output
# ============================================================
# 🎯 Goal: Understand how Python stores and displays data

# ─────────────────────────────────────────────
# 1. PRINT — Displaying output
# ─────────────────────────────────────────────

print("Hello, World!")          # Print text (string)
print(42)                        # Print a number
print(3.14)                      # Print a decimal number
print(True)                      # Print a boolean
print("Hello", "Python", "!")   # Print multiple values


# ─────────────────────────────────────────────
# 2. VARIABLES — Storing data
# ─────────────────────────────────────────────
# Variables hold values. No need to declare a type!

name = "Sukanthan"       # String (text)
age = 25                 # Integer (whole number)
height = 5.9             # Float (decimal number)
is_student = True        # Boolean (True or False)

print(name)
print(age)
print(height)
print(is_student)


# ─────────────────────────────────────────────
# 3. DATA TYPES — Types of values in Python
# ─────────────────────────────────────────────

# int   → whole numbers
x = 10
print(type(x))           # <class 'int'>

# float → decimal numbers
y = 3.14
print(type(y))           # <class 'float'>

# str   → text (always in quotes)
greeting = "Hello"
print(type(greeting))    # <class 'str'>

# bool  → True or False
is_active = True
print(type(is_active))   # <class 'bool'>

# NoneType → represents "nothing" / empty
nothing = None
print(type(nothing))     # <class 'NoneType'>


# ─────────────────────────────────────────────
# 4. TYPE CONVERSION — Changing data types
# ─────────────────────────────────────────────

# Convert string to integer
num_str = "100"
num_int = int(num_str)
print(num_int + 5)       # 105

# Convert integer to string
age = 25
message = "I am " + str(age) + " years old."
print(message)

# Convert integer to float
price = float(10)
print(price)             # 10.0

# Convert float to integer (cuts off decimal)
pi = 3.99
print(int(pi))           # 3


# ─────────────────────────────────────────────
# 5. INPUT — Getting data from the user
# ─────────────────────────────────────────────
# input() always returns a STRING

# Uncomment below lines to test interactively:
# user_name = input("What is your name? ")
# user_age = int(input("How old are you? "))
# print(f"Hello, {user_name}! You are {user_age} years old.")


# ─────────────────────────────────────────────
# 6. F-STRINGS — Clean way to format output
# ─────────────────────────────────────────────
# Use f"..." and put variables inside {}

name = "Sukanthan"
age = 25
city = "Chennai"

# Old way (messy)
print("My name is " + name + " and I am " + str(age) + " years old.")

# Modern way with f-strings (clean ✅)
print(f"My name is {name} and I am {age} years old.")
print(f"I live in {city}.")
print(f"Next year I will be {age + 1} years old.")


# ─────────────────────────────────────────────
# 7. MULTIPLE ASSIGNMENT
# ─────────────────────────────────────────────

# Assign multiple variables on one line
a, b, c = 1, 2, 3
print(a, b, c)           # 1 2 3

# Assign same value to multiple variables
x = y = z = 0
print(x, y, z)           # 0 0 0


# ─────────────────────────────────────────────
# 8. COMMENTS — Notes in your code
# ─────────────────────────────────────────────

# This is a single-line comment (Python ignores this)

"""
This is a multi-line comment (called a docstring).
You can write multiple lines here.
Python ignores this too.
"""

print("Comments don't affect the output!")


# ============================================================
# ✏️  EXERCISES — Practice yourself!
# ============================================================
# 1. Create a variable called `country` and set it to your country name.
#    Print it using an f-string: "I am from {country}"

# 2. Create two variables: price = 49.99 and quantity = 3
#    Calculate the total cost and print: "Total cost: {total}"

# 3. Convert the string "2024" to an integer, add 10, and print the result.

# 4. Use input() to ask the user for their favorite color.
#    Print: "Your favorite color is {color}"
#    (Hint: Uncomment and write your code below)

# YOUR CODE HERE:
