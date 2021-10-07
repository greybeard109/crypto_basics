import string
import enchant
import random


class CaesarCipher:
    """ Implementation of the classic Caesar Cipher """

    def __init__(self, shift=3):
        self.letters = string.ascii_uppercase
        self.key_space = len(self.letters)
        self.generate_keys(shift)

    def generate_keys(self, shift):
        self.key = {self.letters[i]: self.letters[(
            i + shift) % self.key_space] for i in range(self.key_space)}

        # decryption key, is just the reverse of the encryption key
        self.dkey = {value: key for (key, value) in self.key.items()}

    def encrypt(self, message):
        message = message.upper()
        cipher_text = [self.key[letter] if letter in self.letters else letter
                       for letter in message]
        return ''.join(cipher_text)

    def decrypt(self, message):
        message = message.upper()
        clear_text = [self.dkey[letter] if letter in self.letters else letter
                      for letter in message]
        return ''.join(clear_text)


def get_caesar_key(msg):
    """ Brute force the cipher shift, use PyEnchant to detect English words"""

    key = None

    d = enchant.Dict('en_GB')
    for shift in range(1, 26):
        caesar = CaesarCipher(shift=shift)
        decrypt_text = caesar.decrypt(msg)
        for word in decrypt_text.split():
            if d.check(word):
                key = shift
            else:
                key = None
        
        if key:
            break

    return key


if __name__ == '__main__':

    # create a cipher text with a random key
    caesar = CaesarCipher(shift=random.randint(1, 25))
    msg = 'Follow the white rabbit'
    cipher_text = caesar.encrypt(msg)
    print(cipher_text)

   # bruteforce the cipher key 
    key = get_caesar_key(cipher_text)
    if key:
        caesar.generate_keys(key)
        print(f'Key found : {key}')
        print(f'Clear text: {caesar.decrypt(cipher_text)}')
    else:
        print("Key not found")
