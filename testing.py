from RSA import *

rsa = RSA()

message = "The quick brown fox jumps over the lazy dog."

encrypted_message = RSA.encrypt(message, rsa.public_key)

decrypted_message = RSA.decrypt(encrypted_message, rsa.private_key)

print("message:", message)
print()
print("encrypted_message:", encrypted_message)
print()
print("decrypted_message:", decrypted_message)