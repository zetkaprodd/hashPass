##### Imports #####
from hashlib import sha256

##### Functions #####


def verifyExistingMasterPassword():
    try:
        with open("master_password.txt", "r") as file:
            return True
    except FileNotFoundError:
        return False
    
def getMasterPassword():
    try:
        with open("master_password.txt", "r") as file:
            return file.read()
    except Exception as e:
        print("Erreur lors de la lecture du mot de passe maître.")
        print(e)

def defineMasterPassword():
    master_password = input("Entrez le nouveau mot de passe maître: ")
    try:
        with open("master_password.txt", "w") as file:
            file.write(sha256(master_password.encode()).hexdigest())
    except Exception as e:
        print("Erreur lors de l'écriture du mot de passe maître.")
        print(e)
    