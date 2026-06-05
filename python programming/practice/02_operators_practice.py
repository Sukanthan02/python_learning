# ============================================================
# LESSON 02: Operators & Expressions
# ============================================================
# 🎯 Goal: Learn how to perform calculations and comparisons in Python

# ─────────────────────────────────────────────
# 1. ARITHMETIC OPERATORS — Math operations
# ─────────────────────────────────────────────

a = 10
b = 3

print(a + b)    # 13  → Addition
print(a - b)    # 7   → Subtraction
print(a * b)    # 30  → Multiplication
print(a / b)    # 3.333... → Division (always returns float)
print(a // b)   # 3   → Floor Division (no decimal, rounds down)
print(a % b)    # 1   → Modulus (remainder)
print(a ** b)   # 1000 → Exponentiation (10 to the power of 3)


# ─────────────────────────────────────────────
# 2. ASSIGNMENT OPERATORS — Update variables
# ─────────────────────────────────────────────

score = 100
score += 10     # same as: score = score + 10
print(score)    # 110

score -= 5      # same as: score = score - 5
print(score)    # 105

score *= 2      # same as: score = score * 2
print(score)    # 210

score //= 3     # same as: score = score // 3
print(score)    # 70

score **= 2     # same as: score = score ** 2
print(score)    # 4900


# ─────────────────────────────────────────────
# 3. COMPARISON OPERATORS — Compare values
# ─────────────────────────────────────────────
# Always return True or False (Boolean)

x = 5
y = 10

print(x == y)   # False → Equal to
print(x != y)   # True  → Not equal to
print(x < y)    # True  → Less than
print(x > y)    # False → Greater than
print(x <= 5)   # True  → Less than or equal
print(x >= 10)  # False → Greater than or equal


# ─────────────────────────────────────────────
# 4. LOGICAL OPERATORS — Combine conditions
# ─────────────────────────────────────────────

age = 20
has_id = True

# and → Both must be True
print(age >= 18 and has_id)     # True

# or  → At least one must be True
print(age >= 18 or has_id)      # True

# not → Reverses True/False
print(not has_id)               # False
print(not (age < 18))           # True


# ─────────────────────────────────────────────
# 5. IDENTITY OPERATORS — Check if same object
# ─────────────────────────────────────────────

a = [1, 2, 3]
b = a           # b points to SAME list as a
c = [1, 2, 3]  # c is a DIFFERENT list with same values

print(a is b)       # True  → Same object in memory
print(a is c)       # False → Different objects
print(a is not c)   # True


# ─────────────────────────────────────────────
# 6. MEMBERSHIP OPERATORS — Check if item in collection
# ─────────────────────────────────────────────

fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)        # True
print("grape" in fruits)        # False
print("mango" not in fruits)    # True

# Works on strings too!
message = "Hello Python"
print("Python" in message)      # True
print("Java" in message)        # False


# ─────────────────────────────────────────────
# 7. OPERATOR PRECEDENCE — Order of operations
# ─────────────────────────────────────────────
# Python follows BODMAS / PEMDAS rules
# Brackets → Exponent → Multiply/Divide → Add/Subtract

result = 2 + 3 * 4
print(result)           # 14 (NOT 20! Multiplication first)

result = (2 + 3) * 4
print(result)           # 20 (Brackets first)

result = 2 ** 3 + 1
print(result)           # 9  (Exponent first: 8 + 1)


# ─────────────────────────────────────────────
# 8. PRACTICAL EXAMPLE — BMI Calculator
# ─────────────────────────────────────────────

weight_kg = 70      # weight in kilograms
height_m = 1.75     # height in meters

bmi = weight_kg / (height_m ** 2)
print(f"BMI: {bmi:.2f}")  # .2f → round to 2 decimal places

# Check category using comparison
print(bmi < 18.5)   # Underweight
print(18.5 <= bmi < 24.9)  # Normal weight
print(bmi >= 25.0)  # Overweight


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Calculate the area of a circle: area = π * r²
#    Use r = 7 and π = 3.14159. Print the result.

# 2. A store gives 20% discount on a product worth 500.
#    Calculate the final price using operators.

# 3. Check if the number 17 is odd using the % operator.
#    Print: "17 is odd: True/False"

# 4. You have age = 17. Check if someone can:
#    a) Vote: age >= 18
#    b) Drive (with parent): age >= 16
#    c) Both vote AND drive: use 'and'

# YOUR CODE HERE:
