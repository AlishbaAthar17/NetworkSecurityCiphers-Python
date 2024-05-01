#VIGENERE CIPHER
#A plain-text message that needs to be encrypted
#A key to encrypt the plain-text message
#The key must repeat cyclically until it matches the length of the plaintext
#Each letter from the plain-text message must move further in the alphabet equal to the index of the letter of the key
#For example, KEY = key , Plain_text = HELLO ; "k" of key lies on the 10th index of the alphabets starting from 0
#"k" lies on "H" of attack so H will move 10 positions ahead and stop at "R" and so on. 

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_to_index = {char: index for index, char in enumerate(alphabet)}
index_to_alphabet = {index: char for index, char in enumerate(alphabet)}

def vigenereCipher(plain_text, key):
    encrypted_text = ""
    key_length = len(key)

    split_text = [plain_text[i:i + key_length] for i in range(0, len(plain_text),key_length)]

    for split in split_text:
        i = 0
        for letter in split:
            encryption_value = (alphabet_to_index[letter] + alphabet_to_index[key[i]]) % len(alphabet)
            encrypted_text += index_to_alphabet[encryption_value]
            i = i + 1
    return encrypted_text

def main():
    key = 'lemon'
    plain_text = 'attackatdawn'
    vigenere_encryption = vigenereCipher(plain_text,key)
    print("Plain text: " + plain_text)
    print("Encrypted text: " + vigenere_encryption)
main()