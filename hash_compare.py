import hashlib
m1 = input("Enter first message : ")
m2 = input("Enter second message : ")
b1 = m1.encode('utf-8')
b2 = m2.encode('utf-8')
h1 = hashlib.sha256(b1).hexdigest()
h2 = hashlib.sha256(b2).hexdigest()
print("Hash of first message : ",h1)
print("Hash of second message : ",h2)

if h1 == h2:
    print("Both messages have same Hash.")
else:
    print("Both messages have different Hash.")