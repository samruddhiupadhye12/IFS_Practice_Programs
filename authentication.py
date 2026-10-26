import mysql.connector
import string, bcrypt, random, getpass, re

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Authentication_Users"
)
cursor = db.cursor()

def validate_password(password):
    return (
        len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*?]", password)
    )

def generate_captcha():
    return ''.join(random.choices( string.ascii_letters + string.digits, k=5))

def register():
    username = input("Enter username : ")
    password = getpass.getpass("Enter password : ")

    if not validate_password(password):
        print("**Password must contain : \n")
        print("1 Uppercase, 1 lowercase, 1 digit, 1 speacial character and length of password at least 8 characters!")
        return

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    cursor.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (username, hashed_pw))
    db.commit()

    print("Registration successful!")
    print("Ready to use the application!")

def login():
    username = input("Enter username : ")
    password = getpass.getpass("Enter password : ")

    captcha = generate_captcha()
    print("Captcha : ",captcha)

    captcha_input = input("Enter captcha : ")
    if captcha != captcha_input:
        print("Invalid captcha!")
        return

    cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(password.encode(), user[0]):
        print("logged in successfully.!")
        print("Ready to use the application!")
    else:
        print("Invalid username or password!")

while True:
    print("\n1.Register")
    print("2.Login")
    print("3.Exit")
    choice = input("Enter choice : ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")