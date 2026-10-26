def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_len = len(key)
    key_index = 0

    for char in text:
        shift = ord(key[key_index % key_len]) - 65

        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower() :
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
        key_index = key_index + 1
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_len = len(key)
    key_index = 0

    for char in text:
        shift = ord(key[key_index % key_len]) - 65

        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower() :
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
        key_index = key_index + 1
    return result


msg = input("Enter message : ")
key = input("Enter key : ")

encrypt = vigenere_encrypt(msg, key)
decrypt = vigenere_decrypt(encrypt, key)


print("Original Message : ",msg)
print("Key : ", key)
print("Encrypted : ", encrypt)
print("Decrypted : ", decrypt)