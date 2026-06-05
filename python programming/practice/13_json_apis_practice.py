# ============================================================
# LESSON 13: Working with JSON & APIs
# ============================================================
# 🎯 Goal: Parse JSON data and call REST APIs from Python
# Install first: pip install requests httpx

import json
from datetime import datetime

# ─────────────────────────────────────────────
# 1. JSON BASICS — What is JSON?
# ─────────────────────────────────────────────
# JSON (JavaScript Object Notation) = the language of APIs
# Python dict ↔ JSON object
# Python list ↔ JSON array

# ─────────────────────────────────────────────
# 2. PYTHON json MODULE
# ─────────────────────────────────────────────

# Dict → JSON string (serialization)
user = {
    "id": 1,
    "name": "Sukanthan",
    "email": "sukanthan@example.com",
    "skills": ["Python", "FastAPI", "SQL"],
    "active": True,
    "age": 25
}

json_str = json.dumps(user)                 # Compact JSON string
json_pretty = json.dumps(user, indent=2)    # Pretty-printed
print("JSON string:\n", json_pretty)

# JSON string → Dict (deserialization)
data = json.loads(json_str)
print("\nDeserialized dict:")
print(data["name"])             # Sukanthan
print(data["skills"][0])       # Python

# Write JSON to file
with open("user.json", "w") as f:
    json.dump(user, f, indent=2)

# Read JSON from file
with open("user.json") as f:
    loaded = json.load(f)
print(f"\nLoaded from file: {loaded['name']}")

import os
os.remove("user.json")


# ─────────────────────────────────────────────
# 3. MAKING HTTP REQUESTS — requests library
# ─────────────────────────────────────────────
# pip install requests

try:
    import requests

    # ── GET Request ─────────────────────────────
    print("\n=== GET Request ===")
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    print(f"Status Code: {response.status_code}")   # 200 = OK
    print(f"Headers: {dict(list(response.headers.items())[:2])}")
    
    if response.status_code == 200:
        data = response.json()    # Automatically parse JSON!
        print(f"User: {data['name']} | Email: {data['email']}")
        print(f"City: {data['address']['city']}")
    
    # ── GET with Query Parameters ────────────────
    print("\n=== GET with Query Params ===")
    params = {"_limit": 3, "_page": 1}
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params=params
    )
    posts = response.json()
    print(f"Got {len(posts)} posts:")
    for post in posts:
        print(f"  - {post['title'][:50]}...")
    
    # ── POST Request — Create data ───────────────
    print("\n=== POST Request ===")
    new_post = {
        "title": "Python for Backend Developers",
        "body": "Learning Python is the best decision for backend dev!",
        "userId": 1
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post    # Automatically sets Content-Type: application/json
    )
    print(f"Status: {response.status_code}")   # 201 = Created
    created = response.json()
    print(f"Created post with ID: {created['id']}")

    # ── PUT Request — Update data ────────────────
    print("\n=== PUT Request ===")
    update_data = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=update_data
    )
    print(f"Status: {response.status_code}")   # 200 = OK
    
    # ── DELETE Request ───────────────────────────
    print("\n=== DELETE Request ===")
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    print(f"Status: {response.status_code}")   # 200 = OK

except ImportError:
    print("💡 Install requests: pip install requests")
    print("   Then uncomment and run the API examples above.")


# ─────────────────────────────────────────────
# 4. HANDLING API RESPONSES PROPERLY
# ─────────────────────────────────────────────

def safe_api_call(url, method="GET", **kwargs):
    """Wrapper for safe API calls with error handling."""
    try:
        response = requests.request(method, url, timeout=10, **kwargs)
        response.raise_for_status()    # Raise exception for 4xx/5xx
        return response.json()
    except requests.exceptions.ConnectionError:
        print("❌ No internet connection!")
    except requests.exceptions.Timeout:
        print("❌ Request timed out!")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e.response.status_code} - {e}")
    except requests.exceptions.JSONDecodeError:
        print("❌ Response is not valid JSON!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    return None


# ─────────────────────────────────────────────
# 5. HEADERS & AUTHENTICATION
# ─────────────────────────────────────────────

"""
# Bearer Token Authentication (JWT) — common in backend APIs
headers = {
    "Authorization": "Bearer your_jwt_token_here",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.get(
    "https://api.example.com/users/me",
    headers=headers
)

# API Key Authentication
headers = {"X-API-Key": "your_api_key"}
response = requests.get("https://api.example.com/data", headers=headers)

# Basic Authentication
response = requests.get(
    "https://api.example.com/resource",
    auth=("username", "password")
)
"""


# ─────────────────────────────────────────────
# 6. API CLIENT CLASS — Clean, reusable pattern
# ─────────────────────────────────────────────

class JSONPlaceholderClient:
    """Client for JSONPlaceholder API."""
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self, timeout=10):
        self.timeout = timeout
        self.session = None
    
    def _get_session(self):
        """Lazily create a session (reuse connection)."""
        if self.session is None:
            import requests
            self.session = requests.Session()
            self.session.headers.update({
                "Content-Type": "application/json",
                "Accept": "application/json"
            })
        return self.session
    
    def get_user(self, user_id: int):
        session = self._get_session()
        response = session.get(f"{self.BASE_URL}/users/{user_id}", timeout=self.timeout)
        response.raise_for_status()
        return response.json()
    
    def get_posts(self, user_id=None, limit=10):
        session = self._get_session()
        params = {"_limit": limit}
        if user_id:
            params["userId"] = user_id
        response = session.get(f"{self.BASE_URL}/posts", params=params, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
    
    def create_post(self, title, body, user_id):
        session = self._get_session()
        response = session.post(
            f"{self.BASE_URL}/posts",
            json={"title": title, "body": body, "userId": user_id},
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
    
    def close(self):
        if self.session:
            self.session.close()


# Use the client
try:
    client = JSONPlaceholderClient()
    
    print("\n=== API Client Demo ===")
    user = client.get_user(1)
    print(f"User: {user['name']} from {user['address']['city']}")
    
    posts = client.get_posts(user_id=1, limit=3)
    print(f"\nUser's posts ({len(posts)}):")
    for post in posts:
        print(f"  📄 {post['title'][:45]}...")
    
    new_post = client.create_post("My First API Post", "Content here!", 1)
    print(f"\nCreated post #{new_post['id']}")
    
    client.close()
    
except Exception as e:
    print(f"API demo requires internet: {e}")


# ─────────────────────────────────────────────
# 7. WORKING WITH REAL PUBLIC APIs
# ─────────────────────────────────────────────

PUBLIC_APIS = {
    "JSONPlaceholder":    "https://jsonplaceholder.typicode.com  (fake REST API)",
    "OpenWeatherMap":     "https://openweathermap.org/api  (weather data — needs key)",
    "GitHub API":         "https://api.github.com  (repos, users — free tier)",
    "REST Countries":     "https://restcountries.com  (country information)",
    "CoinGecko":          "https://api.coingecko.com  (crypto prices — free)",
    "NewsAPI":            "https://newsapi.org  (news articles — needs key)",
}

print("\n🌐 Popular Free Public APIs:")
for name, url in PUBLIC_APIS.items():
    print(f"  {name:<20} → {url}")


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Use the REST Countries API to:
#    URL: https://restcountries.com/v3.1/name/{country}
#    - Get info about "India"
#    - Print: name, capital, population, currency

# 2. Use GitHub API to get your repos:
#    URL: https://api.github.com/users/{username}/repos
#    - Print repo name, description, stars, language
#    - Sort by star count

# 3. Create an APIClient class for any public API of your choice.
#    It should have methods that map to the API's endpoints.

# 4. Build a mini weather app (OpenWeatherMap needs free API key):
#    - Ask user for a city name
#    - Fetch and display: temperature, humidity, description

# YOUR CODE HERE:
