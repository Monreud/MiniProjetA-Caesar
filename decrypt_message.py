"""
Auteur : Augustin Montredon
"""
import string
import input_reading as ir


def decrypter_mot(message: str, key=None):

    alphabet = string.ascii_lowercase
    uncrypted = 0

    mot_decrypter = ''
    current_letter = []
    next_letter = []

    # Brute-force dans le cas où il n'y a pas de clé
    if key is None:
        new_key = 0  # Initialisation de la clé
        while uncrypted == 0:  # Tant que le message n'est pas décrypté on continue à tester
            for i in range(len(message)):
                current_letter = message[i]
                next_letter = alphabet[(alphabet.index(current_letter) + 26 - new_key) % 26]  # On teste selon l'alphabet
                mot_decrypter += next_letter

            if ir.mot_dans_fichier(mot_decrypter):  # On vérifie la présence du mot potentiellement décrypté dans le fichier
                return mot_decrypter, new_key

            else:  # Si pas un mot on recommence
                mot_decrypter = ''
                new_key += 1

    else:  # Simple décryptage selon la clé fournie
        new_key = key
        for i in range(len(message)):
            current_letter = message[i]
            next_letter = alphabet[(alphabet.index(current_letter) + 26 - key) % 26]

            mot_decrypter += next_letter

    return mot_decrypter, new_key


def decrypter_message(message: list, key=None):
    message_decrypte = [''] * len(message)

    for i in range(len(message)):  # On parcours la liste et on décrypte les mots un par un
        mot, key = decrypter_mot(message[i], key)
        message_decrypte[i] = mot

    return message_decrypte, key
