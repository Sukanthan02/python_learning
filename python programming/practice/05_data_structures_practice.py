# ============================================================
# LESSON 05: Data Structures — Lists, Tuples, Sets, Dictionaries
# ============================================================
# 🎯 Goal: Store and organize multiple pieces of data

# ════════════════════════════════════════════
# PART A: LISTS — ordered, mutable, allows duplicates
# ════════════════════════════════════════════

print("=" * 50)
print("LISTS")
print("=" * 50)

# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]    # Lists can hold any type!

print(fruits)


# ── Accessing Items ─────────────────────────
print(fruits[0])        # "apple"  → First item (index starts at 0)
print(fruits[-1])       # "mango"  → Last item (negative index)
print(fruits[1:3])      # ["banana", "cherry"] → Slicing

# ── Modifying Items ─────────────────────────
fruits[1] = "blueberry"
print(fruits)           # ['apple', 'blueberry', 'cherry', 'mango']

# ── Adding Items ─────────────────────────────
fruits.append("grape")          # Add to end
fruits.insert(1, "kiwi")       # Insert at position 1
fruits.extend(["lemon", "lime"]) # Add multiple items
print(fruits)

# ── Removing Items ─────────────────────────
fruits.remove("kiwi")           # Remove by value
popped = fruits.pop()           # Remove last item and return it
popped_at = fruits.pop(0)      # Remove item at index 0
print(f"Removed: {popped}, {popped_at}")
print(fruits)

# ── List Info ───────────────────────────────
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(numbers))             # 8  → length
print(numbers.count(1))        # 2  → count occurrences
print(numbers.index(4))        # 2  → find position of value
print(min(numbers))             # 1  → minimum
print(max(numbers))             # 9  → maximum
print(sum(numbers))             # 31 → sum

# ── Sorting ─────────────────────────────────
numbers.sort()                  # Sort in-place (modifies list)
print(numbers)                  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)      # Sort descending
print(numbers)

sorted_nums = sorted([5, 3, 8, 1])  # Returns NEW sorted list
print(sorted_nums)

# ── Other Useful Operations ─────────────────
numbers.reverse()               # Reverse in-place
numbers_copy = numbers.copy()   # Shallow copy
numbers.clear()                 # Remove all items

# ── Check Membership ────────────────────────
colors = ["red", "green", "blue"]
print("red" in colors)          # True
print("purple" not in colors)  # True


# ════════════════════════════════════════════
# PART B: TUPLES — ordered, IMMUTABLE (cannot change)
# ════════════════════════════════════════════

print("\n" + "=" * 50)
print("TUPLES")
print("=" * 50)

# Creating tuples — use () or just commas
coordinates = (10.5, 20.3)
rgb = (255, 128, 0)
single = (42,)          # IMPORTANT: trailing comma for single item!

print(coordinates[0])   # 10.5
print(rgb[1])           # 128

# Tuples are immutable — you CANNOT do this:
# rgb[0] = 100  ← ❌ ERROR

# Unpacking tuples
x, y = coordinates
print(f"x={x}, y={y}")

# Use tuples for fixed data that shouldn't change
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print(DAYS_OF_WEEK)

# Tuples are faster than lists — use for fixed data!
print(type(coordinates))   # <class 'tuple'>


# ════════════════════════════════════════════
# PART C: SETS — unordered, UNIQUE items only
# ════════════════════════════════════════════

print("\n" + "=" * 50)
print("SETS")
print("=" * 50)

# Creating a set — duplicates are automatically removed!
colors = {"red", "blue", "green", "red", "blue"}
print(colors)           # {'red', 'blue', 'green'} — duplicates gone!

# Create from list (remove duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)           # {1, 2, 3, 4}

# ── Set Operations ───────────────────────────
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print(set_a | set_b)    # Union     → {1,2,3,4,5,6,7} — all items
print(set_a & set_b)    # Intersection → {3,4,5} — common items
print(set_a - set_b)    # Difference → {1,2} — in A but not B
print(set_a ^ set_b)    # Symmetric diff → {1,2,6,7} — not in both

# ── Adding / Removing ───────────────────────
colors.add("yellow")
colors.discard("red")   # Remove if exists (no error if missing)
print(colors)

# Check membership (very fast for sets!)
print("blue" in colors)


# ════════════════════════════════════════════
# PART D: DICTIONARIES — key-value pairs
# ════════════════════════════════════════════

print("\n" + "=" * 50)
print("DICTIONARIES")
print("=" * 50)

# Creating a dictionary
user = {
    "name": "Sukanthan",
    "age": 25,
    "city": "Chennai",
    "is_active": True
}

print(user)

# ── Accessing Values ─────────────────────────
print(user["name"])              # "Sukanthan" — direct access
print(user.get("age"))          # 25 — safe access
print(user.get("email", "N/A")) # "N/A" — default if key missing

# ── Adding / Updating ────────────────────────
user["email"] = "sukanthan@email.com"   # Add new key
user["age"] = 26                         # Update existing key
print(user)

# ── Removing ─────────────────────────────────
removed = user.pop("city")              # Remove and return value
print(f"Removed city: {removed}")
del user["is_active"]                   # Just delete

# ── Iterating ────────────────────────────────
print("\nUser details:")
for key, value in user.items():         # .items() → key-value pairs
    print(f"  {key}: {value}")

print("\nKeys:", list(user.keys()))     # All keys
print("Values:", list(user.values())) # All values

# ── Checking Keys ─────────────────────────────
print("name" in user)       # True
print("phone" in user)      # False

# ── Nested Dictionaries ──────────────────────
employees = {
    "E001": {"name": "Alice", "role": "Backend Dev", "salary": 80000},
    "E002": {"name": "Bob",   "role": "Frontend Dev", "salary": 75000},
    "E003": {"name": "Charlie", "role": "DevOps",    "salary": 90000},
}

print(f"\n{employees['E001']['name']} is a {employees['E001']['role']}")

# Loop through nested dict
for emp_id, details in employees.items():
    print(f"{emp_id}: {details['name']} - {details['role']}")

# ── dict.update() ────────────────────────────
defaults = {"theme": "dark", "language": "en", "notifications": True}
user_prefs = {"theme": "light", "font_size": 14}

defaults.update(user_prefs)   # Merge user prefs into defaults
print(defaults)


# ─────────────────────────────────────────────
# COMPARISON: Which to use when?
# ─────────────────────────────────────────────
print("\n📚 Quick Reference:")
print("LIST  → ordered, changeable, allow duplicates → [1, 2, 3]")
print("TUPLE → ordered, unchangeable, allow duplicates → (1, 2, 3)")
print("SET   → unordered, no duplicates, fast lookup → {1, 2, 3}")
print("DICT  → key-value pairs, fast lookup by key → {'a': 1}")


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Create a list of 5 programming languages. Sort them alphabetically.
#    Then add "Python" and remove the last one.

# 2. You have two lists:
#    list1 = [1, 2, 3, 4, 5]
#    list2 = [4, 5, 6, 7, 8]
#    Find: common items, unique to list1, all unique items combined.
#    Hint: Convert to sets!

# 3. Create a dictionary for a student with:
#    name, age, grades (a list of numbers), and city
#    Calculate and print the average grade.

# 4. Given this list with duplicates:
#    data = [1, 5, 3, 2, 5, 1, 3, 8, 9, 2]
#    Remove duplicates using a set, then sort and print.

# 5. Create a phonebook dictionary with 3 contacts.
#    Write code to look up a name and return the phone number,
#    or "Not found" if the name doesn't exist.

# YOUR CODE HERE:
