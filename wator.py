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

            for case in ligne:

                if isinstance(case, Poisson):
                    print("P", end=" | ")
                elif isinstance(case, Requin):
                    print("R", end=" | ")
                else:
                    print ("_", end=" | ")

            print("\n")


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
        coups_possibles = self.deplacement_possible(monde)
        if len(coups_possibles) != 0:
            coup_a_jouer = choice(coups_possibles)
            print(coup_a_jouer)
            x_coup = coup_a_jouer[0]
            y_coup = coup_a_jouer[1]

            x_preced = self.x
            y_preced = self.y

            self.x = x_coup
            self.y = y_coup
            monde.grille[y_coup][x_coup] = self

            if self.compteur_repro >= 5:
                monde.grille[y_preced][x_preced] = Poisson(x_preced, y_preced)
                self.compteur_repro = 0
            else:
                monde.grille[y_preced][x_preced] = "_"
        
    def vivre_une_journee(self, monde):
        self.compteur_repro += 1
        self.se_deplacer(monde)

class Requin:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.requin_repro = 0
        self.energie = 6


    
    def deplacement_possible(self, monde):
        list = []
        if monde.grille[(self.y + 1) % monde.hauteur][self.x] == "_":
            list.append((self.x, (self.y + 1 ) % monde.hauteur))

        if monde.grille[(self.y - 1) % monde.hauteur][self.x] == "_":
            list.append((self.x, (self.y - 1 ) % monde.hauteur))

        if monde.grille[self.y][(self.x + 1) % monde.largeur] == "_" :
            list.append(((self.x + 1) % monde.largeur, self.y))

        if monde.grille[self.y][(self.x - 1) % monde.largeur] == "_" :
            list.append(((self.x + 1) % monde.largeur, self.y))

        return list

    def se_deplacer(self, monde):
        pass
        
    def vivre_une_journee(self, monde):
        pass



monde = Monde(10, 8)
monde.peupler(1, 1)
monde.afficher_monde()

for ligne in monde.grille :
    for case in ligne :
        if isinstance(case, Requin) :
            print(case.deplacement_possible(monde))