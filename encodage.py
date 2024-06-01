"""
Encodage César

"""
import string
from random import randint
from random import choice
# test git
def encodage(mot_a_encoder, cle_decriptage):
    mot_crypte = ""
    alphabet = string.ascii_lowercase  # On recupere l'alphabet
    alphabet_crypte = ""
    ### Test boucle sur tout l'alphabet
    for i in range(len(alphabet)):
        alphabet_crypte += alphabet[(i + cle_decriptage) % 26]
        # On décalle l'alphabet, le modulo sert à recommencer l'alphabet pour les extrémités

    for i in range(len(mot_a_encoder)):
        mot_crypte += alphabet_crypte[alphabet.find(mot_a_encoder[i])]
        # On cherche la lettre du mot saisi dans l'alphabet normal
        # On trouve la lettre équivalente dans notre alphabet crypté
        # On concatène chaque lettre cryptée dans notre mot crypté

    return mot_crypte

def encodage_fichier ():
    fichier_utilisateur = "mots_pendu.txt"
    fichier = open(fichier_utilisateur, "r", encoding="utf-8")
    fichier_encode = open("mots_encode.txt", "w", encoding="utf-8")

    banque_de_mots = fichier.read().splitlines()



    for i in range(len(banque_de_mots)):
        cle_aleatoire = randint(1, 25)  # Une clé à 0 n'encode pas le mot
        banque_de_mots_encode = encodage(banque_de_mots[i], cle_aleatoire)
        fichier_encode.write(f"{banque_de_mots_encode}\n")
    return fichier_encode

encodage("test", -2)
encodage_fichier()