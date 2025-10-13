#!/bin/env python

from models import create_user, get_users
from errors import ValidationError

def add_user_service(name, email):
    """Validate input and call DB layer."""
    if not name or not email:
        raise ValidationError("Name and email are required")
    create_user(name, email)
    return {"status": "success"}

def list_users_service():
    """Return a list of all users."""
    rows = get_users()
    return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]

