import hashlib
from django.conf import settings
SALT_KEY = "somerandomsaltkey--"


def hash_raw_password(password: str) -> str:
    hash_object = hashlib.sha256()
    hash_object.update(SALT_KEY.encode())
    hash_object.update(password.encode())
    hashed_password = hash_object.hexdigest()
    return hashed_password


def check_password(raw_password: str, hashed_password: str) -> bool:
    hashed_input_password = hash_raw_password(raw_password)
    return hashed_input_password == hashed_password