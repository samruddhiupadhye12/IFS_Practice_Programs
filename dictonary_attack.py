import getpass
common_password = ["admin", "qwerty", "password", "12345", "welcome", "hello"]
password = getpass.getpass("Enter password : ")
if password in common_password:
    print("Password found in common password list that is used by hackers!")
    print("Your password is too weak and can get easily hacked!")
else:
    print("Your password is unique!")
    print("Password always should be unique, long and non-hackable!")
