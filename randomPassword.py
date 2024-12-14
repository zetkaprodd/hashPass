import random
import string

# Variables
lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
numbers = string.digits
specialCharacters = string.punctuation

# Functions

def generateRandomPassword() -> None:
    size = getSize()
    characters = getCharacters()
    password = "".join(random.choice(characters) for i in range(size))
    print("\nRandom password : \n", password)

def getSize() -> int:
    return int(input("Please enter the desired password size : "))

def getCharacters() -> str:
    characters = ""
    options = [
        ("Do you want to include lowercase letters ? (y/n) : ", lowerLetters),
        ("Do you want to include uppercase letters ? (y/n) : ", upperLetters),
        ("Do you want to include digits ? (y/n) : ", numbers),
        ("Do you want to include special characters ? (y/n) : ", specialCharacters)
    ]
    
    for prompt, charSet in options:
        choice = ""
        while choice != "y" and choice != "n":
            choice = input(prompt)
        if choice == "y":
            characters += charSet
    
    return characters
  