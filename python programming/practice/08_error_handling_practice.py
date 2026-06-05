# ============================================================
# LESSON 08: Error Handling — try/except, Custom Exceptions
# ============================================================
# 🎯 Goal: Handle errors gracefully so your app doesn't crash

# ─────────────────────────────────────────────
# 1. WHY ERROR HANDLING?
# ─────────────────────────────────────────────
# Without error handling:
# result = 10 / 0     ← This crashes the entire program!
# print(result)

# With error handling:
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")


# ─────────────────────────────────────────────
# 2. COMMON BUILT-IN EXCEPTIONS
# ─────────────────────────────────────────────
# ValueError       → Wrong value type conversion
# TypeError        → Wrong type for operation
# IndexError       → List index out of range
# KeyError         → Dictionary key not found
# FileNotFoundError → File doesn't exist
# ZeroDivisionError → Divided by zero
# AttributeError   → Object has no attribute
# NameError        → Variable not defined
# ImportError      → Module not found

examples = [
    ("int('abc')",           int, ("abc",)),
    ("10 / 0",               lambda a, b: a / b, (10, 0)),
    ("[1,2,3][10]",          lambda l, i: l[i], ([1, 2, 3], 10)),
    ("{'a':1}['z']",         lambda d, k: d[k], ({"a": 1}, "z")),
]

print("Common Exceptions Demo:")
for desc, fn, args in examples:
    try:
        result = fn(*args)
    except (ValueError, ZeroDivisionError, IndexError, KeyError) as e:
        print(f"  {type(e).__name__}: {e}  (from: {desc})")


# ─────────────────────────────────────────────
# 3. TRY / EXCEPT / ELSE / FINALLY
# ─────────────────────────────────────────────

def safe_divide(a, b):
    try:
        result = a / b             # Code that might fail
    except ZeroDivisionError:
        print("  ❌ Division by zero!")
        return None
    except TypeError:
        print("  ❌ Invalid types — need numbers!")
        return None
    else:
        # Runs ONLY if no exception occurred
        print(f"  ✅ Result: {result}")
        return result
    finally:
        # ALWAYS runs — great for cleanup
        print("  🔄 Division attempt complete.")

print("\nDivision tests:")
safe_divide(10, 2)      # Success
safe_divide(10, 0)      # ZeroDivisionError
safe_divide("a", "b")  # TypeError


# ─────────────────────────────────────────────
# 4. CATCHING MULTIPLE EXCEPTIONS
# ─────────────────────────────────────────────

def parse_number(text):
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return None

print("\nParsing numbers:")
print(parse_number("42"))       # 42
print(parse_number("3.14"))     # 3.14
print(parse_number("hello"))    # None

# Catch multiple in one line
def process(data):
    try:
        result = data[0] / data[1]
        return result
    except (IndexError, ZeroDivisionError, TypeError) as e:
        print(f"  Error ({type(e).__name__}): {e}")
        return None

process([10, 2])
process([10])
process([10, 0])
process("not a list")


# ─────────────────────────────────────────────
# 5. RAISE — Trigger exceptions intentionally
# ─────────────────────────────────────────────

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is not realistic (must be 0-150).")
    return age

print("\nAge validation:")
try:
    set_age(-5)
except ValueError as e:
    print(f"  ❌ {e}")

try:
    set_age("twenty")
except TypeError as e:
    print(f"  ❌ {e}")

try:
    print(f"  ✅ Age set to {set_age(25)}")
except Exception as e:
    print(f"  ❌ {e}")


# ─────────────────────────────────────────────
# 6. CUSTOM EXCEPTIONS — Define your own errors
# ─────────────────────────────────────────────

class AppError(Exception):
    """Base exception for this application."""
    pass

class ValidationError(AppError):
    """Raised when data validation fails."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Validation failed on '{field}': {message}")

class AuthenticationError(AppError):
    """Raised when authentication fails."""
    def __init__(self, reason="Invalid credentials"):
        super().__init__(f"Authentication failed: {reason}")

class NotFoundError(AppError):
    """Raised when a resource is not found."""
    def __init__(self, resource, identifier):
        super().__init__(f"{resource} with id '{identifier}' not found.")

# Using custom exceptions
def register_user(username, password):
    if len(username) < 3:
        raise ValidationError("username", "Must be at least 3 characters long.")
    if len(password) < 8:
        raise ValidationError("password", "Must be at least 8 characters long.")
    return {"username": username, "status": "registered"}

def get_user(user_id, db):
    if user_id not in db:
        raise NotFoundError("User", user_id)
    return db[user_id]

print("\nCustom exception tests:")
fake_db = {1: "Alice", 2: "Bob"}

try:
    register_user("ab", "secret123")
except ValidationError as e:
    print(f"  ❌ {e}")

try:
    register_user("alice", "short")
except ValidationError as e:
    print(f"  ❌ {e}")

try:
    result = register_user("alice", "securepassword")
    print(f"  ✅ {result}")
except ValidationError as e:
    print(f"  ❌ {e}")

try:
    user = get_user(99, fake_db)
except NotFoundError as e:
    print(f"  ❌ {e}")

try:
    user = get_user(1, fake_db)
    print(f"  ✅ Found user: {user}")
except NotFoundError as e:
    print(f"  ❌ {e}")


# ─────────────────────────────────────────────
# 7. CONTEXT MANAGERS — with statement
# ─────────────────────────────────────────────
# "with" ensures cleanup happens even if an error occurs
# Most common use: file operations

import json
import os

def safe_read_json(filename):
    """Read a JSON file safely."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"  ❌ File '{filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"  ❌ Invalid JSON in '{filename}': {e}")
        return None

# Test it
data = safe_read_json("nonexistent.json")
print(f"\nResult: {data}")

# Create and read a valid JSON
with open("temp.json", "w") as f:
    json.dump({"name": "test"}, f)

data = safe_read_json("temp.json")
print(f"Result: {data}")
os.remove("temp.json")


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Write a function `safe_int_input(prompt)` that keeps asking the user
#    for input until they enter a valid integer.

# 2. Create a custom exception `InsufficientFundsError` for a bank account.
#    Write a BankAccount class with deposit() and withdraw() methods.
#    Raise InsufficientFundsError if balance would go negative.

# 3. Write a function that reads a CSV file and handles:
#    - FileNotFoundError
#    - Empty file (no data)
#    - Malformed rows (wrong number of columns)

# YOUR CODE HERE:
