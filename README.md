# ENCRYPTAGE/DÉCRYTPAGE CÉSAR
Ce repository contient un code permettant de crypter/décrypter des messages selon la méthode César (avec clé de cryptage) UNIQUEMENT VIA ENTREE UTILISATEUR (dans la console).  
L'utilisateur doit entrer des messages SANS accents, SANS caractères spéciaux et SANS majuscule pour décryptage.
## Contenu du repo
Les fichiers python :  
- main.py : interface utilisateur qui lance les fichiers correspondants
- encodage.py : permet de crypter un message
- input_reading.py : contient les fonctions nécessaires à la lecture et la gestion des entrées utilisateur
- decrypt_message.py : permet de décrypter un message
Les fichiers .txt :
- mots_pendu.txt : contient des mots dont l'utilisateur peut se servir s'il n'a pas d'idée
- bdd_mots.txt : fichier à modifier lors de la phase de décryptage SANS CLÉ (indiqué dans la console)
## Utilisation 
### Encryptage
L'utilisateur saisit un mot qui sera encrypté avec la clé de son choix. 
Il a également un fichier de mots déjà cryptés avec le script, ils possèdent tous une clé de cryptage aléatoire. 
Cette ressource permet à l'utilisateur de saisir des mots cryptés déjà à sa dispoqition pour tester le script de décryptage. 
Les mots cryptés du fichier sont basés sur ceux du pendu. 
### Décryptage
Lorsque l'utilisateur choisit de décrypter un message, il peut saisir en une entrée un mot ou une phrase et le script saura gérer les deux cas.  
Si l'utilisateur fournit une clé le script décrypte le message et renvoit le message.  
Sinon, le script utilise un brute-force et cherche parmis les mots du fichier bdd_mots.txt s'il y a une correspondance pour le mot en cours.  
A noter : POUR NE PAS FOURNIR DE CLÉ, SIMPLEMENT APPUYER SUR ENTRER LORS DE L'INPUT, PUIS ENTRER LES MOTS A TROUVER DANS LE FICHIER bdd_mots.txt ET ENREGISTRER (ctrl + s) PUIS RAPPUYER SUR ENTRER.
