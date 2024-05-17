# RSA Project
The presented project highlights the creation and execution of the RSA encryption algorithm through a Python class. It effectively encapsulates RSA operations in a well-designed Python class structure, focusing on user-friendliness.

## RSA()
`RSA()` creates an instance of the class RSA with variables `private_key` and `public_key`

## public_key
`public_key` is a variable of type `public_key`. It's the encryption key for the `private_key` that was created by the same `RSA()` instance.

## private_key
`private_key` is a variable of type `Private_key`. It's the decryption key for the `public_key` that was created by the same `RSA()` instance.

## encrypt(text: str, public_key: public_key, max_ascii_character = 128)
`encrypt()` is a static method that takes variables, `text` of type `str` and `public_key` of type `public_key`, in order to return the `text` encrypted as type `int`. This `text` can be decrypted by the method `decrypt()`.

## decrypt(encrypted_message: int, private_key: private_key, max_ascii_character = 128):
`decrypt()` is static method that takes variables `encrypted_message` of type `int` and `private_key` of type `private_key`, in order return `encrypted_message` decrypted as tpye `str`.

## max_ascii_character
`max_ascii_character` is an optional parameter present in `encrypt()` and `decrypt()` that allows users to change the highest ASCII character that is used in message that being encrypted or decrypted.

## Example of the RSA class being used
```
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
```
### Output
```
message: The quick brown fox jumps over the lazy dog.

encrypted_message: 54627992755237788124878797434886663646060165265974648366009157378922788991212314091224940830687047439418950954412940583014435692221097983748662424312869461471177576317064245867567178523768579860116324157673674422736662441710481890765514804614118498977843799808833989209716357913633740252232135282873226889649

decrypted_message: The quick brown fox jumps over the lazy dog.
```
**Note that `encrypted_message` will always be a random number.
