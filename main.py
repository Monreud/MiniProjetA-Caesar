"""
Encodage et décodage César
"""
import input_reading as ir
import encodage
import decrypt_message

if __name__ == "__main__":
    choix = 0
    end = 0

    while choix != 1 and choix != 2 and choix != 3:
        choix = int(input("Souhaitez vous \n1 - Encoder un message ?\n2 - Décoder un message ?\n3 - Quitter\n"))


        if choix == 1:
            while end != 1 and end != 2:
                end = int(input("Souhaitez vous \n1 - Encoder un mot ?\n2 - Quitter\n? "))
                if end == 1:
                    mot_a_encoder = input("Quel mot ou phrase souhaitez vous encoder ? ")
                    cle_cryptage = int(input("Quelle valeur de clé souhaitez vous pour encoder votre mot "))
                    mot_crypte = encodage.encodage_phrase(mot_a_encoder, cle_cryptage)
                    print(f'Votre mot crypté est {mot_crypte}')
                elif end == 2:
                    print("Au revoir")
                    break
                else:
                    print("Ce cas n'est pas pris en compte par le programme\n")



        elif choix == 2:
            choix2 = 0
            file_name = ir.lecture_fichier()
            mot_ou_phrase = True

            while choix2 != 1 or choix2 != 2:
                choix2 = int(input('Entrez un mot ou une phrase ou quitter \n 1 - Message personnalisé \n 2 - Quitter'))

                if choix2 == 1:
                    message = ir.lecture_entree()
                    mot_ou_phrase = ' ' in message
                    file_name = ir.lecture_fichier()
                    choix_key = input('Souhaitez-vous fournir une clé de décryptage ? ')

                    if not mot_ou_phrase:
                        try:
                            message_decrypt, key = decrypt_message.decrypter_mot(message, int(choix_key))
                        except ValueError:
                            print('Aucune clé détectée')
                            message_decrypt, key = decrypt_message.decrypter_mot(message)

                    else:
                        try:
                            phrase = ir.separer_mots_message(message)
                            message_decrypt, key = decrypt_message.decrypter_message(phrase, int(choix_key))
                        except ValueError:
                            phrase = ir.separer_mots_message(message)
                            input('Aucune clé détectée, veuillez écrire les mots décryptés sans accents dans le fichier '
                                  'bdd_mots.txt et l\'enregistrer puis appuyer sur une touche du clavier')
                            message_decrypt, key = decrypt_message.decrypter_message(phrase)

                    print('Le message décrypté est : ', message_decrypt, ' et a été crypté avec une clé = ', key, ' ou ', key - 26)

                elif choix2 == 2:
                    break

                else:
                    choix2 = input('Mauvaise entrée, veuillez entrez un mot ou une phrase ou quitter \n '
                                  '1 - Message personnalisé \n 2 - Quitter')


        elif choix == 3:
            print("Au revoir")
            break

        else:
            print("Saisie invalide veuillez recommencer ")

