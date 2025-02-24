from random import randint
class Personnage:
    def __init__(self, nom, ):
        self.nom = nom
        self.points_de_vie = 0
        self.attaque = 0
        self.defense = 0
        self.vitesse = 0
        self.lvl_joueur=1
        self.choix_classe()
        self.points_de_vie_monstre= randint(50,100)
        self.nom_monstre= liste_monstre[randint(0,9)]
        self.attaque_monstre=randint(5,20)
        self.defense_monstre=randint(5,20)
         
    def choix_classe(self):
        print("Choisissez votre classe :")
        print("1. Mage")
        print("2. Assassin")
        print("3. Tank")
        choix = input("le numéro ou le nom de la classe choisie : ")
        if choix == "1" or choix=="Mage":
            self.attaque += 10
            self.defense += 6
            self.vitesse += 5
            self.points_de_vie += 30
        elif choix == "2" or choix=="Assassin":
            self.attaque += 5
            self.vitesse += 10
            self.points_de_vie += 40
        elif choix == "3"or choix=="Tank":
            self.attaque += 5
            self.defense += 10
            self.vitesse += 2
            self.points_de_vie += 50
        else:
            print("Choix invalide")
            self.choix_classe()
        print("Vous avez choisi la classe", choix,"et vos stats sont""\n",
              "Attaque:", self.attaque,"\n",
              "Défense:", self.defense,"\n",
              "Vitesse:", self.vitesse, "\n",
              "Points de vie:", self.points_de_vie)
        
    def monter_niveau(self):
        nombre_de_points=5
        self.lvl_joueur+=1
        print("Vous avez atteint le niveau",self.lvl_joueur)
        print("il vous reste",nombre_de_points,"points à répartir")
        print("1. Attaque")
        print("2. Défense")
        print("3. Vitesse")
        print("4. Points de vie")
        
        while nombre_de_points!=0:
            choix=input("le numéro de la caractéristique à augmenter : ")
            if choix=="1":
                self.attaque+=1
                nombre_de_points-=1
            elif choix=="2":
                self.defense+=1
                nombre_de_points-=1
            elif choix=="3":
                self.vitesse+=1
                nombre_de_points-=1
            elif choix=="4":
                self.points_de_vie+=5
                nombre_de_points-=1
            else:
                print("Choix invalide")
                self.monter_niveau()
            print(  "1. Attaque:", self.attaque,"\n",
                    "2. Défense:", self.defense,"\n",
                    "3. Vitesse:", self.vitesse, "\n",
                    "4. Points de vie:", self.points_de_vie)
            print("il vous reste",nombre_de_points,"points à répartir")
        print("Vous avez fini de répartir vos points")
    
    def attaque_monstre (self):
        self.points_de_vie=self.attaque_monstre-self.defense/2
        print("Vous avez perdu",self.attaque_monstre-self.defense/2,"points de vie") 
        print("Il vous reste",self.points_de_vie,"points de vie")
    
    def attaque_joueur (self):
        self.points_de_vie_monstre=self.attaque-self.defense_monstre/2
        

liste_monstre=["Gobelin","Orc","Dragon","Loup","Squelette","Golem","Géant","Chimère","Basilic","Hydre"]
nomdujoueur = input("Entrez votre nom : ")
perso1=Personnage(nomdujoueur)
perso1.monter_niveau()
