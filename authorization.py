import mysql.connector
import bcrypt, getpass

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="DemoDB"
)
cursor = db.cursor()

username = input("Enter username : ")
password = getpass.getpass("Enter password : ")

cursor.execute("SELECT password,permissions FROM user WHERE username=%s", (username,))
user = cursor.fetchone()

if user and bcrypt.checkpw(password.encode(), user[0]):
    print("Logged in successfully!")

    action = input("Action(read/write/execute) : ").lower()
    permission = user[1].split(",")

    if action in permission:
        if action == "read":
            with open("Demo.txt", "r") as f:
                print("\nFile Contennt : \n")
                print(f.read())
        elif action == "write":
            data = input("Enter data : ")
            with open("Demo.txt", "a") as f:
                f.write("\n" + data + "\n")
            print("Data written successfully!")
        elif action == "execute":
            print("Executing file opeartion.!(Simulation)")
    else:
        print("Permission Denied")

else:
    print("Authentication Failed.!")


db.close()