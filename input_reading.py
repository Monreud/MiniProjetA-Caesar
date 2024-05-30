"""

"""
import string


def lecture_fichier():
    with open("message.txt", 'r', encoding = 'utf-8') as fio:
        # Lire le contenu du fichier
        contenu = fio.read()

    return contenu


def lecture_entree():
    entree = input('Quel message souhaitez-vous décrypter ?')

    return entree


def ecriture():
    contenu = "Hello world"
    # On crée un fichier txt et on écrit dedans
    with open("message_encrypte.txt", "w") as fio:
        fio.write(contenu)


if __name__ == '__main__':
    choix = 0
    while choix != 1 or choix != 2:
        choix = int(input('Souhaitez-vous entrer votre propre message ou en charger un ? \n'
              '1 - Message personnalisé \n'
              '2 - Message dans un fichier'))

        if choix == 1:
            message = lecture_entree()
            #message_decrypt, key = decrypter(message)
            #print('Le message décrypté est : ', message_decrypt, ' et a été crypté avec une clé = ', key)

        elif choix == 2:
            message = lecture_fichier()
            #message_decrypt, key = decrypter(message)
            #print('Le message décrypté est : ', message_decrypt, ' et a été crypté avec une clé = ', key)