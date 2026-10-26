def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result = result + chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result = result + chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result = result + char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

msg = input("Enter message : ")
shift_val = int(input("Enter shift value : "))

encrypt = caesar_encrypt(msg, shift_val)
decrypt = caesar_decrypt(encrypt, shift_val)

print("Original Message : ",msg)
print("Shift : ", shift_val)
print("Encrypted : ", encrypt)
print("Decrypted : ", decrypt)