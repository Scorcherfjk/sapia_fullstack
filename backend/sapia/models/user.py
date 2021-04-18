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

    def __init__(self, id, name, lastname, phone_number, email, password, date_of_birth, headquarter=None, program=None, bio=None):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.email = email
        self.password = password
        self.headquarter = headquarter
        self.program = program
        self.bio = bio

    @classmethod
    def short(cls, id, email, password):
        return cls(id, None, None, None, email, password, None)

    @classmethod
    def from_query(cls, data):
        return cls(
            str(data['_id']),
            data['name'],
            data['lastname'],
            data['phone_number'],
            data['email'],
            str(data['password']),
            data['date_of_birth'],
            data['headquarter'],
            data['program'],
            data['bio'],
        )

    def __str__(self):
        return self.id

    def toDictSave(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "lastname": self.lastname,
            "phone_number": self.phone_number,
            "date_of_birth": self.date_of_birth,
            "bio": self.bio,
            "headquarter": self.headquarter,
            "program": self.program
        }
    
    def toDictRespose(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname,
            "phone_number": self.phone_number,
            "date_of_birth": self.date_of_birth.strftime('%Y-%m-%d'),
            "bio": self.bio,
            "headquarter": self.headquarter,
            "program": self.program
        }
