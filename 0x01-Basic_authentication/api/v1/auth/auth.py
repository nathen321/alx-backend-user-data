#!/usr/bin/env python3
"""  manage the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None or excluded_paths is None or len(excluded_paths) <= 0:
            return True
        normalized_path = path if path.endswith('/') else path + '/'

        if normalized_path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None
        auth_token = request.headers.get('Authorization')
        if auth_token:
            return auth_token
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
