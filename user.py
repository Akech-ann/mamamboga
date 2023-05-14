import hashlib
import datetime

class User:
    def __init__(self, name, email, password, phone_number, address):
        self.name = name
        self.email = email
        self.password = self._hash_password(password)
        self.phone_number = phone_number
        self.address = address
        
    def _hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    def change_password(self, new_password):
        self.password = self._hash_password(new_password)
    
    def update_profile(self, name=None, email=None, phone_number=None, address=None):
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number
        if address is not None:
            self.address = address
        
    def get_user_info(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "created_at": self.created_at
        }

