import numpy as np
def text_to_numbers(text):
    numbers = []
    for char in text:
        val = ord(char.upper()) - ord('A')
        numbers.append(val)
    return numbers

def numbers_to_text(numbers):
    text = " "
    for num in numbers:
        text = text + chr(num % 26 + ord('A'))
    return text

def hill_encrypt(text, key_matrix):
    numbers = text_to_numbers(text)

    block_size = key_matrix.shape[0]
    if len(numbers) % block_size != 0:
        numbers = numbers + [ord('X') - ord('A')]

    chunks = []
    for i in range(0, len(numbers), block_size):
        chunk = numbers[i:i+block_size]
        chunks.append(chunk)

    encrypted_chunks = []
    for chunk in chunks:
        vector = np.array(chunk)
        res = np.dot(key_matrix, vector) % 26
        encrypted_chunks.extend(res)

    return numbers_to_text(encrypted_chunks)

key = np.array([[3,3], [2,5]])
msg = input("Enter plaintext : ")

print("Key Matrix : \n", key)
encrypt = hill_encrypt(msg, key)

print("Plaintext : ",msg.upper())
print("Ciphertext : ", encrypt)