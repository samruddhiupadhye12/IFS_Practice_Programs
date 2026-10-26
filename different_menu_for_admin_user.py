import getpass

username = input("Enter username : ")
password = getpass.getpass("Enter password : ")

if username == "admin" and password == "admin@1":
    print("Logged in successfully")
    print("\n---Admin Menu---")
    print("1.Add user")
    print("2.Delete user")
    print("3.View Reports")

elif username == "user" and password == "user@2":
    print("Logged in successfully")
    print("\n---User Menu---")
    print("1.View profile")
    print("2.Change password")
    print("3.Logout")

else:
    print("Invalid username or password!")