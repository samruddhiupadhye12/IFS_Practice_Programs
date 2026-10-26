import random, string

length = int(input("Enter length of password you want : "))
password = ''.join(random.choices( string.ascii_letters + string.digits + string.punctuation, k=length))
print("Generated password : ",password)