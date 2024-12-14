##### Imports #####
import base64, hashlib, os
from cryptography.fernet import Fernet
from utils import askTag, askMasterPassword

##### Functions #####

def verifyExistingMasterPassword() -> bool:
    try:
        with open("masterPassword.txt", "r") as file:
            return True
    except FileNotFoundError:
        return False
    
def getMasterPassword() -> str:
    try:
        with open("masterPassword.txt", "r") as file:
            return file.read()
    except Exception as e:
        print("Error reading master password.")
        print(e)

def defineMasterPassword() -> None:
    masterPassword = askMasterPassword()
    try:
        hashedPassword = hashlib.sha256(masterPassword.encode()).hexdigest()
        with open("masterPassword.txt", "w") as file:
            file.write(hashedPassword)
    except Exception as e:
        print("Error writing master password.")
        print(e)

def encryptPassword(master_password: str, tag: str) -> str:

    combined = f"{master_password}{tag}"
    random_bytes = os.urandom(16) 
    combined_with_nonce = combined.encode() + random_bytes
    hash_object = hashlib.sha256(combined_with_nonce)
    hashed_password = base64.urlsafe_b64encode(hash_object.digest()).decode('utf-8')
    return hashed_password

def truncatePassword(password: str, size : int) -> str:    
    return password[:size]

