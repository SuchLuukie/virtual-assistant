# Import libraries
import hashlib
import string
import random
import json
import time

class Encryption:
    def __init__(self):
        self.chars = list(string.printable)[:-6]
        self.salt_length = 32
        self.hash_iterations = 500

    # Function to compare a given password to one in the database
    def compare_password(self, uuid, password):
        db = json.load(open("authentication/users.json"))

        salt = self.get_salt(uuid)
        salted_password = self.merge_salt_and_password(password, salt)
        hashed_password = self.hash_password(salted_password)

        db_password = db[uuid]["password"]
        if hashed_password == db_password:
            return True
        return False


    # Function to hash password
    def hash_password(self, salted_password):
        for i in range(945032):
            encoded_password = salted_password.encode("utf8")
            hashed_password = hashlib.sha512(encoded_password).hexdigest()
            salted_password = hashed_password

        return hashed_password

    
    # Function to get salt
    def get_salt(self, uuid):
        return json.load(open("authentication/salts.json"))[uuid]


    # Function to merge salt and password for future hashing
    def merge_salt_and_password(self, password, salt):
        middle_index = int(len(salt) / 2)
        return salt[:middle_index] + password + salt[middle_index:]

    
    # Function to generate a randomized string of characters
    def generate_salt(self):
        salt = ""
        for i in range(self.salt_length):
            salt += random.choice(self.chars)
        return salt


    # Function to store salt in database by UUID
    def store_salt(self, uuid, salt):
        with open("salts.json", "r+") as file:
            data = json.load(file)
            data.update({uuid: salt})
            json.dump(data, file)

Encryption()