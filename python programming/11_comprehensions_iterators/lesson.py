# ============================================================
# LESSON 11: Comprehensions & Iterators
# ============================================================
# 🎯 Goal: Write elegant, efficient Python using comprehensions

# ─────────────────────────────────────────────
# 1. LIST COMPREHENSION — Build lists elegantly
# ─────────────────────────────────────────────

# Traditional way
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print("Traditional:", squares)

# List comprehension — same thing in 1 line!
squares = [i ** 2 for i in range(1, 11)]
print("Comprehension:", squares)

# Syntax: [expression for item in iterable]
#         [expression for item in iterable if condition]

# With condition (filter)
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print("Even squares:", even_squares)

# From another list
fruits = ["apple", "banana", "cherry", "avocado", "apricot"]
a_fruits = [f.upper() for f in fruits if f.startswith("a")]
print("A-fruits uppercase:", a_fruits)

# With complex expression
words = ["hello", "WORLD", "Python", "CODE"]
normalized = [w.lower().strip() for w in words]
print("Normalized:", normalized)

# Nested list comprehension — create a 3x3 matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:", matrix)

# Flatten a nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in nested for x in row]
print("Flattened:", flat)


# ─────────────────────────────────────────────
# 2. DICTIONARY COMPREHENSION
# ─────────────────────────────────────────────

# Build a dict from a range
squares_dict = {i: i**2 for i in range(1, 6)}
print("\nSquares dict:", squares_dict)

# Transform an existing dict
prices = {"apple": 0.5, "banana": 0.3, "cherry": 1.2}
# Add 10% tax
with_tax = {item: round(price * 1.1, 2) for item, price in prices.items()}
print("With tax:", with_tax)

# Filter dict — only expensive items
expensive = {k: v for k, v in prices.items() if v > 0.4}
print("Expensive:", expensive)

# Invert a dict (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print("Inverted:", inverted)

# From two lists using zip
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
student_scores = {name: score for name, score in zip(names, scores)}
print("Student scores:", student_scores)


# ─────────────────────────────────────────────
# 3. SET COMPREHENSION
# ─────────────────────────────────────────────

# Unique lengths of words
words = ["hello", "world", "hi", "python", "code", "hi"]
unique_lengths = {len(w) for w in words}
print("\nUnique lengths:", unique_lengths)

# Unique even numbers
numbers = [1, 2, 3, 4, 5, 2, 4, 6, 3]
unique_evens = {n for n in numbers if n % 2 == 0}
print("Unique evens:", unique_evens)


# ─────────────────────────────────────────────
# 4. GENERATOR EXPRESSIONS — Memory efficient!
# ─────────────────────────────────────────────
# Like list comprehensions but with () instead of []
# They don't build the entire list in memory — generate one at a time

# List comp → creates full list in memory
squares_list = [x**2 for x in range(1_000_000)]    # uses lots of RAM

# Generator → generates values one at a time (much more efficient!)
squares_gen = (x**2 for x in range(1_000_000))     # uses tiny RAM

# Consume the generator
print("\nFirst 5 generator values:")
for i, val in enumerate(squares_gen):
    if i >= 5:
        break
    print(f"  {val}")

# Great for sum, max, min, etc.
total = sum(x**2 for x in range(1001))
print(f"Sum of squares 1-1000: {total}")


# ─────────────────────────────────────────────
# 5. GENERATORS — yield keyword
# ─────────────────────────────────────────────

def count_up(start, end, step=1):
    """A generator function using yield."""
    current = start
    while current <= end:
        yield current          # Pause and return value
        current += step       # Resume from here next time

# Use the generator
counter = count_up(1, 10)
print("\nGenerator output:")
for num in counter:
    print(num, end=" ")
print()

# Fibonacci generator
def fibonacci():
    """Infinite Fibonacci sequence generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take first 10 Fibonacci numbers
fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print("First 10 Fibonacci:", first_10)


# ─────────────────────────────────────────────
# 6. ITERATORS — iter() and next()
# ─────────────────────────────────────────────

# Any iterable can be turned into an iterator
fruits = ["apple", "banana", "cherry"]
iterator = iter(fruits)

print("\nManual iteration:")
print(next(iterator))    # apple
print(next(iterator))    # banana
print(next(iterator))    # cherry
# print(next(iterator))  ← StopIteration error!

# for loop uses iterators internally!
# for x in fruits: is equivalent to:
# it = iter(fruits)
# while True:
#     try: x = next(it)
#     except StopIteration: break
#     # loop body


# ─────────────────────────────────────────────
# 7. USEFUL BUILT-IN ITERATION TOOLS
# ─────────────────────────────────────────────

# zip — iterate multiple lists together
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
cities = ["Chennai", "Mumbai", "Delhi"]

for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}, {city}")

# enumerate — iterate with index
print("\nIndexed:")
for i, name in enumerate(names, start=1):
    print(f"  {i}. {name}")

# map — apply function to each item
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("\nDoubled:", doubled)

squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter — keep items that match condition
even = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print("Evens:", even)

# sorted with key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print("\nTop students:")
for rank, (name, score) in enumerate(by_score, start=1):
    print(f"  {rank}. {name}: {score}")

# any() and all()
numbers = [2, 4, 6, 8, 10]
print("\nAll even?", all(n % 2 == 0 for n in numbers))   # True
print("Any > 9?", any(n > 9 for n in numbers))            # True

passwords = ["abc", "longpassword123", "xy"]
print("All valid (>=8 chars)?", all(len(p) >= 8 for p in passwords))  # False


# ─────────────────────────────────────────────
# 8. PRACTICAL EXAMPLE — Data Processing Pipeline
# ─────────────────────────────────────────────

raw_data = [
    {"name": "alice", "score": 85, "active": True},
    {"name": "BOB", "score": 42, "active": False},
    {"name": "Charlie", "score": 91, "active": True},
    {"name": "diana", "score": 67, "active": True},
    {"name": "EVE", "score": 38, "active": False},
]

# Using comprehensions to process data
active_students = [
    {
        "name": s["name"].title(),
        "score": s["score"],
        "grade": "A" if s["score"] >= 90 else "B" if s["score"] >= 70 else "C"
    }
    for s in raw_data
    if s["active"]
]

print("\nActive students (processed):")
for student in sorted(active_students, key=lambda s: s["score"], reverse=True):
    print(f"  {student['name']}: {student['score']} ({student['grade']})")

avg_score = sum(s["score"] for s in active_students) / len(active_students)
print(f"Average score: {avg_score:.1f}")


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Given a list of words, use list comprehension to:
#    - Get words with more than 5 letters
#    - Get their lengths as a separate list
#    words = ["cat", "elephant", "dog", "python", "ox", "anaconda"]

# 2. Given a list of temperatures in Celsius:
#    temps_c = [-10, 0, 20, 37, 100]
#    Use list comprehension to convert to Fahrenheit: F = C * 9/5 + 32

# 3. Write a generator function prime_numbers() that infinitely yields prime numbers.
#    Use it to get the first 20 prime numbers.

# 4. Given this data, use dict comprehension to create a lookup by email:
#    users = [{"name": "Alice", "email": "a@b.com"}, {"name": "Bob", "email": "b@c.com"}]
#    Result: {"a@b.com": "Alice", "b@c.com": "Bob"}

# YOUR CODE HERE:
