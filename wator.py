from random import randint, choice
from time import sleep
import os

class Monde:

    def __init__(self, largeur:int, hauteur:int):
        """
        Initialise le monde
        :param largeur: Le nombre de colonnes souhaité
        :param hauteur: Le nombre de lignes souhaité
        """

        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [["_" for _ in range(largeur)] for _ in range(hauteur)]
        #self.liste_poissons = []


    def __del__(self):
        pass
    
    def afficher_monde(self):
        """Méthode pour afficher le monde, qui affichera un P ou un R dans la grille à l'emplacement des Poissons et des Requins"""

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
        """
        Méthode pour définir la position des thon et des requins aléatoirement
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
        """Créer les liste de poissons et de requins qui doivent jouer, puis leur fais jouer un tour"""

        liste_poissons = []
        liste_requins = []

        for ligne in self.grille:
            for case in ligne:
                if isinstance(case, Poisson):
                    liste_poissons.append(case)
                if isinstance(case, Requin):
                    liste_requins.append(case)

        for poisson in liste_poissons:
            poisson.vivre_une_journee(self)

        for requin in liste_requins:
            requin.vivre_une_journee(self)

        print(liste_poissons)
        print(liste_requins)


class Poisson:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.compteur_repro = 0
    
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

        if monde.grille[(self.y + 1) % monde.hauteur][self.x] == "P":
            list.append((self.x, (self.y + 1 ) % monde.hauteur))

        if monde.grille[(self.y - 1) % monde.hauteur][self.x] == "P":
            list.append((self.x, (self.y - 1 ) % monde.hauteur))

        if monde.grille[self.y][(self.x + 1) % monde.largeur] == "P" :
            list.append(((self.x + 1) % monde.largeur, self.y))

        if monde.grille[self.y][(self.x - 1) % monde.largeur] == "P" :
            list.append(((self.x + 1) % monde.largeur, self.y))

        return list
    
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
        self.compteur_repro = 0
        self.energie = 6


    
    def deplacement_possible(self, monde):
        list = []

        """ verifie si il y a un poisson dans une case. self.y pour la hauteur (haut bas), self.x pour la largeur(gauche droite) """
        if isinstance(monde.grille[(self.y + 1) % monde.hauteur][self.x], Poisson):
            list.append((self.x, (self.y + 1 ) % monde.hauteur))
            return list
        elif isinstance(monde.grille[(self.y - 1) % monde.hauteur][self.x], Poisson):
            list.append((self.x, (self.y - 1 ) % monde.hauteur))
            return list
        elif isinstance(monde.grille[self.y][(self.x + 1) % monde.largeur], Poisson):
            list.append(((self.x + 1) % monde.largeur, self.y))
            return list
        elif isinstance(monde.grille[self.y][(self.x - 1) % monde.largeur], Poisson):
            list.append(((self.x + 1) % monde.largeur, self.y))
            return list
        else :
            """ verification des déplacement possible. self.y pour la hauteur (haut bas), self.x pour la largeur(gauche droite) """
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
        coups_possible = self.deplacement_possible(monde)
        if len(coups_possible) != 0 :
            coup_a_jouer = choice(coups_possible)
            x_coup = coup_a_jouer[0]
            y_coup = coup_a_jouer[1]

            x_preced = self.x
            y_preced = self.y

            self.x = x_coup
            self.y = y_coup
            monde.grille[y_coup][x_coup] = self

            if self.compteur_repro >= 8 :
                monde.grille[y_preced][x_preced] = Requin(x_preced, y_preced)
            else :
                monde.grille[y_preced][x_preced] = "_"

        return coup_a_jouer
        
    def vivre_une_journee(self, monde):
        self.compteur_repro += 1
        self.se_deplacer(monde)



monde = Monde(10, 8)
monde.peupler(3, 2)
monde.afficher_monde()


"""for ligne in monde.grille :
    for case in ligne :
        if isinstance(case, Requin) :
            print(case.deplacement_possible(monde))
            #print(case.se_deplacer(monde))
            case.se_deplacer(monde)"""
print("------------------")
monde.jouer_un_tour()
monde.afficher_monde()