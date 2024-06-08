"""
Auteur : Augustin Montredon
"""

import decrypt_message


# Lis et renvoit les mots du fichier fournit
def lecture_fichier():
    with open("bdd_mots.txt", 'r', encoding='utf-8') as fio:
        # Lire le contenu du fichier
        contenu = fio.read()

    return contenu


# prends chaque mots et sépare pour les retours à la ligne
def mot_dans_fichier(mot):
    mots = lecture_fichier().splitlines()
    return mot in mots


# Entrée utilisateur pour décryptage
def lecture_entree():
    return input('Quel message souhaitez-vous décrypter ?')


# Dans le cas d'une phrase, sépare la string par les espaces et renvoie une liste de mots
def separer_mots_message(message):
    mots = message.split()
    return mots



