def printMenu() -> None:
    print("###################################################################")
    print("Here is the menu:")
    print("1 - Change master password.")
    print("2 - Generate a random password.")
    print("3 - Generate a password from your master password and your tag.")
    print("4 - Leave.")
    print("###################################################################\n")


def getChoice() -> int:
    return int(input("Please, enter your choice: "))

def askTag() -> str:
    return input("Please, enter your tag: ")

def askMasterPassword() -> str:
    return input("Please,  enter your master password: ")

def askSize() -> int:
    return int(input("Please, enter the desired password size: "))