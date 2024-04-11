import random
from sympy import *


class RSA:
    def __init__(self, e, bit_count=512):

        self.e = e

        def generate_large_prime(bits):
            while True:
                prime_candidate = random.getrandbits(bits)
                if isprime(prime_candidate):
                    return prime_candidate

        while True:
            self.p = generate_large_prime(bit_count)
            self.q = generate_large_prime(bit_count)
            self.m = (self.p - 1) * (self.q - 1)
            if gcd(self.m, self.e) == 1:
                break

        self.n = self.p * self.q

        self.d = pow(e, -1, self.m)

        self.public_key = (self.n, self.e)
        self.private_key = (self.n, self.d)

    @staticmethod
    def encrypt(text, n, e, max_ascii_character=128):

        max_ascii_character = len(bin(max_ascii_character)) - 2

        message_bin = ""

        for element in text:
            element = bin(ord(element))
            element = element.replace("0b", "")
            while len(element) != max_ascii_character:
                element = "0" + element
            message_bin += element
        message_bin = int(message_bin, 2)

        def fme(base, exponent, mod):
            x = 1
            power = base % mod
            exponent = bin(exponent)
            o = len(exponent)
            for r in range(o - 1, 1, -1):
                if int(exponent[r]) == 1:
                    x = (x * power) % mod
                power = (power * power) % mod
            return x
        return fme(message_bin, e, n)

    @staticmethod
    def decrypt(encrypt_message, n, d, max_ascii_character=128):

        max_ascii_character = len(bin(max_ascii_character)) - 2

        def fme(base, exponent, mod):
            x = 1
            power = base % mod
            exponent = bin(exponent)
            o = len(exponent)
            for r in range(o - 1, 1, -1):
                if int(exponent[r]) == 1:
                    x = (x * power) % mod
                power = (power * power) % mod
            return x

        decrypt_message_num = fme(encrypt_message, d, n)
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
