"""from random import randint 

nombre_allumettes = 21
print("il y a ",nombre_allumettes," sur la table" )

allumettes_joueur = 0
while nombre_allumettes>=1:   
    
    allumettes_joueur = int(input("combien d'allumettes prenez-vous ? "))
    while  allumettes_joueur<1 or allumettes_joueur>3 :
        print("le nombre d'allumettes doit etre entre 1 et 3 inclus ")
        allumettes_joueur =int(input("combien d'allumettes prenez-vous ? "))

    
    nombre_allumettes -= allumettes_joueur
    
    if nombre_allumettes >= 3:
        allumettes_bot = randint(1,3)
        print("le bot a pris ",allumettes_bot," allumettes" )
    elif 0< nombre_allumettes <= 3:
        allumettes_bot = randint(1,nombre_allumettes)      
        print("le bot a pris ",allumettes_bot," allumettes" )

    nombre_allumettes -= allumettes_bot
    print("il y a ",nombre_allumettes," sur la table" )
    
    if nombre_allumettes == 1 :# verifie si le joueur a perdu
        print("vous avez perdu ")
    if nombre_allumettes == 0 : # verifie si le joueur a gagne
        print("vous avez gagné(e) ")"""
     

from random import randint 

nombre_allumettes = 21
print("il y a ",nombre_allumettes," sur la table" )

allumettes_joueur = 0
while nombre_allumettes>=1:   
    allumettes_joueur = int(input("combien d'allumettes prenez-vous ? "))
    while  allumettes_joueur<1 or allumettes_joueur>3 :
        print("le nombre d'allumettes doit etre entre 1 et 3 inclus ")
        allumettes_joueur =int(input("combien d'allumettes prenez-vous ? "))
    nombre_allumettes -= allumettes_joueur
    
    if nombre_allumettes >= 3:
        allumettes_bot = randint(1,3)
        print("le bot a pris ",allumettes_bot," allumettes" )
    elif 0< nombre_allumettes <= 3:
        allumettes_bot = randint(1,nombre_allumettes)      
        print("le bot a pris ",allumettes_bot," allumettes" )

    nombre_allumettes -= allumettes_bot
    print("il y a ",nombre_allumettes," sur la table" )
    
    if nombre_allumettes == 1 :# verifie si le joueur a perdu
        print("vous avez perdu ")
    if nombre_allumettes == 0 : # verifie si le joueur a gagne
        print("vous avez gagné(e) ")