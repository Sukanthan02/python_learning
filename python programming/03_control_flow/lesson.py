# ============================================================
# LESSON 03: Control Flow — if/elif/else & Loops
# ============================================================
# 🎯 Goal: Make decisions and repeat actions in Python

# ─────────────────────────────────────────────
# 1. IF STATEMENT — Make decisions
# ─────────────────────────────────────────────

age = 20

if age >= 18:
    print("You are an adult.")    # This runs if condition is True

# ─────────────────────────────────────────────
# 2. IF / ELSE — Two paths
# ─────────────────────────────────────────────

temperature = 35

if temperature > 30:
    print("It's hot outside! ☀️")
else:
    print("The weather is nice. 🌤️")


# ─────────────────────────────────────────────
# 3. IF / ELIF / ELSE — Multiple conditions
# ─────────────────────────────────────────────

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")


# ─────────────────────────────────────────────
# 4. NESTED IF — if inside if
# ─────────────────────────────────────────────

is_logged_in = True
is_admin = False

if is_logged_in:
    print("Welcome back!")
    if is_admin:
        print("Admin panel is accessible.")
    else:
        print("You have standard access.")
else:
    print("Please log in first.")


# ─────────────────────────────────────────────
# 5. TERNARY OPERATOR — One-line if/else
# ─────────────────────────────────────────────

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# More examples
number = -5
abs_value = number if number >= 0 else -number
print(f"Absolute value: {abs_value}")


# ─────────────────────────────────────────────
# 6. FOR LOOP — Repeat for each item
# ─────────────────────────────────────────────

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Loop through a range of numbers
print("\nCounting 1 to 5:")
for i in range(1, 6):       # range(start, stop) — stop is NOT included
    print(i)

# range with step
print("\nEven numbers 0 to 10:")
for i in range(0, 11, 2):   # range(start, stop, step)
    print(i)

# Loop through a string
word = "Python"
print("\nLetters in Python:")
for letter in word:
    print(letter)


# ─────────────────────────────────────────────
# 7. WHILE LOOP — Repeat while condition is True
# ─────────────────────────────────────────────

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1    # IMPORTANT: Always change the variable to avoid infinite loop!

# While with user input (uncomment to test):
# password = ""
# while password != "secret123":
#     password = input("Enter password: ")
# print("Access granted!")


# ─────────────────────────────────────────────
# 8. BREAK — Exit a loop early
# ─────────────────────────────────────────────

print("\nSearching for 'banana':")
fruits = ["apple", "mango", "banana", "cherry", "grape"]

for fruit in fruits:
    if fruit == "banana":
        print(f"Found it: {fruit}!")
        break    # Stop the loop immediately
    print(f"Not this one: {fruit}")


# ─────────────────────────────────────────────
# 9. CONTINUE — Skip current iteration
# ─────────────────────────────────────────────

print("\nSkipping even numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        continue    # Skip even numbers, go to next iteration
    print(i)        # Only odd numbers will print


# ─────────────────────────────────────────────
# 10. PASS — Placeholder (do nothing)
# ─────────────────────────────────────────────

for i in range(5):
    if i == 3:
        pass    # TODO: handle this case later
    else:
        print(i)


# ─────────────────────────────────────────────
# 11. ENUMERATE — Loop with index
# ─────────────────────────────────────────────

students = ["Alice", "Bob", "Charlie", "Diana"]

print("\nStudent List:")
for index, name in enumerate(students, start=1):
    print(f"{index}. {name}")


# ─────────────────────────────────────────────
# 12. NESTED LOOPS — Loop inside a loop
# ─────────────────────────────────────────────

print("\nMultiplication Table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")


# ─────────────────────────────────────────────
# 13. PRACTICAL EXAMPLE — Number guessing game
# ─────────────────────────────────────────────

import random

secret = random.randint(1, 10)
print("\n🎮 Guess the number (1-10)!")
print(f"(For demo, secret is: {secret})")

attempts = 0
for attempt in range(3):   # Give 3 attempts
    guess = secret          # In real game: int(input("Your guess: "))
    attempts += 1
    
    if guess == secret:
        print(f"✅ Correct! Got it in {attempts} attempt(s)!")
        break
    elif guess < secret:
        print("Too low! ⬆️")
    else:
        print("Too high! ⬇️")
else:
    print(f"❌ Game over! The number was {secret}")


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Print a triangle pattern using nested loops:
#    *
#    **
#    ***
#    ****
#    *****

# 2. Use a for loop to sum all numbers from 1 to 100.
#    Print: "Sum of 1 to 100 = 5050"

# 3. Write code that checks if a number is positive, negative, or zero.
#    Test with: -5, 0, 8

# 4. Use a while loop to count down from 10 to 1,
#    then print "Blast off! 🚀"

# 5. Loop through this list and print only strings (not numbers):
#    data = ["hello", 42, "world", 3.14, "python", True]
#    Hint: use type() to check

# YOUR CODE HERE:
