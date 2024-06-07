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


if __name__ == '__main__':
    choix = 0
    file_name = lecture_fichier()
    mot_ou_phrase = True

    while choix != 1 or choix != 2:
        choix = int(input('Souhaitez-vous entrer votre propre message ou en charger un ? \n'
                          '1 - Message personnalisé \n ''2 - Message dans un fichier \n'
                          '3 - Quitter'))

        if choix == 1:
            message = lecture_entree()
            mot_ou_phrase = ' ' in message
            file_name = lecture_fichier()
            choix_key = input('Souhaitez-vous fournir une clé de décryptage ? ')

            if not mot_ou_phrase:
                try:
                    message_decrypt, key = decrypt_message.decrypter_mot(message, int(choix_key))
                except ValueError:
                    print('Aucune clé détectée')
                    message_decrypt, key = decrypt_message.decrypter_mot(message)

            else:
                try:
                    phrase = separer_mots_message(message)
                    message_decrypt, key = decrypt_message.decrypter_message(phrase, int(choix_key))
                except ValueError:
                    phrase = separer_mots_message(message)
                    input('Aucune clé détectée, veuillez écrire les mots décryptés sans accents dans le fichier '
                          'mots_pendu.txt et l\'enregistrer puis appuyer sur une touche du clavier')
                    message_decrypt, key = decrypt_message.decrypter_message(phrase)

            print('Le message décrypté est : ', message_decrypt, ' et a été crypté avec une clé = ', key)

        elif choix == 2:
            file_name = lecture_fichier()
            message = lecture_entree()
            message_decrypt, key = decrypt_message.decrypter_mot(message, file_name)
            print('Le message décrypté est : ', message_decrypt, ' et a été crypté avec une clé = ', key)

        else:
            break
