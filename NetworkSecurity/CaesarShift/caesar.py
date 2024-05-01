import string

def caesar(text,shift,alphabets):
    
    def alphabet_shift(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(alphabet_shift,alphabets))
    encrypt_alphabet = ''.join(alphabets)
    encrypted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(encrypt_alphabet,encrypted_alphabet)
    return text.translate(table)

plain_text = "Hello, my name is Alishba!"
print(caesar(plain_text,3,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))