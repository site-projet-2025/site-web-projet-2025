from random import randint
nombre_de_partie=int(input("combien de partie pour cette session: "))
for i in range(nombre_de_partie):   
    resultat_bot_randint=randint(1,3)
    if resultat_bot_randint==3:
        coup_du_bot='papier'
    if resultat_bot_randint==2:
        coup_du_bot='ciseaux'
    else:
        coup_du_bot='pierre'

    coup_du_joueur=str(input("qu'elle est votre choix entre 'papier', 'ciseaux' et 'pierre': "))
    while coup_du_joueur not in ['pierre','papier','ciseaux']:
        print("veuilliez rentrer sois 'pierre', 'papier' ou 'ciseaux'")
        coup_du_joueur=str(input("qu'elle est votre choix entre 'papier', 'ciseaux' et 'pierre': "))
    
    if coup_du_joueur=='papier' and coup_du_bot=='ciseaux':   
        print("vous avez perdu, en effet vous avez fait ",coup_du_joueur,"et le bot a fait",coup_du_bot)

    if coup_du_joueur=='pierre' and coup_du_bot=='papier':
        print("vous avez perdu, en effet vous avez fait ",coup_du_joueur,"et le bot a fait",coup_du_bot)

    if coup_du_joueur=='ciseaux' and coup_du_bot=='pierre':
        print("vous avez perdu, en effet vous avez fait ",coup_du_joueur,"et le bot a fait",coup_du_bot)

    if coup_du_bot==coup_du_joueur:
        print ("vous et le bot avez fait le meme resultats",coup_du_joueur,", conclusion egalité")
    else:
        print("BRAVO!!! vous avez gagné en faisant",coup_du_joueur, "et le bot",coup_du_bot)
