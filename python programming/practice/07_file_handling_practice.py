# ============================================================
# LESSON 07: File Handling — Read, Write, Append
# ============================================================
# 🎯 Goal: Read from and write to files using Python

import os

# ─────────────────────────────────────────────
# 1. WRITING TO A FILE
# ─────────────────────────────────────────────
# Mode "w" → write (creates file if not exists, OVERWRITES if exists)

with open("sample.txt", "w") as file:
    file.write("Hello, File World!\n")
    file.write("This is line 2.\n")
    file.write("Python file handling is easy!\n")

print("✅ File written successfully!")

# ─────────────────────────────────────────────
# 2. READING FROM A FILE
# ─────────────────────────────────────────────
# Mode "r" → read (default)

# Read entire file as one string
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFull content:")
    print(content)

# Read line by line (memory efficient for large files)
with open("sample.txt", "r") as file:
    print("Line by line:")
    for line in file:
        print(f"  > {line.strip()}")

# Read all lines into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"\nNumber of lines: {len(lines)}")
    print(f"First line: {lines[0].strip()}")


# ─────────────────────────────────────────────
# 3. APPENDING TO A FILE
# ─────────────────────────────────────────────
# Mode "a" → append (adds to end, does NOT overwrite)

with open("sample.txt", "a") as file:
    file.write("This line was appended later.\n")
    file.write("Appending is useful for logs!\n")

print("\n✅ Lines appended!")

# Verify append worked
with open("sample.txt", "r") as file:
    print(file.read())


# ─────────────────────────────────────────────
# 4. FILE MODES SUMMARY
# ─────────────────────────────────────────────
# "r"  → Read only (default). Error if file doesn't exist.
# "w"  → Write. Creates or overwrites file.
# "a"  → Append. Creates or adds to end of file.
# "x"  → Exclusive create. Error if file EXISTS.
# "r+" → Read + write. Error if file doesn't exist.
# "w+" → Write + read. Creates or overwrites.
# "b"  → Binary mode (add to others: "rb", "wb")


# ─────────────────────────────────────────────
# 5. WORKING WITH JSON FILES (very common in backend!)
# ─────────────────────────────────────────────
import json

# Write JSON file
data = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@email.com", "active": True},
        {"id": 2, "name": "Bob",   "email": "bob@email.com",   "active": False},
        {"id": 3, "name": "Charlie", "email": "charlie@email.com", "active": True},
    ]
}

with open("users.json", "w") as file:
    json.dump(data, file, indent=4)  # indent=4 makes it pretty

print("✅ JSON file written!")

# Read JSON file
with open("users.json", "r") as file:
    loaded = json.load(file)

print("\nLoaded users:")
for user in loaded["users"]:
    status = "Active" if user["active"] else "Inactive"
    print(f"  {user['id']}. {user['name']} ({status})")


# ─────────────────────────────────────────────
# 6. FILE EXISTENCE CHECKS
# ─────────────────────────────────────────────
import os

filename = "sample.txt"
print(f"\nFile exists: {os.path.exists(filename)}")
print(f"File size: {os.path.getsize(filename)} bytes")
print(f"Is file: {os.path.isfile(filename)}")
print(f"Is directory: {os.path.isdir(filename)}")


# ─────────────────────────────────────────────
# 7. HANDLING FILE ERRORS
# ─────────────────────────────────────────────
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("\n❌ File not found!")
except PermissionError:
    print("\n❌ No permission to read this file!")
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")


# ─────────────────────────────────────────────
# 8. PRACTICAL EXAMPLE — Simple Logger
# ─────────────────────────────────────────────
from datetime import datetime

def log(message, level="INFO", filename="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    with open(filename, "a") as f:
        f.write(log_entry)
    print(f"  Logged: {log_entry.strip()}")

def read_logs(filename="app.log"):
    if not os.path.exists(filename):
        print("No log file found.")
        return
    with open(filename, "r") as f:
        print(f.read())

# Test the logger
print("\n📋 Testing Logger:")
log("Application started")
log("User logged in: alice@email.com")
log("Failed login attempt", level="WARNING")
log("Database connection failed", level="ERROR")

print("\n📄 Log file contents:")
read_logs()

# Cleanup demo files
for f in ["sample.txt", "users.json", "app.log"]:
    if os.path.exists(f):
        os.remove(f)
print("\n🧹 Demo files cleaned up.")


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Create a file "shopping_list.txt". Write 5 grocery items (one per line).
#    Then read the file and print each item with a number (1. Apple, 2. Milk...)

# 2. Create a simple contact book:
#    - Save contacts as JSON: [{"name": "Alice", "phone": "1234567890"}, ...]
#    - Write a function to add a contact
#    - Write a function to search by name
#    - Write a function to list all contacts

# 3. Write a function that counts:
#    - Total lines in a file
#    - Total words in a file
#    - Total characters in a file

# YOUR CODE HERE:
