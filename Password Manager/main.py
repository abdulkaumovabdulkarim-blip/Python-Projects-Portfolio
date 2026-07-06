# main.py
# PYTHON PROJECTS - "Password Manager"

# Abdulqayumov Abdukarim


import os
from cryptography.fernet import Fernet
import json

# File data
KEY_FILE = "KEY_FILE.txt"
DATA_FILE = "data.json"

# Main menu function
def main_menu():
    # Menu
    print("\n--- Choose an action ---")
    print("1. View passwrods")
    print("2. Add a password")
    print("3. Search for a passwrod")
    print("0. Exit")
    choice = input("Enter your choice: ")
    # Check is it digit
    try: 
        choice = int(choice)
    except Exception as e:
        print("\n[Error]: Invalid Choice! Try again")
        return main_menu()
    else:
        if choice < 0 or choice > 3:
            print("\n[Error]: Choice has to be between 0 and 3! Try again")
            return main_menu()  

    return choice

# Load or Create the key
def load_or_create_key():

    # if no file with key, then create it 
    if not os.path.exists(KEY_FILE):
        new_key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(new_key)

    try:
        # if file is empty, throw an error
        if os.path.getsize(KEY_FILE) == 0:
            return "Error"
        else:
            # Get key from file
            with open(KEY_FILE, "rb") as f:
                return f.read()
    except Exception as e:
        print(e)

# View function
def view_passwords(key):
    # If no file or it is empty
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        print("\nNo saved passwords yet!")
        return
    else:
        # Open file and get all data from it
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Count for number of accounts
        count = 1

        # for loop to go throw all websites
        for account, info in data.items():
            user = info["User"]
            password_encrypted = info["Password"]
            
            password_decrypted = key.decrypt(password_encrypted.encode('utf-8')).decode('utf-8')
            print(f'{count}. {account} | User: {user} | Password: {password_decrypted}')
            count += 1

# Add password function
def add_passwords(key):
    passwords_file = os.path.realpath(DATA_FILE)

    account = input("Accout: ")
    user = input("User: ")
    password = input("Password: ")
    
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) != 0:
        with open(passwords_file, "r") as f:
            data = json.load(f)
    else:
        data = {}

    encrypted_password = key.encrypt(password.encode('utf-8')).decode('utf-8')


    data[str(account)] = {
        "User": str(user),
        "Password": str(encrypted_password)
    }

    with open(passwords_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print('\n[Entry Saved and Encrypted]')

    

# Search function
def search_passwords(key):
    password_file = os.path.realpath(DATA_FILE)
    found = False
    account = input('Enter name of account(website name): ')

    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        print("\nNo saved passwords yet!")
        return
    else:
        with open(password_file, "r") as f:
            data = json.load(f)
        
        for i in data:
            if i == account:
                found = True
                break

        if found == True:
            password = data[account]["Password"]
            password_bytes = password.encode('utf-8')
            password_decrypted = key.decrypt(password_bytes).decode('utf-8')
            print(f"\n[Result]: {account} | User: {data[account]["User"]} | Password: {password_decrypted}")
        else:
            print("\n[Error]: No password and user with such an account!")
            return




# PROGRAMM ENTERANCE PASSWORD
enterance_password = "Py_0011!"

print("--- Secure Password Vault ---\n")


# --- START ---
# System Enterance check
while(True):
    master_password = input('Enter Master Password: ')

    if master_password == 'Py_0011!':
        print('\nAuthentication Successful.')
        break
    else:
        print("\n[Error]: Wrong master password! Try again please\n")
        continue

# Main System loop
exit=True
while(exit==True):

    # Get key
    key = load_or_create_key()
    if key == "Error":
        print('[Error]: KEY_FILE is empty!')
        break
    suit = Fernet(key)
    # Main Menu
    menu_choice = main_menu()

    if menu_choice == 1:
        view_passwords(suit)
    elif menu_choice == 2:
        add_passwords(suit)
    elif menu_choice == 3:
        search_passwords(suit)
    elif menu_choice == 0:
        print("\nThank you for using Master Password!")
        break