"""Handles adding a new user to database
"""

from werkzeug.security import generate_password_hash
from sqlalchemy import text, exc
from src.utils.database import db

def insert_new_user(username, password):
    """Inserts a new user into database"""
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password)"
               " VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        return True
    except exc.IntegrityError:
        return False
