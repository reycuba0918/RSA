from random import getrandbits
from sympy import isprime
from sympy import gcd
from RSA_util import *

class RSA:

    max_ascii_character = 128

    def __init__(self): 

        e = 1001 # e needs to be odd
        bit_count:int=512

        def generate_large_prime(bits):
            while True:
                prime_candidate = getrandbits(bits)
                if isprime(prime_candidate):
                    return prime_candidate

        while True:
            p = generate_large_prime(bit_count)
            q = generate_large_prime(bit_count)
            m = (p - 1) * (q - 1)
            pop = gcd(m, e)
            if pop == 1:
                break

        n = p * q

        d = pow(e, -1, m)

        self.public_key = public_key(n, e)
        self.private_key = private_key(n, d)

    @staticmethod
    def encrypt(text: str, public_key: public_key, max_ascii_character = 128):

        max_ascii_character = len(bin(max_ascii_character)) - 2

        message_bin = ""

        for element in text:
            element = bin(ord(element))
            element = element.replace("0b", "")
            while len(element) != max_ascii_character:
                element = "0" + element
            message_bin += element
        message_bin = int(message_bin, 2)

        return fme(message_bin, public_key.e, public_key.n)

    @staticmethod
    def decrypt(encrypted_message: int, private_key: private_key, max_ascii_character = 128):

        max_ascii_character = len(bin(max_ascii_character)) - 2

        decrypt_message_num = fme(encrypted_message, private_key.d, private_key.n)
        decrypt_message_bin = bin(decrypt_message_num).replace("0b", "")
        while len(decrypt_message_bin) % max_ascii_character != 0:
            decrypt_message_bin = "0" + decrypt_message_bin

        decrypt_message = ""
        for i in range(len(decrypt_message_bin) - 1, -1, -8):
            temp_letter_in_bin = ""
            for ii in range(i - (max_ascii_character - 1), i + 1):
                temp_letter_in_bin += decrypt_message_bin[ii]
            decrypt_message = chr(int(temp_letter_in_bin, 2)) + decrypt_message

        return decrypt_message
