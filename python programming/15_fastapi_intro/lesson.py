# ============================================================
# LESSON 15: Introduction to FastAPI — Your First Backend API
# ============================================================
# 🎯 Goal: Build a real REST API with FastAPI
#
# SETUP (run these in terminal first):
#   python -m venv venv
#   venv\Scripts\activate          (Windows)
#   pip install fastapi uvicorn[standard] pydantic
#
# RUN THE SERVER:
#   uvicorn lesson:app --reload
#
# VISIT:
#   http://localhost:8000           → API root
#   http://localhost:8000/docs      → Swagger UI (interactive!)
#   http://localhost:8000/redoc     → ReDoc documentation

from fastapi import FastAPI, HTTPException, Query, Path, status
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, List
from datetime import datetime

# ─────────────────────────────────────────────
# 1. CREATE THE APP
# ─────────────────────────────────────────────

app = FastAPI(
    title="📚 Python Learners API",
    description="A complete REST API built while learning Python backend development!",
    version="1.0.0",
)


# ─────────────────────────────────────────────
# 2. PYDANTIC MODELS — Data validation & schemas
# ─────────────────────────────────────────────

class UserCreate(BaseModel):
    """Schema for creating a new user."""
    name: str
    email: str
    role: str = "user"          # default value
    age: Optional[int] = None
    
    @field_validator("name")
    @classmethod
    def name_must_be_valid(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        return v.strip().title()
    
    @field_validator("role")
    @classmethod
    def role_must_be_valid(cls, v):
        allowed = ["user", "admin", "editor", "moderator"]
        if v not in allowed:
            raise ValueError(f"Role must be one of: {allowed}")
        return v


class UserResponse(BaseModel):
    """Schema for returning user data."""
    id: int
    name: str
    email: str
    role: str
    age: Optional[int]
    created_at: str


class UserUpdate(BaseModel):
    """Schema for updating user data — all fields optional."""
    name: Optional[str] = None
    role: Optional[str] = None
    age: Optional[int] = None


class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    author_name: str
    created_at: str


# ─────────────────────────────────────────────
# 3. IN-MEMORY DATABASE (for learning — later use SQLAlchemy!)
# ─────────────────────────────────────────────

# These act as our "database" tables
users_db: dict[int, dict] = {}
posts_db: dict[int, dict] = {}
user_id_counter = 1
post_id_counter = 1

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Seed some initial data
def seed_data():
    global user_id_counter, post_id_counter
    
    initial_users = [
        {"name": "Alice Smith",   "email": "alice@example.com",   "role": "admin",  "age": 28},
        {"name": "Bob Johnson",   "email": "bob@example.com",     "role": "editor", "age": 32},
        {"name": "Charlie Brown", "email": "charlie@example.com", "role": "user",   "age": 25},
    ]
    
    for u in initial_users:
        users_db[user_id_counter] = {**u, "id": user_id_counter, "created_at": now()}
        user_id_counter += 1
    
    initial_posts = [
        {"user_id": 1, "title": "Welcome to My Blog!",         "content": "Hello World!"},
        {"user_id": 1, "title": "Python is Amazing",            "content": "Here's why..."},
        {"user_id": 2, "title": "FastAPI Tutorial for Beginners", "content": "Let's build an API!"},
    ]
    
    for p in initial_posts:
        posts_db[post_id_counter] = {**p, "id": post_id_counter, "created_at": now()}
        post_id_counter += 1

seed_data()


# ─────────────────────────────────────────────
# 4. ROOT & HEALTH CHECK ROUTES
# ─────────────────────────────────────────────

@app.get("/", tags=["General"])
def root():
    """Welcome endpoint."""
    return {
        "message": "🐍 Python Learners API",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health", tags=["General"])
def health_check():
    """Check if the API is running."""
    return {
        "status": "healthy",
        "timestamp": now(),
        "total_users": len(users_db),
        "total_posts": len(posts_db),
    }


# ─────────────────────────────────────────────
# 5. USER ROUTES — Full CRUD
# ─────────────────────────────────────────────

@app.get("/users", response_model=List[UserResponse], tags=["Users"])
def get_all_users(
    role: Optional[str] = Query(None, description="Filter by role"),
    limit: int = Query(10, ge=1, le=100, description="Max results"),
    offset: int = Query(0, ge=0, description="Skip first N results"),
    search: Optional[str] = Query(None, description="Search by name or email"),
):
    """
    Get all users.
    
    - **role**: Filter by user role
    - **limit**: Number of results (max 100)
    - **offset**: Skip N results (for pagination)
    - **search**: Search by name or email
    """
    result = list(users_db.values())
    
    # Apply filters
    if role:
        result = [u for u in result if u["role"] == role]
    
    if search:
        query = search.lower()
        result = [u for u in result if query in u["name"].lower() or query in u["email"].lower()]
    
    # Pagination
    total = len(result)
    result = result[offset:offset + limit]
    
    return result


@app.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def get_user(
    user_id: int = Path(..., ge=1, description="The user ID")
):
    """Get a specific user by ID."""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found."
        )
    return users_db[user_id]


@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: UserCreate):
    """
    Create a new user.
    
    - **name**: Full name (min 2 characters)
    - **email**: Valid email address (must be unique)
    - **role**: user, admin, editor, or moderator
    - **age**: Optional age
    """
    global user_id_counter
    
    # Check for duplicate email
    existing_emails = [u["email"].lower() for u in users_db.values()]
    if user.email.lower() in existing_emails:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Email '{user.email}' is already registered."
        )
    
    new_user = {
        "id": user_id_counter,
        "name": user.name,
        "email": user.email.lower(),
        "role": user.role,
        "age": user.age,
        "created_at": now()
    }
    
    users_db[user_id_counter] = new_user
    user_id_counter += 1
    
    return new_user


@app.put("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def update_user(
    user_id: int,
    updates: UserUpdate
):
    """Update user details. Only provided fields are updated."""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found."
        )
    
    user = users_db[user_id]
    
    # Only update provided fields
    if updates.name is not None:
        user["name"] = updates.name.strip().title()
    if updates.role is not None:
        allowed = ["user", "admin", "editor", "moderator"]
        if updates.role not in allowed:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Role must be one of: {allowed}"
            )
        user["role"] = updates.role
    if updates.age is not None:
        user["age"] = updates.age
    
    users_db[user_id] = user
    return user


@app.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int):
    """Delete a user and all their posts."""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found."
        )
    
    # Delete user's posts
    posts_to_delete = [pid for pid, p in posts_db.items() if p["user_id"] == user_id]
    for pid in posts_to_delete:
        del posts_db[pid]
    
    deleted_user = users_db.pop(user_id)
    
    return {
        "message": f"User '{deleted_user['name']}' and {len(posts_to_delete)} post(s) deleted.",
        "deleted_user_id": user_id
    }


# ─────────────────────────────────────────────
# 6. POST ROUTES
# ─────────────────────────────────────────────

@app.get("/posts", tags=["Posts"])
def get_all_posts(
    user_id: Optional[int] = Query(None, description="Filter by author"),
    limit: int = Query(10, ge=1, le=50)
):
    """Get all posts, optionally filtered by author."""
    posts = list(posts_db.values())
    
    if user_id:
        posts = [p for p in posts if p["user_id"] == user_id]
    
    # Enrich with author name
    enriched = []
    for post in posts[:limit]:
        author = users_db.get(post["user_id"], {})
        enriched.append({
            **post,
            "author_name": author.get("name", "Unknown")
        })
    
    return enriched


@app.post("/posts", status_code=status.HTTP_201_CREATED, tags=["Posts"])
def create_post(post: PostCreate):
    """Create a new post."""
    global post_id_counter
    
    if post.user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {post.user_id} not found."
        )
    
    new_post = {
        "id": post_id_counter,
        "user_id": post.user_id,
        "title": post.title,
        "content": post.content,
        "created_at": now()
    }
    
    posts_db[post_id_counter] = new_post
    post_id_counter += 1
    
    return new_post


@app.delete("/posts/{post_id}", tags=["Posts"])
def delete_post(post_id: int):
    """Delete a post."""
    if post_id not in posts_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {post_id} not found."
        )
    deleted = posts_db.pop(post_id)
    return {"message": f"Post '{deleted['title']}' deleted successfully."}


# ─────────────────────────────────────────────
# 7. STATISTICS ROUTE
# ─────────────────────────────────────────────

@app.get("/stats", tags=["General"])
def get_stats():
    """Get API statistics."""
    role_counts = {}
    for user in users_db.values():
        role = user["role"]
        role_counts[role] = role_counts.get(role, 0) + 1
    
    posts_per_user = {}
    for post in posts_db.values():
        uid = post["user_id"]
        name = users_db.get(uid, {}).get("name", "Unknown")
        posts_per_user[name] = posts_per_user.get(name, 0) + 1
    
    return {
        "total_users": len(users_db),
        "total_posts": len(posts_db),
        "users_by_role": role_counts,
        "posts_by_author": posts_per_user,
        "server_time": now(),
    }


# ─────────────────────────────────────────────
# RUN INSTRUCTIONS
# ─────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Python Learners API...")
    print("📖 Swagger UI: http://localhost:8000/docs")
    print("📊 Stats:       http://localhost:8000/stats")
    uvicorn.run("lesson:app", host="0.0.0.0", port=8000, reload=True)
