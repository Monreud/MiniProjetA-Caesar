"""

"""
import string

import decrypt_message


def lecture_fichier():
    with open("mots_pendu.txt", 'r', encoding = 'utf-8') as fio:
        # Lire le contenu du fichier
        contenu = fio.read()

    return contenu


def mot_dans_fichier(mot):
    mots = lecture_fichier().splitlines()
    return mot in mots


def lecture_entree():
    return input('Quel message souhaitez-vous décrypter ?')


def ecriture(file_name,contenu):
    # On crée un fichier txt et on écrit dedans
    with open(file_name, "w") as fio:
        fio.write(contenu)


if __name__ == '__main__':
    choix = 0
    file_name = lecture_fichier()
    while choix != 1 or choix != 2:
        choix = int(input('Souhaitez-vous entrer votre propre message ou en charger un ? \n'
              '1 - Message personnalisé \n'
              '2 - Message dans un fichier \n'
                          '3 - Quitter'))

        if choix == 1:
            message = lecture_entree()
            file_name = lecture_fichier()
            choix_key = input('Souhaitez-vous fournir une clé de décryptage ? ')
            try:
                message_decrypt, key = decrypt_message.decrypter(message, int(choix_key))
            except ValueError:
                print('Aucune clé détectée')
                message_decrypt, key = decrypt_message.decrypter(message)
            print('Le message décrypté est : ', message_decrypt, ' et a été crypté avec une clé = ', key)

        elif choix == 2:
            file_name = lecture_fichier()
            message = lecture_entree()
            message_decrypt, key = decrypt_message.decrypter(message, file_name)
            print('Le message décrypté est : ', message_decrypt, ' et a été crypté avec une clé = ', key)

        else:
            break