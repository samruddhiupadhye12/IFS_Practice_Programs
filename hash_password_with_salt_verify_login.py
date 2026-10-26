import os, hashlib, getpass

password = getpass.getpass("Enter password : ")
salt = os.urandom(16)
hash_pass = hashlib.sha256(salt+password.encode('utf-8')).hexdigest()
# print("Salt : ",salt.hex())
print("Hash password : ",hash_pass)
print("Password stored successfully!")

login_password = getpass.getpass("Enter password for login : ")
login_hash = hashlib.sha256(salt+login_password.encode('utf-8')).hexdigest()

if login_hash == hash_pass:
    print("Logged in successfully!")
else:
    print("Log in failed!")