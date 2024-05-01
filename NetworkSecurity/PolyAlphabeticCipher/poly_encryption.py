#POLY-ALPHABETIC CIPHER
#In this encryption technique, each letter of the plain-text is substituted onto different letters for encryption
#This is done using the encryption table




encryption_table = [
    "asdfghjklpoiuytrewqzxcvbnm",
    "qazwsxedcrfvtgbyhnupjmikol",
    "zxcvbnmkioplujhytgfredswqa"
]

def polyalphabetic_cipher(plain_text):
    encrypted_text = ''
    key_index = 0
    table_length = len(encryption_table)

    for letter in plain_text:
        shift = key_index % table_length
        encryption_letter = encryption_table[shift][ord(letter) - ord('a')]
        encrypted_text += encryption_letter
        key_index = key_index + 1
    return encrypted_text

def main():
    plain_text = 'attackatdawn'
    polyalphabetic_encryption = polyalphabetic_cipher(plain_text)
    print("Original text: " + plain_text)
    print("Encrypted text: " + polyalphabetic_encryption)
main()