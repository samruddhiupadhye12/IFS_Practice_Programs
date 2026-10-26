import hashlib, getpass
password = getpass.getpass("Enter password : ")
binary_pass = password.encode('utf-8')
sha256_pass = hashlib.sha256(binary_pass).hexdigest()
print("Hash of entered password : ",sha256_pass)