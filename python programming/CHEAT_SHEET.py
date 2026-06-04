# ============================================================
# PYTHON CHEAT SHEET — Quick Reference for All Lessons
# ============================================================

# ── Variables & Types ─────────────────────────────────────
x = 10          # int
y = 3.14        # float
s = "hello"     # str
b = True        # bool
n = None        # NoneType
print(type(x))  # <class 'int'>

# ── Type Conversion ───────────────────────────────────────
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"

# ── F-strings ─────────────────────────────────────────────
name = "Alice"
print(f"Hello, {name}!")
print(f"{3.14159:.2f}")     # 3.14
print(f"{100:05d}")         # 00100

# ── Operators ─────────────────────────────────────────────
# Math:  +  -  *  /  //  %  **
# Compare: ==  !=  <  >  <=  >=
# Logic: and  or  not
# Membership: in  not in

# ── Control Flow ──────────────────────────────────────────
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

for i in range(5):          # 0,1,2,3,4
    print(i)

while x > 0:
    x -= 1

# ── Functions ─────────────────────────────────────────────
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")              # uses default
greet("Bob", "Hi")          # overrides default

# Lambda
double = lambda x: x * 2
sorted_list = sorted([3,1,2], key=lambda x: -x)

# ── Lists ─────────────────────────────────────────────────
lst = [1, 2, 3]
lst.append(4)               # [1,2,3,4]
lst.insert(0, 0)            # [0,1,2,3,4]
lst.remove(2)               # removes first 2
lst.pop()                   # removes last
lst.sort()                  # in-place sort
lst[1:3]                    # slice
len(lst)                    # length

# ── Tuples ────────────────────────────────────────────────
t = (1, 2, 3)               # immutable
a, b, c = t                 # unpacking

# ── Sets ──────────────────────────────────────────────────
s = {1, 2, 3}
s.add(4)
s.discard(2)
{1,2,3} | {3,4,5}           # union
{1,2,3} & {3,4,5}           # intersection
{1,2,3} - {3,4,5}           # difference

# ── Dictionaries ──────────────────────────────────────────
d = {"name": "Alice", "age": 25}
d["email"] = "a@b.com"      # add/update
d.get("phone", "N/A")       # safe access
d.pop("age")                # remove
for k, v in d.items():      # iterate
    print(k, v)
"name" in d                 # check key

# ── String Methods ────────────────────────────────────────
s = "  Hello World  "
s.strip()                   # "Hello World"
s.upper() / s.lower()
s.replace("World", "Python")
s.split()                   # ["Hello", "World"]
",".join(["a","b","c"])     # "a,b,c"
s.startswith("Hello")
s.find("World")             # index
s.count("l")                # occurrences
s[0:5]                      # slice

# ── File Handling ─────────────────────────────────────────
with open("file.txt", "w") as f:
    f.write("Hello\n")

with open("file.txt", "r") as f:
    content = f.read()
    lines = f.readlines()

import json
with open("data.json", "w") as f:
    json.dump({"key": "value"}, f, indent=2)
with open("data.json") as f:
    data = json.load(f)

# ── Error Handling ────────────────────────────────────────
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
else:
    print("Success!")
finally:
    print("Always runs")

raise ValueError("Custom error message")

# ── Classes ───────────────────────────────────────────────
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} speaks"
    def __str__(self):
        return f"Animal({self.name})"

class Dog(Animal):
    def speak(self):           # Override
        return f"{self.name}: Woof!"

dog = Dog("Rex")
print(dog.speak())

# ── Comprehensions ────────────────────────────────────────
[x**2 for x in range(10)]
[x for x in range(10) if x % 2 == 0]
{k: v for k, v in d.items()}
{x for x in [1,2,2,3]}

# ── Decorators ────────────────────────────────────────────
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def hello():
    print("Hello!")

# ── Common Built-ins ──────────────────────────────────────
len([1,2,3])                # 3
range(5)                    # 0,1,2,3,4
enumerate(["a","b"])        # (0,"a"), (1,"b")
zip([1,2], ["a","b"])       # (1,"a"), (2,"b")
map(str, [1,2,3])           # ["1","2","3"]
filter(None, [0,1,2])       # [1,2]
sorted([3,1,2])             # [1,2,3]
sum([1,2,3])                # 6
min([1,2,3]) / max([1,2,3]) # 1 / 3
any([False, True])          # True
all([True, True])           # True
isinstance(42, int)         # True

# ── FastAPI Quick Reference ───────────────────────────────
"""
from fastapi import FastAPI, HTTPException, Query, Path, status
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    active: bool = True

@app.get("/items")
def list_items(): return [...]

@app.get("/items/{item_id}")
def get_item(item_id: int): ...

@app.post("/items", status_code=201)
def create_item(item: Item): ...

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item): ...

@app.delete("/items/{item_id}")
def delete_item(item_id: int): ...

# Run: uvicorn main:app --reload
"""
