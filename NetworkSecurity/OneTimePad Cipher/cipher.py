def string_encryption(text, key):
    cipher_text = ''
    cipher = [0] * len(key)

    for i in range(len(key)):
        cipher[i] = ord(text[i]) - 65 + ord(key[i]) - 65

    for i in range(len(key)):
        if cipher[i] > 25:
            cipher[i] = cipher[i] - 26

    for i in range(len(key)):
        x = cipher[i] + 65
        cipher_text += chr(x)

    return cipher_text

def string_decryption(s, key):
    plain_text = ''
    plain = [0] * len(key)

    for i in range(len(key)):
        plain[i] = ord(s[i]) - 65 - (ord(key[i]) - 65)

    for i in range(len(key)):
        if plain[i] < 0:
            plain[i] = plain[i] + 26

    for i in range(len(key)):
        x = plain[i] + 65
        plain_text += chr(x)

    return plain_text

def main():
    plain_text = 'HELLO'
    key = 'MONEY'
    encrypted_text = string_encryption(plain_text.upper(), key.upper())
    print('Cipher Text - ' + encrypted_text)
    print('Message - ' + string_decryption(encrypted_text, key.upper()))


if __name__ == "__main__":
    main()
