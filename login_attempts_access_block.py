import getpass

stored_username = "Admin"
stored_password = "Admin@123"

attempts = 3

while attempts > 0:
    username = input("Enter username : ")
    password = getpass.getpass("Enter password : ")

    if username == stored_username and password == stored_password:
        print("Logged in successfully!")
        break
    else:
        attempts = attempts - 1

        if attempts > 0:
            print(f"Invalid username or password. {attempts} attempt(s) left.")
        else:
            print("Too many failed attempts. Access blocked and Account Locked!")