from random import randint, choice
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
        position = randint(self.grille)
        return position
    
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


monde = Monde(10, 8)
monde.afficher_monde()

print(monde.peupler)