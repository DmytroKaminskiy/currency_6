
'''
A
Encrypt
'Dima'
['D', 'i', 'm', 'a']
[68, 105, 109, 97] + 1
[69, 106, 110, 98]
['E', 'j', 'n', 'b']
'Enjb'

Decrypt
'Enjb'
['E', 'j', 'n', 'b']
[69, 106, 110, 98] - 1
[68, 105, 109, 97]
['D', 'i', 'm', 'a']
'Dima'

A --> B ('Enjb')
B ('Enjb') --> A 'Dima'
A(encrypt | decrypt)
'''

KEY = 2


def encrypt(message: str) -> str:
    chars = list(message)
    encrypted_message = ''

    for char in chars:
        encrypted_message += chr(ord(char) + KEY)

    return encrypted_message


def decrypt(message: str) -> str:
    chars = list(message)
    encrypted_message = ''

    for char in chars:
        encrypted_message += chr(ord(char) - KEY)

    return encrypted_message