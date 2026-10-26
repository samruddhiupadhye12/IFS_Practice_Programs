import rsa
public_key, private_key = rsa.newkeys(2048)
msg = input("Enter the message : ").encode('utf-8')
encrypted = rsa.encrypt(msg, public_key)
decrypted = rsa.decrypt(encrypted, private_key).decode('utf-8')

print("Encrypted message : ",encrypted.hex())
print("Decrypted message : ",decrypted)