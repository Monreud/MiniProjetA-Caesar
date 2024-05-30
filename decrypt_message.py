"""

"""
import string
import input_reading as ir


def decrypter(message, key):
    alphabet = string.ascii_lowercase
    uncrypted = 0

    mot_decrypter = ''
    current_letter = []
    next_letter = []


    for i in range(len(message)):
        current_letter = message[i]
        next_letter = alphabet[(alphabet.index(current_letter) + 26 - key)%26]

        mot_decrypter += next_letter

    return mot_decrypter

