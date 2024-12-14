from hashingUtils import *
from utils import printMenu, getChoice, askTag
from randomPassword import *

import os


def main():
    
    choice : int = 0
    masterPassword : str = ""

    os.system("cls")

    while(True):

        printMenu()
        choice = getChoice()

        if choice == 1:
            defineMasterPassword()
        
        elif choice == 2:
            generateRandomPassword()
        
        elif choice == 3:
            if not(verifyExistingMasterPassword()):
                defineMasterPassword()

            tag = askTag()
            masterPassword = getMasterPassword()
            size = getSize()

            finalPwd = encryptPassword(masterPassword, tag)
            finalPwd = truncatePassword(finalPwd, size)

            print(f"\nGenerated password: {finalPwd}")

        elif choice == 4:
            os.system("cls")
            print("Thanks for using my password generator, goodbye !")
            break

        else:
            print("Invalid choice.")
            continue


if __name__ == "__main__":
    main()