# FastAPI Backend Architecture & Learning Guide

Welcome to Python Backend Development! This repository is configured with a modern, production-ready, clean-architecture template using **FastAPI**, **SQLAlchemy**, **MySQL**, **Redis**, **Celery**, **Alembic**, and **Docker**.

## 🛠️ Tech Stack Overview
- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python.
- **SQLAlchemy (v2.0)**: Object-Relational Mapping (ORM) library to write MySQL database queries in standard Python classes.
- **Pydantic (v2.0)**: Data validation and settings management.
- **Celery & Redis**: Background task runner and memory queue to run asynchronous processes.
- **Alembic**: Database schema migration manager.
- **Docker & Compose**: Container orchestration for development and production setup.

## 📁 Repository Structure
- `app/main.py`: Main entrypoint of the application.
- `app/core/`: Contains base infrastructure configuration (`config.py`, `database.py`, `security.py`, `redis.py`, `celery_app.py`).
- `app/models/`: SQLAlchemy ORM database models.
- `app/schemas/`: Pydantic models for validation and serialization.
- `app/crud/`: Clean Database Access Object (DAO) helpers.
- `app/api/`: Routing, endpoints (v1), and dependency injection (`deps.py`).
- `app/worker/`: Celery asynchronous worker tasks.

## 🚀 Running the App
The best way to run the entire backend stack is via Docker:
```bash
docker-compose up --build
```
This automatically boots up:
1. MySQL database (Port `3306`)
2. Redis cache/broker (Port `6379`)
3. FastAPI Server (Port `8000`)
4. Celery background worker

Once started, visit:
- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
