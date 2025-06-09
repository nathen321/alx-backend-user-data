#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User ${user.email} already exists")
        else:
            hash = _hash_password(password)
            return self._db.add_user(
                email=email, hashed_password=hash.decode('utf-8'))


def _hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
