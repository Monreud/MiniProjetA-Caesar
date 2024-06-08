"""

"""

import decrypt_message


def lecture_fichier():
    with open("mots_pendu.txt", 'r', encoding='utf-8') as fio:
        # Lire le contenu du fichier
        contenu = fio.read()

    return contenu


def mot_dans_fichier(mot):
    mots = lecture_fichier().splitlines()
    return mot in mots


def lecture_entree():
    return input('Quel message souhaitez-vous décrypter ?')


def separer_mots_message(message):
    mots = message.split()
    return mots


def ecriture(file_name, contenu):
    # On crée un fichier txt et on écrit dedans
    with open(file_name, "w") as fio:
        fio.write(contenu)
