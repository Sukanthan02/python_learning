# ============================================================
# LESSON 10: Modules & Packages
# ============================================================
# 🎯 Goal: Organize code, use built-in modules, and install packages

# ─────────────────────────────────────────────
# 1. IMPORTING BUILT-IN MODULES
# ─────────────────────────────────────────────

# Import entire module
import math
print(math.pi)              # 3.141592...
print(math.sqrt(16))        # 4.0
print(math.floor(4.7))      # 4
print(math.ceil(4.2))       # 5

# Import specific things from a module
from math import sqrt, pi, factorial
print(sqrt(25))             # 5.0
print(pi)                   # 3.141592...
print(factorial(5))         # 120

# Import with alias
import math as m
print(m.pow(2, 10))         # 1024.0


# ─────────────────────────────────────────────
# 2. USEFUL BUILT-IN MODULES
# ─────────────────────────────────────────────

# os — operating system interactions
import os
print(os.getcwd())                    # Current directory
print(os.listdir("."))                # Files in current dir
os.makedirs("temp_dir", exist_ok=True)
os.rmdir("temp_dir")

# sys — system-specific parameters
import sys
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

# datetime — date and time
from datetime import datetime, date, timedelta

now = datetime.now()
print(f"Now: {now}")
print(f"Date: {now.strftime('%Y-%m-%d')}")
print(f"Time: {now.strftime('%H:%M:%S')}")

today = date.today()
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
print(f"Today: {today}, Tomorrow: {tomorrow}, Next week: {next_week}")

# Parse a date string
d = datetime.strptime("2024-06-15", "%Y-%m-%d")
print(f"Parsed date: {d}")

# random — random number generation
import random
print(random.randint(1, 100))         # Random int 1-100
print(random.choice(["a", "b", "c"])) # Random item from list
print(random.random())                # Float between 0.0 and 1.0

items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)

sample = random.sample(range(50), 5)  # 5 unique random nums from 0-49
print(sample)

# json — JSON encoding/decoding
import json
data = {"name": "Alice", "age": 30, "active": True}
json_string = json.dumps(data)          # dict → JSON string
print(json_string)

back_to_dict = json.loads(json_string)  # JSON string → dict
print(back_to_dict["name"])

# re — Regular Expressions
import re
text = "My email is user@example.com and phone is 987-654-3210"

# Find email
email = re.search(r"[\w.]+@[\w.]+\.[a-z]{2,}", text)
if email:
    print(f"Email found: {email.group()}")

# Find all numbers
numbers = re.findall(r"\d+", text)
print(f"Numbers found: {numbers}")


# ─────────────────────────────────────────────
# 3. CREATING YOUR OWN MODULE
# ─────────────────────────────────────────────
# A module is simply a .py file!
# See: helpers.py in this folder

# helpers.py would contain:
"""
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
"""

# Then in your main file:
# from helpers import greet, add, PI
# print(greet("Alice"))


# ─────────────────────────────────────────────
# 4. PACKAGES — Folders of modules
# ─────────────────────────────────────────────
# A package is a folder with __init__.py
#
# mypackage/
#   __init__.py       ← makes it a package
#   utils.py
#   validators.py
#   models/
#       __init__.py
#       user.py
#
# Usage:
# from mypackage import utils
# from mypackage.validators import validate_email


# ─────────────────────────────────────────────
# 5. PIP — Installing third-party packages
# ─────────────────────────────────────────────
# Open terminal and run:

# Install a package:
#   pip install requests

# Install specific version:
#   pip install requests==2.28.0

# Install multiple from a file:
#   pip install -r requirements.txt

# List installed packages:
#   pip list

# Save current packages to file:
#   pip freeze > requirements.txt

# Uninstall:
#   pip uninstall requests


# ─────────────────────────────────────────────
# 6. VIRTUAL ENVIRONMENTS — Isolate dependencies
# ─────────────────────────────────────────────
# ALWAYS use a virtual environment for each project!

# Create a virtual environment:
#   python -m venv venv

# Activate it:
#   Windows:   venv\Scripts\activate
#   Mac/Linux: source venv/bin/activate

# Now install packages — they go into venv, not globally!
#   pip install fastapi uvicorn

# Deactivate:
#   deactivate


# ─────────────────────────────────────────────
# 7. POPULAR PACKAGES FOR BACKEND DEVELOPMENT
# ─────────────────────────────────────────────

packages = {
    "fastapi":       "Modern, fast web framework for APIs",
    "uvicorn":       "ASGI server to run FastAPI",
    "sqlalchemy":    "Database ORM (Object Relational Mapper)",
    "alembic":       "Database migration tool for SQLAlchemy",
    "pydantic":      "Data validation and settings management",
    "httpx":         "HTTP client for async requests",
    "python-dotenv": "Load .env configuration files",
    "pytest":        "Testing framework",
    "redis":         "Redis client for caching",
    "celery":        "Distributed task queue",
    "boto3":         "AWS SDK for Python",
    "pandas":        "Data manipulation and analysis",
}

print("\n📦 Essential Backend Packages:")
for pkg, desc in packages.items():
    print(f"  {pkg:<20} → {desc}")


# ─────────────────────────────────────────────
# 8. PRACTICAL EXAMPLE — Using requests library
# ─────────────────────────────────────────────
# First install: pip install requests

"""
import requests

# GET request to a public API
response = requests.get("https://httpbin.org/json")

if response.status_code == 200:
    data = response.json()
    print("API Response:", data)
else:
    print(f"Error: {response.status_code}")

# POST request
payload = {"name": "Alice", "job": "Developer"}
response = requests.post("https://reqres.in/api/users", json=payload)
print("Created:", response.json())
"""

print("\n💡 Uncomment the requests section and run after: pip install requests")


# ─────────────────────────────────────────────
# 9. __name__ == "__main__"
# ─────────────────────────────────────────────
# This block ONLY runs when the file is executed directly
# NOT when the file is imported as a module

if __name__ == "__main__":
    print("\n✅ This script is running directly!")
    
    # Put your main code here
    today = date.today()
    print(f"Today's date: {today}")
    print(f"Python version: {sys.version.split()[0]}")


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Using the datetime module:
#    - Print how many days until Christmas (Dec 25) from today
#    - Print what day of the week your birthday falls on this year

# 2. Using the random module:
#    - Generate a random 6-character password with letters and digits
#    - Simulate rolling 2 dice 10 times and count doubles

# 3. Create your own module "math_helpers.py" with these functions:
#    - is_prime(n): returns True if n is prime
#    - fibonacci(n): returns list of first n fibonacci numbers
#    - factors(n): returns list of all factors of n
#    Then import and use them in this file.

# 4. Create a requirements.txt listing packages you would need for
#    a basic FastAPI project with database and JWT authentication.

# YOUR CODE HERE:
