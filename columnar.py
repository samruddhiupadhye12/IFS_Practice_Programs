def columnar_encrypt(text, key):
    num_cols = len(key)
    num_rows = -(-len(text) // num_cols)
    padded_text = text.ljust(num_cols * num_rows, 'x')

    matrix = []
    for i in range(0, len(padded_text), num_cols):
        row = padded_text[i:i+num_cols]
        matrix.append(row)

    col_order = sorted(range(len(key)), key=lambda k:key[k])

    ciphertext = ''.join(''.join(row[i] for row in matrix) for i in col_order)
    return ciphertext

def columnar_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = -(-len(ciphertext) // num_cols)
    col_length = num_rows

    col_order = sorted(range(len(key)), key=lambda k:key[k])

    columns = {}
    start = 0
    for i in col_order:
        columns[i] = ciphertext[start:start+col_length]
        start = start + col_length

    matrix = []
    for r in range(num_rows):
        row = ""
        for c in range(num_cols):
            row = row + columns[c][r]
        matrix.append(row)

    plaintext = ''.join(matrix).rstrip('x')
    return plaintext

msg = input("Enter the message : ")
key = input("Enter the key : ")

encrypt = columnar_encrypt(msg, key)
decrypt = columnar_decrypt(encrypt, key)

print("Original : ",msg)
print("Encrypted : ", encrypt)
print("Decrypted : ",decrypt)