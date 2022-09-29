from random import randint, choice, random
from time import sleep
import os

class Monde:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [["_" for _ in range(largeur)] for _ in range(hauteur)]

    def __del__(self):
        pass
    
    def afficher_monde(self):
        for ligne in self.grille:
            print(ligne)
            """for case in ligne:
                print(case)"""

    def peupler(self, nb_poisson:int, nb_requin:int):
        """Méthode pour initialiser la position des thon et des requins
        :param nb_poisson: Nombre de poisson à afficher dans la grille
        :param nb_requin: Nombre de requin à afficher dans la grille
        """
        
        for _ in range(nb_poisson): # Itère tout les poissons

            while True:

                x_random = randint(0, self.largeur - 1)
                y_random = randint(0, self.hauteur - 1)

                if self.grille[y_random][x_random] == "_" :
                    self.grille[y_random][x_random] = Poisson(x_random, y_random)
                    break



        for _ in range(nb_requin):  # Itère tout les requins

            while True:

                x_random = randint(0, self.largeur - 1)
                y_random = randint(0, self.hauteur - 1)

                if self.grille[y_random][x_random] == "_" :
                    self.grille[y_random][x_random] = Requin(x_random, y_random)
                    break
            

            
    
    def jouer_un_tour(self):
        pass


class Poisson:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.compteur_repro = 0
    
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
        self.energie = 6


    
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

monde = Monde(10, 8)
monde.afficher_monde()
monde.peupler(1, 1)
monde.afficher_monde()