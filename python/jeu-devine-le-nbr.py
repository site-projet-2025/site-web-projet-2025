# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:02:58 2023

@author: julesabry
"""

from random import randint
def jeu_devine_le_nombre_sans_limite():
    num_aleatoire=randint(1,100)
    nombre_du_joueur=int
    nombre_essaie=0
    while nombre_du_joueur!=num_aleatoire:
        nombre_du_joueur=int(input("quelle est le numéros selon vous?"))
        nombre_essaie+=1
        if nombre_du_joueur<num_aleatoire:
            print("trop petit")
        if nombre_du_joueur>num_aleatoire:
            print("trop grand")
    else:
        print("gagner")

def jeu_devine_le_nombre_avec_limite(nombre_de_tour):
    num_aleatoire = randint(1, 100)
    nombre_de_tour_2 = 0
    nombre_essaie=0
    while nombre_de_tour_2 < nombre_de_tour:
        nombre_du_joueur = int(input("Devine le nombre entre 1 et 100 : "))
        nombre_essaie = nombre_essaie+1
        if nombre_du_joueur == num_aleatoire:
            print(f"Bravo, tu as deviné le nombre ! en {nombre_essaie} essais!!")
            break
        elif nombre_du_joueur < num_aleatoire:
            print("Le nombre est plus grand. Essaye encore.")
        else:
            print("Le nombre est plus petit. Essaye encore.")
        
        nombre_de_tour_2 += 1

    if nombre_de_tour_2 == nombre_de_tour:
        print(f"Tu as atteint le nombre maximum de tentatives. Le nombre était {num_aleatoire}.")
quelle_jeu=input("à quel mode du jeu, <<devine le nombre>> voulez-vous jouer? (vous avez le choix entre sans limite ou avec limite) ")
x=str
sans="sans limite"
s="sans"
avec="avec limite"
a="avec"

if quelle_jeu == "sans limite"or quelle_jeu=="sans":
    jeu_devine_le_nombre_sans_limite()
elif quelle_jeu== "avec limite" or quelle_jeu=="avec":
    argument=int(input("combien de tours maximum? "))
    jeu_devine_le_nombre_avec_limite(argument)
else:
    print("veuillez recommencer")