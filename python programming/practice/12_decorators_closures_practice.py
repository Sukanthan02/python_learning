# ============================================================
# LESSON 12: Decorators & Closures
# ============================================================
# 🎯 Goal: Understand higher-order functions and @decorators

# ─────────────────────────────────────────────
# 1. FIRST-CLASS FUNCTIONS — Functions as values
# ─────────────────────────────────────────────
# In Python, functions are objects! They can be:
# - Stored in variables
# - Passed as arguments
# - Returned from functions

def say_hello():
    print("Hello!")

# Store in a variable
greet = say_hello       # No () — we're NOT calling it, just referencing
greet()                 # Now call it → "Hello!"

# Pass as argument
def run_function(fn):
    print("Running function...")
    fn()

run_function(say_hello)   # Pass the function itself

# Return a function
def get_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply     # Return the inner function!

double = get_multiplier(2)
triple = get_multiplier(3)

print(double(5))    # 10
print(triple(5))    # 15


# ─────────────────────────────────────────────
# 2. CLOSURES — Inner function remembers outer vars
# ─────────────────────────────────────────────

def make_counter(start=0):
    count = start   # This variable is "captured" by the closure
    
    def increment(by=1):
        nonlocal count          # Allow modifying the outer variable
        count += by
        return count
    
    return increment

counter = make_counter(10)
print(counter())     # 11
print(counter())     # 12
print(counter(5))    # 17

# Each counter is independent!
counter2 = make_counter(0)
print(counter2())    # 1
print(counter())     # 18 (counter still at 17+1)


# ─────────────────────────────────────────────
# 3. DECORATORS — Wrap a function with extra behavior
# ─────────────────────────────────────────────
# A decorator is a function that takes a function and returns a new (enhanced) function

# Manual decorator (to understand the concept)
def timer_decorator(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)      # Call the original function
        end = time.time()
        print(f"  ⏱️  {func.__name__}() took {(end-start)*1000:.2f}ms")
        return result
    
    return wrapper

# Applying manually
def slow_function():
    import time
    time.sleep(0.1)
    return "Done!"

slow_function = timer_decorator(slow_function)  # Manual decoration
result = slow_function()
print(result)


# Using @ syntax (syntactic sugar — same thing!)
import time
import functools

def timer(func):
    @functools.wraps(func)      # Preserves original function name/docs
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = (time.time() - start) * 1000
        print(f"  ⏱️  {func.__name__}() took {elapsed:.2f}ms")
        return result
    return wrapper

@timer
def compute_squares(n):
    return [i**2 for i in range(n)]

result = compute_squares(10000)
print(f"Computed {len(result)} squares")


# ─────────────────────────────────────────────
# 4. COMMON DECORATOR PATTERNS
# ─────────────────────────────────────────────

# ── Logger Decorator ────────────────────────
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(a) for a in args)
        print(f"  📝 Calling {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"  📝 {func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 5)


# ── Retry Decorator ─────────────────────────
def retry(max_attempts=3, delay=0.1):
    """Decorator factory — decorator with parameters."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  ⚠️  Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise Exception(f"All {max_attempts} attempts failed!")
        return wrapper
    return decorator

import random

@retry(max_attempts=3, delay=0.05)
def unstable_api_call():
    """Simulates an API that sometimes fails."""
    if random.random() < 0.6:    # 60% chance of failure
        raise ConnectionError("Server temporarily unavailable")
    return "API response: success!"

try:
    result = unstable_api_call()
    print(f"  ✅ {result}")
except Exception as e:
    print(f"  ❌ {e}")


# ── Cache / Memoize Decorator ────────────────
def memoize(func):
    """Cache function results to avoid recomputation."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"\nFibonacci(35) = {fibonacci(35)}")   # Fast with cache!

# Python has built-in memoization:
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(f"fib(40) = {fib(40)}")


# ── Validate Input Decorator ─────────────────
def validate_positive(*param_positions):
    """Validate that specific parameters are positive numbers."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for pos in param_positions:
                if pos < len(args) and args[pos] <= 0:
                    raise ValueError(f"Argument at position {pos} must be positive!")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_positive(0, 1)
def divide(a, b):
    return a / b

try:
    print(divide(10, 2))      # 5.0 ✅
    print(divide(-5, 2))      # ❌ ValueError
except ValueError as e:
    print(f"  ❌ {e}")


# ─────────────────────────────────────────────
# 5. STACKING DECORATORS
# ─────────────────────────────────────────────
# Multiple decorators are applied bottom-up!

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@bold
@uppercase
def greet(name):
    return f"hello, {name}"

print(greet("World"))    # **HELLO, WORLD** (uppercase first, then bold)


# ─────────────────────────────────────────────
# 6. REAL BACKEND USE — Auth Decorator
# ─────────────────────────────────────────────

# This is similar to how FastAPI/Flask route protection works!

fake_user = {"id": 1, "name": "Alice", "role": "admin"}

def require_auth(func):
    """Simulate authentication check."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # In real app: check token from request headers
        token = kwargs.get("token", None)
        if not token:
            raise PermissionError("Authentication required!")
        # In real app: decode and verify the token
        print(f"  🔐 Auth passed for token: {token[:8]}...")
        kwargs["user"] = fake_user   # Inject user into function
        return func(*args, **kwargs)
    return wrapper

def require_role(role):
    """Simulate role-based access control."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user = kwargs.get("user", {})
            if user.get("role") != role:
                raise PermissionError(f"Requires role: {role}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_auth
@require_role("admin")
def delete_user(user_id, token=None, user=None):
    print(f"  🗑️  User {user_id} deleted by {user['name']}")
    return True

try:
    delete_user(99, token="fake_jwt_token_abc123")
except PermissionError as e:
    print(f"  ❌ {e}")


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Create a @uppercase decorator that converts function's return value to uppercase.

# 2. Create a @rate_limit(calls_per_minute) decorator factory that
#    limits how many times a function can be called per minute.

# 3. Create a @deprecated(message) decorator that prints a warning
#    when the decorated function is called.

# 4. Create a @singleton decorator that ensures a class only has one instance.

# YOUR CODE HERE:
