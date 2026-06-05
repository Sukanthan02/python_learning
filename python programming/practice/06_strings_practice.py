# ============================================================
# LESSON 06: Strings — Methods, Formatting, Slicing
# ============================================================
# 🎯 Goal: Master string manipulation in Python

# ─────────────────────────────────────────────
# 1. CREATING STRINGS
# ─────────────────────────────────────────────
single = 'Hello'
double = "World"
multi  = """This is a
multi-line string"""

print(single, double)
print(multi)


# ─────────────────────────────────────────────
# 2. STRING INDEXING & SLICING
# ─────────────────────────────────────────────
text = "Python Programming"

print(text[0])          # P   → first character
print(text[-1])         # g   → last character
print(text[0:6])        # Python
print(text[7:])         # Programming
print(text[:6])         # Python
print(text[::2])        # every 2nd character
print(text[::-1])       # REVERSED string


# ─────────────────────────────────────────────
# 3. STRING METHODS
# ─────────────────────────────────────────────
message = "  Hello, Python World!  "

print(message.upper())          # UPPERCASE
print(message.lower())          # lowercase
print(message.title())          # Title Case
print(message.strip())          # Remove spaces
print(message.replace("Python", "Java"))

text = "Python is amazing. Python is popular."
print(text.find("Python"))      # 0  → index
print(text.count("Python"))     # 2  → count
print(text.startswith("Python"))# True
print(text.endswith("popular."))# True

# Split & Join
csv = "apple,banana,cherry,mango"
fruits = csv.split(",")        # → list
joined = " | ".join(fruits)    # → string
print(fruits)
print(joined)

# Check content
print("hello".isalpha())       # True
print("12345".isdigit())       # True
print("hello123".isalnum())    # True


# ─────────────────────────────────────────────
# 4. STRING FORMATTING (f-strings)
# ─────────────────────────────────────────────
name = "Alice"
score = 95.567
items = 3

print(f"Name: {name}")
print(f"Score: {score:.2f}")       # 2 decimal places
print(f"Items: {items:05d}")       # Pad zeros: 00003
print(f"Name: {name:>10}")         # Right-align
print(f"Name: {name:<10}|")       # Left-align
print(f"Name: {name:^10}|")       # Center

x, y = 5, 3
print(f"{x} + {y} = {x + y}")
print(f"{'hello'.upper()}")


# ─────────────────────────────────────────────
# 5. ESCAPE CHARACTERS
# ─────────────────────────────────────────────
print("Line 1\nLine 2")           # new line
print("Name:\tSukanthan")         # tab
print("He said \"Hello\"")        # quote inside string
path = r"C:\Users\Documents"      # raw string (no escaping)
print(path)


# ─────────────────────────────────────────────
# 6. PRACTICAL EXAMPLE — Email Validator
# ─────────────────────────────────────────────
def validate_email(email):
    email = email.strip().lower()
    if "@" not in email:
        return False, "Missing @ symbol"
    parts = email.split("@")
    if len(parts) != 2:
        return False, "Invalid format"
    username, domain = parts
    if len(username) < 1:
        return False, "Username too short"
    if "." not in domain:
        return False, "Domain must have a dot"
    return True, "Valid email!"

emails = ["sukanthan@gmail.com", "invalid-email", "missing@dot"]
for email in emails:
    is_valid, message = validate_email(email)
    status = "✅" if is_valid else "❌"
    print(f"  {status} '{email}': {message}")


# ─────────────────────────────────────────────
# 7. PRACTICAL EXAMPLE — Slug Generator
# ─────────────────────────────────────────────
def generate_slug(title):
    slug = title.lower().strip().replace(" ", "-")
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789-"
    return "".join(c for c in slug if c in allowed)

print(generate_slug("My First Blog Post!"))
print(generate_slug("Python for Backend Developers 2024"))


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Check if "racecar" is a palindrome (reads same forwards and backwards).

# 2. Given: "John Michael Smith" — extract first name, last name, initials.

# 3. Count words in: "apple banana apple cherry apple banana"
#    Expected output: {"apple": 3, "banana": 2, "cherry": 1}

# 4. Write mask_credit_card("1234567890123456") → "****-****-****-3456"

# YOUR CODE HERE:
