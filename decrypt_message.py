"""

"""
import string
import input_reading as ir


def decrypter(message, key=None):
    alphabet = string.ascii_lowercase
    uncrypted = 0

    mot_decrypter = ''
    current_letter = []
    next_letter = []

    if key is None:
        new_key = 0
        while uncrypted == 0:
            for i in range(len(message)):
                current_letter = message[i]
                next_letter = alphabet[(alphabet.index(current_letter) + 26 - new_key) % 26]
                mot_decrypter += next_letter

            if ir.mot_dans_fichier(mot_decrypter):
                return mot_decrypter, new_key

            else:
                mot_decrypter = ''
                new_key += 1

    else:
        new_key = key
        for i in range(len(message)):
            current_letter = message[i]
            next_letter = alphabet[(alphabet.index(current_letter) + 26 - key)%26]

            mot_decrypter += next_letter

    return mot_decrypter, new_key

