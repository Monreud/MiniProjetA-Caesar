"""
Encodage César

"""
import string


def encodage(mot_a_encoder, cle_decriptage):
    mot_crypte = ""
    alphabet = string.ascii_lowercase  # On recupere l'alphabet
    alphabet_crypte = ""
    print(alphabet)  # test affichage
    print(mot_a_encoder)

    ### Test boucle sur tout l'alphabet
    for i in range(len(alphabet)):
        alphabet_crypte += alphabet[(i + cle_decriptage) % 26]
        # On décalle l'alphabet, le modulo sert à recommencer l'alphabet pour les extrémités
        print(alphabet_crypte)

    for i in range(len(mot_a_encoder)):
        mot_crypte += alphabet_crypte[alphabet.find(mot_a_encoder[i])]
        # On cherche la lettre du mot saisi dans l'alphabet normal
        # On trouve la lettre équivalente dans notre alphabet crypté
        # On concatène chaque lettre cryptée dans notre mot crypté

    print(f"cryptage {mot_crypte}")
    return mot_crypte


encodage("test", -2)
