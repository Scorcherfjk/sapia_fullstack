import hashlib
from datetime import datetime


class User(object):

    name = None
    lastname = None
    phone_number = None
    date_of_birth = None
    bio = None
    id = None
    email = None
    password = None
    headquarter = None
    program = None

    def __init__(self, id, name, lastname, phone_number, email, password, date_of_birth, headquarter=None, program=None):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.email = email
        self.password = password
        self.headquarter = headquarter
        self.program = program

    @classmethod
    def short(cls, id, email, password):
        return cls(id, None, None, None, email, password, None)

    def __str__(self):
        return self.id

    def toDict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "lastname": self.lastname,
            "phone_number": self.phone_number,
            "date_of_birth": self.date_of_birth,
            "bio": self.bio,
        }
