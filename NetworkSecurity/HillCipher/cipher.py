def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def matrix_inverse(matrix, modulus):
    det = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )

    for i in range(modulus):
        if (det * i) % modulus == 1:
            det_inv = i
            break

    if det_inv == 0:
        raise ValueError("Matrix is not invertible")

    inverse_matrix = [
        [
            (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) % modulus,
            (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) % modulus,
            (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) % modulus,
        ],
        [
            (matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) % modulus,
            (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) % modulus,
            (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) % modulus,
        ],
        [
            (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) % modulus,
            (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) % modulus,
            (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % modulus,
        ],
    ]

    for i in range(3):
        for j in range(3):
            inverse_matrix[i][j] = (inverse_matrix[i][j] * det_inv) % modulus

    return inverse_matrix

def hill_encrypt(plain_text, key):
    matrix_size = 3
    plain_text = plain_text.upper().replace(" ", "")
    cipher_text = ""

    while len(plain_text) % matrix_size != 0:
        plain_text += "X"

    for i in range(0, len(plain_text), matrix_size):
        block = [ord(char) - ord('A') for char in plain_text[i:i + matrix_size]]
        encrypted_block = [
            (key[0][0] * block[0] + key[0][1] * block[1] + key[0][2] * block[2]) % 26,
            (key[1][0] * block[0] + key[1][1] * block[1] + key[1][2] * block[2]) % 26,
            (key[2][0] * block[0] + key[2][1] * block[1] + key[2][2] * block[2]) % 26,
        ]

        for num in encrypted_block:
            cipher_text += chr(num + ord('A'))

    return cipher_text

def hill_decrypt(cipher_text, key):
    matrix_size = 3
    cipher_text = cipher_text.upper().replace(" ", "")
    plain_text = ""

    inverse_key = matrix_inverse(key, 26)

    for i in range(0, len(cipher_text), matrix_size):
        block = [ord(char) - ord('A') for char in cipher_text[i:i + matrix_size]]
        decrypted_block = [
            (inverse_key[0][0] * block[0] + inverse_key[0][1] * block[1] + inverse_key[0][2] * block[2]) % 26,
            (inverse_key[1][0] * block[0] + inverse_key[1][1] * block[1] + inverse_key[1][2] * block[2]) % 26,
            (inverse_key[2][0] * block[0] + inverse_key[2][1] * block[1] + inverse_key[2][2] * block[2]) % 26,
        ]

        for num in decrypted_block:
            plain_text += chr(num + ord('A'))

    return plain_text
    
key = [
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19]
]
plain_text = "PAY MORE MONEY"
cipher_text = hill_encrypt(plain_text, key)
decrypted_text = hill_decrypt(cipher_text, key)

print("Original Text:", plain_text)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)
