import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username must contain only normal letters a-z")

        if len(username) < 3:
            raise UserInputError("Minimum length of username is 3 characters")
        
        if len(password) < 8:
            raise UserInputError("Minimum length of password is 8 characters")

        if re.match("[a-z]+$", password):
            raise UserInputError("Password cannot contain only normal letters a-z")
