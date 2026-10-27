import getpass
password = getpass.getpass("Enter password : ")
common_password = ["qwerty", "12345", "password", "admin", "hello", "bye", "welcome", "1234567890"]
for pw in common_password:
    print("Trying : ",pw)
    if pw == password:
        print("Password cracked:", pw)
        print(f" '{password}' present in the common password list.")
        break
else:
    print("Password not found!")