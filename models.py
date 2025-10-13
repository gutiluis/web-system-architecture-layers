#!/bin/env python
from db import get_db_connection
from errors import DatabaseError

def create_user(name, email):
    """Insert a new user into the database."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users(name,email) VALUES (?, ?)", 
                (name, email)
            )
    except Exception as e:
        raise DatabaseError(f"Failed to insert user: {e}")

def get_users():
    """Fetch all users."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email FROM users")
            return cursor.fetchall()
    except Exception as e:
        raise DatabaseError(f"Failed to fetch users: {e}")

