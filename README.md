# RSA Project
The presented project highlights the creation and execution of the RSA encryption algorithm through a Python class. It effectively encapsulates RSA operations in a well-designed Python class structure, focusing on user-friendliness.

# RSA()
`RSA()` creates a instance of the class RSA with variables `private_key` and `public_key`

# public_key
`public_key` is a variable of type `public_key`. It's the encryption key for the `private_key` that was created by the same `RSA()` instance.

# private_key
`private_key` is a variable of type `Private_key`. It's the decryption key for the `public_key` that was created by the same `RSA()` instance.

# encrypt(text: str, public_key: public_key, max_ascii_character = 128)
`encrypt()` is a static method that takes variables, `text` of type `str` and `public_key` of type `public_key`, in order to return the `text` encrypted as type `int`. This `text` can be decrypted by the method `decrypt()`.

# decrypt(encrypted_message: int, private_key: private_key, max_ascii_character = 128):
`decrypt()` is static method that takes variables `encrypted_message` of type `int` and `private_key` of type `private_key`, in order return `encrypted_message` decrypted as tpye `str`.
