from random import randint, choice
from time import sleep
import os

class Monde:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [["_" for _ in range(largeur)] for _ in range(hauteur)]
    
    def afficher_monde(self):
        for ligne in self.grille:
            print(ligne)
            """for case in ligne:
                print(case)"""

    def peupler(self, nb_poisson, nb_requin):
        pass
    
    def jouer_un_tour(self):
        pass


class Poisson:
    def __init__(self, x, y):
        pass
    
    def deplacement_possible(self, monde):
        pass
    
    def se_deplacer(self, monde):
        pass
        
    def vivre_une_journee(self, monde):
        pass

class Requin:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.requin_repro = 0
        self.energie = 5

    
    def deplacement_possible(self, monde):
        list = [(self.y + 1, self.x), (self.y - 1, self.x), (self.y, self.x + 1), (self.y, self.x - 1)]
        if monde[self.y + 1][self.x] == "_":
            list.append[[self.y][self.x]]
        if monde[self.y - 1][self.x] == "_":
            list.append[[self.y][self.x]]
        if monde[self.y][self.x + 1] == "_" :
            list.append[[self.y][self.x + 1]]
        if monde[monde[self.y][self.x - 1]] == "_" :
            list.append[[self.y][self.x - 1]]


    def se_deplacer(self, monde):
        pass
        
    def vivre_une_journee(self, monde):
        pass

monde = Monde(10, 15)
monde.afficher_monde()
requin = Requin(2, 5)
print(requin)
