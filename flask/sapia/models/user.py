import hashlib
from datetime import datetime


class User(object):

    name = 'test'
    lastname = 'test'
    date_of_birth = None
    bio = ''

    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    def __str__(self):
        return f"the user is {self.email}"

    def toDict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "lastname": self.lastname,
            "date_of_birth": self.date_of_birth,
            "bio": self.bio,
        }
