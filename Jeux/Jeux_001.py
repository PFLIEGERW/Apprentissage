#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

#Perso = PV, Armure, Arme, Cartouches restantes,
#Potion de Soin, Terrain, Visibilité
#Adversaire = PV, Armure, Arme, Cartouches restantes,
#Potion de Soin, Terrain, Visibilité
#Terrain = Nom, Esquive, Visibilité
#Armures = Nom, Esquive, Armure
#Armes = Nom, Dégâts, Cartouches, mode de tir


dict_armures = {}
dict_armures["Lourde"] = [-9,10]
dict_armures["Moyenne"] = [-7,8]
dict_armures["Légère"] = [0,5]
dict_armures["Aucune"] = [10,0]
cle_dict_armures = list(dict_armures.keys())
dict_armes = {}
#dict_armes["Test"] = [50,10,2]
dict_armes["L1A1"] = [15,20,1]
dict_armes["M16"] = [12,30,3]
dict_armes["Rhino"] = [20,6,1]
# dict_armes["Pied de biche"] = [8,-1]
cle_dict_armes = list(dict_armes.keys())
dict_terrain = {}
dict_terrain[0] = ["Néant",0,0]
dict_terrain[1] = ["Buisson",25,25]
dict_terrain[2] = ["Petit rocher",50,50]
dict_terrain[3] = ["Gros rocher",150,0]
dict_terrain[4] = ["Plaine",0,100]
cle_dict_terrain = list(dict_terrain.keys())

list_coordonnees = [[0,0,0,0,0,0],
                    [0,4,4,3,4,0],
                    [0,4,4,2,1,0],
                    [0,1,3,2,2,0],
                    [0,3,2,3,4,0],
                    [0,0,0,0,0,0]]


def GenCarte():
    for i in range (1,4):
        for j in range (1,4):
            list_coordonnees[i][j] = random.randint(1,4)


class Personnage:
    def __init__(self,nom_in,posY_in,posX_in):
        self.Nom = nom_in
        self.PV = 20
        self.Armure = ["",0,0]
        self.Potion = 1
        self.Arme = ["",0,0,0]
        self.Cartouches_restantes = 0
        self.Competence = 65
        self.Esquive = 0
        self.Actions = 0
        self.PosY = posY_in # doit contenir la coordonnée Y.
        self.PosX = posX_in # doit contenir la coordonnée X.
        self.Emplacement = dict_terrain[list_coordonnees[self.PosY][self.PosX]]\
.copy()


Adversaire = Personnage("Adversaire",1,1)
Joueur1 = Personnage("Joueur1",4,4)


def Score(perso,compteur):
    
    try:
        with open("Duel_Scores.txt","r+") as file:
            list_scores = file.read().splitlines()
    except FileNotFoundError:
        list_scores = []
    
    score_tuples_present = (perso.Nom,compteur)
    list_scores.append(str(score_tuples_present)) #conversion en string
    list_scores.sort(key = lambda i:i[1],reverse = True) #Tri ordre croissant
    
    with open("Duel_Scores.txt", "w") as file:
        for element in list_scores:
            if element.strip():
                file.write(element+"\n")
    print("Meilleures scores :")
    for x in list_scores:
        print(x)


def Position(perso):
     #Cette fonction indique l'emplacement actuel du personnage.
     #Elle lit également les emplacements situés
     #autour (NSEO).
    if perso.Nom == Joueur1.Nom:
        print(perso.Nom,"vous êtes situé à l'emplacement suivant :",\
        perso.Emplacement[0],"Esquive :",perso.Emplacement[1],\
        "Visibilité :",perso.Emplacement[2])
        print(perso.Nom,"voit ceci :")
        print("-",dict_terrain[list_coordonnees[perso.PosY][perso.PosX-1]][0],\
    "vers l'ouest.")
        print("-",dict_terrain[list_coordonnees[perso.PosY][perso.PosX+1]][0],\
    "vers l'est.")
        print("-",dict_terrain[list_coordonnees[perso.PosY+1][perso.PosX]][0],\
    "vers le sud")
        print("-",dict_terrain[list_coordonnees[perso.PosY-1][perso.PosX]][0],\
    "vers le nord")


def Soin(perso):
    if perso.Potion > 0:
        perso.PV += 10
        print(perso.Nom,"boit une potion de soin !")
    else:
        print(perso.Nom,"n'a plus de potion à boire !")


def Observation(attaquant,defenseur):
    vue = random.randint(1,100)
    
    if attaquant.Nom == Joueur1.Nom:
        print(attaquant.Nom,"voici votre état de santé :",attaquant.PV)
        Position(attaquant)
        print(attaquant.Nom,"Il vous reste",attaquant.Cartouches_restantes,\
        "munitions")
        
        if vue <= defenseur.Emplacement[2]:
            print(defenseur.Nom,"est situé à l'emplacement suivant :"\
            ,defenseur.Emplacement[0])
            print(attaquant.Nom,"voici l'état de",defenseur.Nom,defenseur.PV)
            print(attaquant.Nom,"Voici l'équipement de votre adversaire :",\
            "Armure :",defenseur.Armure[0],"Arme :",defenseur.Arme[0])
            return 1
        else:
            print(defenseur.Nom,"n'est pas visible actuellement.")
            return 0
            
    else:
        if vue <= defenseur.Emplacement[2]:
            return 1
        else:
            return 0


#Deplacement à réécrire complètement.
def Deplacement(perso,compteur):
    tempX = perso.PosX
    tempY = perso.PosY
    if perso.Nom == Joueur1.Nom:
        print("Vers où voulez-vous vous déplacer (N)ord, (S)ud, (E)st,\
(O)uest ?")
        direction = input()
        match direction:
            case "N":
                perso.PosY += - 1
                perso.PosX += 0
                perso.Emplacement = dict_terrain[list_coordonnees[perso.PosY]\
[perso.PosX]].copy()

            case "S":
                perso.PosX += 0
                perso.PosY += 1
                perso.Emplacement = dict_terrain[list_coordonnees[perso.PosY]\
[perso.PosX]].copy()

            case "E":
                perso.PosX += 1
                perso.PosY += 0
                perso.Emplacement = dict_terrain[list_coordonnees[perso.PosY]\
[perso.PosX]].copy()

            case "O":
                perso.PosX += -1
                perso.PosY += 0
                perso.Emplacement = dict_terrain[list_coordonnees[perso.PosY]\
[perso.PosX]].copy()
            
            case _:
                print("Entrée incorrecte.")
                return Deplacement(perso,compteur)

        if perso.Emplacement[0] == "Néant":
            print("Vous ne pouvez pas aller par là !")
            perso.PosX = tempX
            perso.PosY = tempY
            return Deplacement(perso)

    else:
        if perso.Emplacement[0] != "Petit rocher":
            if compteur % 2 == 0:
                direction = random.randint(0,1)
            else:
                direction = random.randint(2,3)
            match direction:
                case 0: # Nord
                    perso.PosY += - 1
                    perso.PosX += 0
                    perso.Emplacement = dict_terrain[list_coordonnees\
[perso.PosY][perso.PosX]].copy()

                case 1: # Est
                    perso.PosX += 0
                    perso.PosY += 1
                    perso.Emplacement = dict_terrain[list_coordonnees\
[perso.PosY][perso.PosX]].copy()

                case 2: # Sud
                    perso.PosX += 1
                    perso.PosY += 0
                    perso.Emplacement = dict_terrain[list_coordonnees\
[perso.PosY][perso.PosX]].copy()

                case 3: # Ouest
                    perso.PosX += -1
                    perso.PosY += 0
                    perso.Emplacement = dict_terrain[list_coordonnees\
[perso.PosY][perso.PosX]].copy()

            if perso.Emplacement[0] == "Néant":
                perso.PosX = tempX
                perso.PosY = tempY
                return Deplacement(perso,compteur)



def Equipement(perso):
    if perso == Joueur1.Nom:
        print("Veuillez choisir votre arme parmis la liste suivante :",\
cle_dict_armes)
        
        temp_joueur1_arme = input()
        try:
            Joueur1.Arme = dict_armes[temp_joueur1_arme].copy()
        except KeyError:
            print("Entrée incorrecte !")
            return Equipement(perso)

        Joueur1.Arme.insert(0,temp_joueur1_arme)
        Joueur1.Cartouches_restantes = Joueur1.Arme[2]
        
        print("Veuillez choisir votre armure parmis la liste suivante : ",\
cle_dict_armures)
        temp_joueur1_armure = input()
        try:
            Joueur1.Armure = dict_armures[temp_joueur1_armure].copy()
        except KeyError:
            print("Entrée incorrecte !")
            return Equipement(perso)

        Joueur1.Armure.insert(0,temp_joueur1_armure)
    
    else:
        temp_adversaire_arme = random.choice(cle_dict_armes)
        temp_adversaire_armure = random.choice(cle_dict_armures)
        
        Adversaire.Arme = dict_armes[temp_adversaire_arme].copy()
        Adversaire.Arme.insert(0,temp_adversaire_arme)
        Adversaire.Cartouches_restantes = Adversaire.Arme[2]
        
        Adversaire.Armure = dict_armures[temp_adversaire_armure].copy()
        Adversaire.Armure.insert(0,temp_adversaire_armure)


def Attaque(attaquant,defenseur):
    for tir in range (attaquant.Arme[3]):
        if attaquant.Cartouches_restantes > 0:
            jet = random.randint(1,100)+(tir*5)
            if jet <= attaquant.Competence-defenseur.Esquive:
                attaquant.Cartouches_restantes -= 1
                
                if attaquant.Arme[1] <= defenseur.Armure[2]:
                    blessure = 0
                elif attaquant.Arme[1] > defenseur.Armure[2]:
                    blessure = attaquant.Arme[1]-defenseur.Armure[2]

                print(attaquant.Nom,"a infligé",blessure,"dégâts à",\
defenseur.Nom)
                defenseur.PV -= blessure

            else:
                attaquant.Cartouches_restantes -= 1
                print(attaquant.Nom,"a râté son attaque !")
        else:
            print("Il ne reste pas de munitions à",attaquant.Nom,"!")
            break
            
def TourHumain(localisation_adversaire,localisation_joueur):
    print("Quelle action voulez-vous effectuer ?")
    print("1 - Déplacement. 2 - Observation. 3 - Potion de soin. \
4 - Attaque")
    try:
        choix = int(input())
    except ValueError:
        print("Entrée incorrecte !")
        return TourHumain(localisation_adversaire,localisation_joueur)
    match choix:
        case 1:
            Deplacement(Joueur1,compteurs_tours)
            Joueur1.Esquive = Joueur1.Armure[1]\
                            +Joueur1.Emplacement[1]
            localisation_joueur = 0
            Joueur1.Actions -= 1
            print("Actions restantes :",Joueur1.Actions)
        case 2:
            obs = Observation(Joueur1,Adversaire)
            Joueur1.Actions -= 1
            if obs == 1:
                localisation_adversaire = 1
            print("Actions restantes :",Joueur1.Actions)
            if localisation_adversaire == 1 and Joueur1.Actions > 0:
                print("Vous pouvez attaquer.")
                print("Voulez-vous attaquer ? (oui/non)")
                choix_attaque = input()
                if choix_attaque.lower() == "oui":
                    Attaque(Joueur1,Adversaire)
                    Joueur1.Actions -= 1
                else:
                    print("Vous n'attaquez pas.")
            else:
                print("Vous ne pouvez pas attaquer \
pour l'instant.")
        case 3:
            print("Vous buvez une potion de soin.")
            Soin(Joueur1)
            Joueur1.Actions -= 1
        case 4:
            if localisation_adversaire == 1:
                Attaque(Joueur1,Adversaire)
                Joueur1.Actions -= 1
            else:
                print("Vous n'avez pas encore localisé \
votre adversaire.")
        case _:
            print("Entrée incorrecte !")
            return TourHumain()


def main():
    GenCarte()
    
    print("Bienvenue dans ce simulateur de duel.")
    Equipement(Joueur1.Nom)
    
    print("Voici votre arme :",Joueur1.Arme[0],"Dégâts :",\
Joueur1.Arme[1],"Nombre de cartouches :",Joueur1.Arme[2],"mode de tir :",\
Joueur1.Arme[3])

    print("Voici votre armure :",Joueur1.Armure[0],"Modificateur d'esquive :",\
Joueur1.Armure[1],"Protection :",Joueur1.Armure[2])

    print("Voici votre emplacement :",Joueur1.Emplacement[0],"Esquive :",\
Joueur1.Emplacement[1],"Visibilité :",Joueur1.Emplacement[2])

    print("Votre adversaire se prépare...")
    Equipement(Adversaire.Nom)
    
    combat = 1
    compteurs_tours = 0
    
    while combat == 1:
        localisation_adversaire = 0
        localisation_joueur = 0
        while Joueur1.PV > 0 and Adversaire.PV > 0:
            Joueur1.Actions = 2
            compteurs_tours += 1
            print("-" * 5)
            print("TOUR N°",compteurs_tours)
            while Joueur1.Actions > 0 and Joueur1.PV > 0:
                print("*" * 5)
                TourHumain(localisation_adversaire,localisation_joueur)
            
            Adversaire.Actions = 2
            while Adversaire.Actions > 0 and Adversaire.PV > 0:
                print("*" * 5)
                if Adversaire.Emplacement[0] != "Petit rocher":
                    print("Votre adversaire se déplace !")
                    Deplacement(Adversaire,compteurs_tours)
                    Adversaire.Esquive = Adversaire.Armure[1]\
                                    +Adversaire.Emplacement[1]
                    localisation_adversaire = 0
                    Adversaire.Actions -= 1
                elif Adversaire.PV <= 10 and Adversaire.Potion > 0:
                    print("Votre adversaire cherche une potion !")
                    Soin(Adversaire)
                    Adversaire.Actions -= 1
                    Adversaire.Potion -= 1
                elif localisation_joueur == 1:
                    Attaque(Adversaire,Joueur1)
                    Adversaire.Actions -= 1
                else:
                    print("Votre adversaire observe !")
                    adv_obs = Observation(Adversaire,Joueur1)
                    Adversaire.Actions -= 1
                    if adv_obs == 1:
                        localisation_joueur = 1
                        if localisation_joueur == 1 and Adversaire.Actions > 0:
                            Attaque(Adversaire,Joueur1)    
                            Adversaire.Actions -= 1

        if Joueur1.PV <= 0:
            print("Vous êtes mort !")
            combat = 0
        else:
            print("Votre adversaire est mort !")
            Score(Joueur1,compteurs_tours)
            combat = 0

if __name__ == '__main__':
    main()