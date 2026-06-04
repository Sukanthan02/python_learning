# ============================================================
# LESSON 14: Database Basics — SQLite with Python
# ============================================================
# 🎯 Goal: Store data permanently using SQL databases
# sqlite3 is built-in — no installation needed!

import sqlite3
import os
from datetime import datetime

DB_FILE = "lesson14.db"

# ─────────────────────────────────────────────
# 1. CONNECTING TO SQLITE
# ─────────────────────────────────────────────

# Connect (creates file if it doesn't exist)
conn = sqlite3.connect(DB_FILE)
conn.row_factory = sqlite3.Row    # Makes rows act like dicts!
cursor = conn.cursor()
print("✅ Database connected!")


# ─────────────────────────────────────────────
# 2. CREATING TABLES
# ─────────────────────────────────────────────

cursor.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name        TEXT    NOT NULL,
        email       TEXT    NOT NULL UNIQUE,
        role        TEXT    NOT NULL DEFAULT 'user',
        created_at  TEXT    NOT NULL
    );
    
    CREATE TABLE IF NOT EXISTS posts (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id     INTEGER NOT NULL,
        title       TEXT    NOT NULL,
        content     TEXT,
        created_at  TEXT    NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
""")
conn.commit()
print("✅ Tables created!")


# ─────────────────────────────────────────────
# 3. INSERTING DATA
# ─────────────────────────────────────────────

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Insert one row — use ? placeholders (NEVER use f-strings for SQL!)
cursor.execute(
    "INSERT OR IGNORE INTO users (name, email, role, created_at) VALUES (?, ?, ?, ?)",
    ("Alice", "alice@example.com", "admin", now())
)

# Insert multiple rows at once
users_data = [
    ("Bob",     "bob@example.com",     "user",  now()),
    ("Charlie", "charlie@example.com", "user",  now()),
    ("Diana",   "diana@example.com",   "editor",now()),
    ("Eve",     "eve@example.com",     "user",  now()),
]
cursor.executemany(
    "INSERT OR IGNORE INTO users (name, email, role, created_at) VALUES (?, ?, ?, ?)",
    users_data
)
conn.commit()
print("✅ Users inserted!")

# Insert posts
posts_data = [
    (1, "Python Basics",        "Learn Python from scratch.",   now()),
    (1, "FastAPI Tutorial",     "Build APIs with FastAPI.",     now()),
    (2, "SQL for Beginners",    "Master SQL in 30 days.",       now()),
    (3, "My Learning Journey",  "My experience with Python.",   now()),
]
cursor.executemany(
    "INSERT OR IGNORE INTO posts (user_id, title, content, created_at) VALUES (?, ?, ?, ?)",
    posts_data
)
conn.commit()
print("✅ Posts inserted!")


# ─────────────────────────────────────────────
# 4. QUERYING DATA — SELECT
# ─────────────────────────────────────────────

print("\n" + "="*50)
print("ALL USERS:")
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

for user in users:
    print(f"  [{user['id']}] {user['name']:<10} | {user['email']:<25} | {user['role']}")


# Fetch single row
cursor.execute("SELECT * FROM users WHERE email = ?", ("alice@example.com",))
alice = cursor.fetchone()
print(f"\nFound user: {alice['name']} (role: {alice['role']})")


# Filter, sort, limit
print("\nNon-admin users (sorted by name):")
cursor.execute("""
    SELECT id, name, email
    FROM users
    WHERE role != 'admin'
    ORDER BY name ASC
    LIMIT 3
""")
for row in cursor.fetchall():
    print(f"  {row['id']}. {row['name']} — {row['email']}")


# ─────────────────────────────────────────────
# 5. JOIN — Combine related tables
# ─────────────────────────────────────────────

print("\nPosts with Author Names (JOIN):")
cursor.execute("""
    SELECT 
        posts.id,
        posts.title,
        users.name  AS author,
        posts.created_at
    FROM posts
    INNER JOIN users ON posts.user_id = users.id
    ORDER BY posts.id
""")

for row in cursor.fetchall():
    print(f"  [{row['id']}] '{row['title']}' by {row['author']}")


# ─────────────────────────────────────────────
# 6. AGGREGATE FUNCTIONS
# ─────────────────────────────────────────────

print("\nPost count per user:")
cursor.execute("""
    SELECT 
        users.name,
        COUNT(posts.id) AS post_count
    FROM users
    LEFT JOIN posts ON users.id = posts.user_id
    GROUP BY users.id
    ORDER BY post_count DESC
""")

for row in cursor.fetchall():
    print(f"  {row['name']:<10}: {row['post_count']} post(s)")


cursor.execute("SELECT COUNT(*) as total, AVG(id) as avg_id FROM users")
stats = cursor.fetchone()
print(f"\nTotal users: {stats['total']}, Avg ID: {stats['avg_id']:.1f}")


# ─────────────────────────────────────────────
# 7. UPDATE & DELETE
# ─────────────────────────────────────────────

# Update
cursor.execute(
    "UPDATE users SET role = ? WHERE email = ?",
    ("moderator", "bob@example.com")
)
conn.commit()
print(f"\n✅ Updated {cursor.rowcount} user(s)")

# Verify update
cursor.execute("SELECT name, role FROM users WHERE email = ?", ("bob@example.com",))
bob = cursor.fetchone()
print(f"Bob's new role: {bob['role']}")

# Delete
cursor.execute("DELETE FROM posts WHERE user_id = ?", (99,))  # Safe — no rows match
conn.commit()
print(f"Deleted {cursor.rowcount} row(s)")


# ─────────────────────────────────────────────
# 8. DATABASE CLASS — Clean OOP pattern
# ─────────────────────────────────────────────

class UserRepository:
    """Repository pattern for User database operations."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
    
    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    
    def create(self, name: str, email: str, role: str = "user") -> dict:
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO users (name, email, role, created_at) VALUES (?, ?, ?, ?)",
                (name, email, role, now())
            )
            conn.commit()
            return self.get_by_id(cursor.lastrowid)
    
    def get_by_id(self, user_id: int) -> dict | None:
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
            return dict(row) if row else None
    
    def get_all(self, role: str = None) -> list:
        with self._connect() as conn:
            if role:
                rows = conn.execute("SELECT * FROM users WHERE role = ?", (role,)).fetchall()
            else:
                rows = conn.execute("SELECT * FROM users ORDER BY id").fetchall()
            return [dict(r) for r in rows]
    
    def update_role(self, user_id: int, new_role: str) -> bool:
        with self._connect() as conn:
            cursor = conn.execute(
                "UPDATE users SET role = ? WHERE id = ?", (new_role, user_id)
            )
            conn.commit()
            return cursor.rowcount > 0
    
    def delete(self, user_id: int) -> bool:
        with self._connect() as conn:
            cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def search(self, query: str) -> list:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM users WHERE name LIKE ? OR email LIKE ?",
                (f"%{query}%", f"%{query}%")
            ).fetchall()
            return [dict(r) for r in rows]


print("\n" + "="*50)
print("UserRepository Demo:")
repo = UserRepository(DB_FILE)

all_users = repo.get_all()
print(f"Total users: {len(all_users)}")

admins = repo.get_all(role="admin")
print(f"Admins: {[u['name'] for u in admins]}")

results = repo.search("al")
print(f"Search 'al': {[u['name'] for u in results]}")


# ─────────────────────────────────────────────
# 9. SQL CHEAT SHEET
# ─────────────────────────────────────────────

SQL_CHEATSHEET = """
SQL QUICK REFERENCE:
═══════════════════════════════════════════════
SELECT * FROM users;                          -- all columns
SELECT name, email FROM users;               -- specific columns
SELECT * FROM users WHERE role = 'admin';    -- filter
SELECT * FROM users ORDER BY name ASC;       -- sort
SELECT * FROM users LIMIT 10 OFFSET 20;     -- pagination
SELECT * FROM users WHERE name LIKE '%ali%'; -- partial match

INSERT INTO users (name, email) VALUES ('Bob', 'bob@x.com');
UPDATE users SET role = 'admin' WHERE id = 1;
DELETE FROM users WHERE id = 99;

SELECT COUNT(*) FROM users;                  -- count rows
SELECT AVG(score), MAX(score) FROM data;    -- aggregates
SELECT u.name, COUNT(p.id) FROM users u
  LEFT JOIN posts p ON u.id = p.user_id
  GROUP BY u.id
  HAVING COUNT(p.id) > 1;                   -- group + filter
═══════════════════════════════════════════════
"""
print(SQL_CHEATSHEET)


# Cleanup
conn.close()
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
print("🧹 Database cleaned up.")


# ============================================================
# ✏️  EXERCISES
# ============================================================
# 1. Create a "todo_app.db" with a "todos" table:
#    Columns: id, title, description, completed (0/1), created_at
#    Write functions: add_todo(), get_todos(), complete_todo(), delete_todo()

# 2. Create a "library.db" with books and members tables.
#    Add a borrows table linking them.
#    Write SQL to find: which books are currently borrowed and by whom.

# 3. Add pagination to UserRepository:
#    get_all(page=1, per_page=10) → returns items for that page

# YOUR CODE HERE:
