
def PlayFairCipher(key):
    
    key = key.replace(" ", "").upper()  
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    matrix = []
    for char in key + alphabet:
        if char not in matrix:
            matrix.append(char)
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def encrypt(message, key):
    playfair_matrix = PlayFairCipher(key)
    message = message.upper().replace(" ", "")  
    encrypted_message = ""
    pairs = []
    i = 0
    while i < len(message):
        if i == len(message) - 1 or message[i] == message[i+1]:
            pairs.append(message[i] + 'X')
            i += 1
        else:
            pairs.append(message[i:i+2])
            i += 2
    
    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1, row2, col2 = -1, -1, -1, -1 
        for r, row in enumerate(playfair_matrix):
            if char1 in row:
                row1, col1 = r, row.index(char1)
            if char2 in row:
                row2, col2 = r, row.index(char2)
        if row1 == row2:
            encrypted_message += playfair_matrix[row1][(col1 + 1) % 5]
            encrypted_message += playfair_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_message += playfair_matrix[(row1 + 1) % 5][col1]
            encrypted_message += playfair_matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_message += playfair_matrix[row1][col2]
            encrypted_message += playfair_matrix[row2][col1]

    return encrypted_message

def decrypt(encrypted_message, key):
    playfair_matrix = PlayFairCipher(key)
    decrypted_message = ""
    pairs = []
    i = 0
    while i < len(encrypted_message):
        pairs.append(encrypted_message[i:i+2])
        i += 2

    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1, row2, col2 = -1, -1, -1, -1

        for r, row in enumerate(playfair_matrix):
            if char1 in row:
                row1, col1 = r, row.index(char1)
            if char2 in row:
                row2, col2 = r, row.index(char2)

        if row1 == row2:
            decrypted_message += playfair_matrix[row1][(col1 - 1) % 5]
            decrypted_message += playfair_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_message += playfair_matrix[(row1 - 1) % 5][col1]
            decrypted_message += playfair_matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_message += playfair_matrix[row1][col2]
            decrypted_message += playfair_matrix[row2][col1]

    return decrypted_message

key = "MONARCHY"
message = "MOSQUE"
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
