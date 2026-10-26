import rsa
public_key, private_key = rsa.newkeys(2048)
msg = input("Enter message for signing : ")
msg_binary = msg.encode()

sign = rsa.sign(msg_binary, private_key, 'SHA-256')
print("Original message : ",msg)
print("Digital Signature : ",sign.hex())

try:
    verifi = rsa.verify(msg_binary, sign, public_key)
    print("Digital sign is valid!")
except Exception:
    print("Digital sign is invalid!")