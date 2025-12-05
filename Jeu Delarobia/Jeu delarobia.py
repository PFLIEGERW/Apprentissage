#!/usr/bin/env python3

from random import randrange
from math import ceil


# Classe qui gère le jeu
class Casino(object):
    """
    Classe de gestion du jeu
    methodes setresult() qui permet de lancer la bille
    set_numero_pari() qui pemret de tester le nombre parié
    set_mise() qui permet de tester la mise
    gains() qui permet de calculer les gains et d'afficher le message au joueur
    """
    numero_pari = 0
    mise_jeu = 0
    # instanciation du résultat
    def __init__(self):
        self.result = self.setresult()

    # méthode de création de résultat
    @staticmethod
    def setresult():
        return randrange(0, 50)

    # methode d'instanciation pour le numéro parié
    def set_numero_pari(self, pari):
        atester = Croupier.isnumber(pari, "Veuillez noter nombre correct : ")
        if atester > 49:
            raise ValueError("Vous ne pouvez parier que des nombres entre 0 et 49 !")
        else:
            self.numero_pari = atester

    # méthode d'instanciation de la mise
    def set_mise(self, mise, argent_joueur):
        atester = Croupier.isnumber(mise, "Veuillez noter un mise : ")
        if atester:
            if atester > argent_joueur:
                raise ValueError("Vous n'avez pas cet argent, vous disposez de %s $" % argent_joueur)
            else:
                self.mise_jeu = atester
        else:
            raise ValueError("Vous n'avez pas rentré un nombre pour votre mise")

    # définition des gains et affichage des messages au joueur
    def gains(self):
        tgains = 0
        if self.numero_pari == self.result:
            tgains += self.mise_jeu * 3 + self.mise_jeu
            Croupier.say("Bravo tu as gagné %s $" % tgains)
        else:
            if Croupier.iseven(self.result) and Croupier.iseven(self.numero_pari):
                tgains += ceil(self.mise_jeu / 2) + self.mise_jeu
                Croupier.say("Bravo tu as gagné %s $" % tgains)
            else:
                tgains -= self.mise_jeu
                Croupier.say("Oh non tu as perdu %s $" % (tgains * -1))
        return tgains


# classe qui gère le joueur et l'argent total
class Joueur(object):
    # instanciation du joueur avec un nom et une somme d'entrée
    def __init__(self, nom, argent):
        self.nom = nom
        self.set_argent(argent)

    # méthode de verification de saisie
    def set_argent(self, argent):
        atester = Croupier.isnumber(argent, "Veuillez noter une somme : ")
        if atester:
            self.argent = atester
        else:
            self.argent = 0

    # méthode de gestion des gains pour le joueur
    def gagner(self, gain):
        self.argent += gain

    # méthode de vérification de solde positif (sortie du jeu en cas d'argent < 1
    def assez_argent(self):
        if self.argent > 0:
            return True
        else:
            Croupier.say("Désolé vous n'avez pas assez d'argent")
            return False

    # méthode d'affichage
    def __str__(self):
        return "Bonjour %s, tu disposes de %s $ pour jouer, amuse toi bien" % (self.nom, self.argent)


# classe de méthodes statiques
class Croupier(object):

    # methode qui "override" un print
    @staticmethod
    def say(prompt):
        print("Croupier :  %s" % prompt)

    # methode qui "overide in input"
    @staticmethod
    def ask(prompt):
        return input(prompt)

    # méthode pour vérifier si un nombre est pair ou impair
    @staticmethod
    def iseven(nbr):
        if nbr % 2:
            return True
        else:
            return False

    # méthode qui teste le parse en int et qui boucle tant que ce n'est pas un int
    @staticmethod
    def isnumber(nbr, prompt):
        while not isinstance(nbr, int):
            try:
                nbr = int(nbr)
                return nbr
            except ValueError:
                nbr = False
                Croupier.say("Ce n'est pas un nombre entier !")
                nbr = input(prompt)


# Lancement du jeu
joueur1 = Joueur(Croupier.ask("Veuillez saisir votre nom  : "), Croupier.ask("Veuillez saisir votre solde : "))

continue_jeu = True
jeu = Casino()

while continue_jeu:
    Croupier.say(joueur1)

    try:
        jeu.set_numero_pari(Croupier.ask("Veuillez saisir le numéro parié : "))
        jeu.set_mise(Croupier.ask("Veuillez saisir votre mise : "), joueur1.argent)
        joueur1.gagner(jeu.gains())
        jeu.setresult()
    except ValueError as err:
        Croupier.say(err)

    if Croupier.ask("Voulez vous continuer à jouer ? [ O / N ] : ").lower() == "n":
        continue_jeu = False
    else:
        continue_jeu = joueur1.assez_argent()