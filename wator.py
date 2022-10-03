from random import randint, choice
from time import sleep
from termcolor import colored #pip install termcolor
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
        self.cases = largeur * hauteur

    
    def afficher_monde(self) -> None:
        """Méthode pour afficher le monde, qui affichera un P ou un R dans la grille à l'emplacement des Poissons et des Requins"""

        for ligne in self.grille:
            for case in ligne:

                if isinstance(case, Poisson):
                    print(colored("P", "blue"), end=" | ")

                elif isinstance(case, Requin):
                    print(colored("R", "red"), end=" | ")

                else:
                    print ("_", end=" | ")

            print("\n")


    def peupler(self, nb_poisson:int, nb_requin:int) -> None:
        """
        Méthode pour définir la position des thon et des requins aléatoirement
        :param nb_poisson: Nombre de poisson à afficher dans la grille
        :param nb_requin: Nombre de requin à afficher dans la grille
        """
        
        nb_total = nb_poisson + nb_requin

        if nb_total > self.cases:
            print("Trop d'entités")

        else:
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
    

    def jouer_un_tour(self) -> int:
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

        self.afficher_monde()
        print(len(liste_poissons), "poissons restants")
        print(len(liste_requins), "requins restants")

        if len(liste_poissons) == self.cases:
            return 0
        
        else:
            return len(liste_poissons) + len(liste_requins)


class Poisson:
    def __init__(self, x:int, y:int):
        """Initialisation des instances de poisson, avec créations des attributs de position et de reproduction"""
        
        self.x = x
        self.y = y
        self.compteur_repro = 0
    

    def deplacement_possible(self, monde:Monde) -> list:
        """
        Vérification des déplacements possible et renvoi une liste contenant les déplacements
        self.y pour la hauteur (haut bas), self.x pour la largeur(gauche droite)
        :param monde: Grille utilisée
        """

        list = []

        if monde.grille[(self.y + 1) % monde.hauteur][self.x] == "_":
                    list.append((self.x, (self.y + 1 ) % monde.hauteur))

        if monde.grille[(self.y - 1) % monde.hauteur][self.x] == "_":
                    list.append((self.x, (self.y - 1 ) % monde.hauteur))

        if monde.grille[self.y][(self.x + 1) % monde.largeur] == "_" :
                    list.append(((self.x + 1) % monde.largeur, self.y))

        if monde.grille[self.y][(self.x - 1) % monde.largeur] == "_" :
                list.append(((self.x - 1) % monde.largeur, self.y))

        return list
    

    def se_deplacer(self, monde:Monde) -> None:
        """
        Méthode pour gérer les déplacements des poissons, qui récupère la liste des deplacement_possible
        :param monde: Grille utilisée
        """

        coups_possibles = self.deplacement_possible(monde)

        if len(coups_possibles) != 0:

            coup_a_jouer = choice(coups_possibles)  #Choisi aléatoirement un coup parmi la liste coups_possibles
            
            x_coup = coup_a_jouer[0]
            y_coup = coup_a_jouer[1]

            x_preced = self.x
            y_preced = self.y

            self.x = x_coup
            self.y = y_coup
            
            monde.grille[y_coup][x_coup] = self

            if self.compteur_repro >= 4:
                monde.grille[y_preced][x_preced] = Poisson(x_preced, y_preced)
                self.compteur_repro = 0

            else:
                monde.grille[y_preced][x_preced] = "_"


    def vivre_une_journee(self, monde:Monde) -> None:
        """
        Fais vivre une journée au poisson, et lui ajoute +1 à sa reproduction
        :param monde: Grille utilisée
        """

        self.se_deplacer(monde)
        self.compteur_repro += 1


class Requin:

    def __init__(self, x:int, y:int):
        """Initialisation des instances de requin, avec créations des attributs de position, de reproduction et d'énergie"""

        self.x = x
        self.y = y 
        self.requin_repro = 0
        self.energie = 5
    

    def deplacement_possible(self, monde:Monde) -> list:
        """"
        Vérification des déplacements possible et renvoi une liste contenant les déplacements
        self.y pour la hauteur (haut bas), self.x pour la largeur(gauche droite)
        :param monde: Grille utilisée
        """

        list = []

        #Vérifie d'abord s'il y a un poisson à côté de lui

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
            list.append(((self.x - 1) % monde.largeur, self.y))
            return list

        else :
            #S'il n'y a pas de poisson, il vérifie les cases vides autour de lui
            if monde.grille[(self.y + 1) % monde.hauteur][self.x] == "_":
                list.append((self.x, (self.y + 1 ) % monde.hauteur))
            if monde.grille[(self.y - 1) % monde.hauteur][self.x] == "_":
                list.append((self.x, (self.y - 1 ) % monde.hauteur))
            if monde.grille[self.y][(self.x + 1) % monde.largeur] == "_" :
                list.append(((self.x + 1) % monde.largeur, self.y))
            if monde.grille[self.y][(self.x - 1) % monde.largeur] == "_" :
                list.append(((self.x - 1) % monde.largeur, self.y))

            return list


    def se_deplacer(self, monde:Monde) -> None:
        """"
        Vérification des déplacements possible et renvoi une liste contenant les déplacements
        self.y pour la hauteur (haut bas), self.x pour la largeur(gauche droite)
        :param monde: Grille utilisée
        """

        coups_possible = self.deplacement_possible(monde)

        if len(coups_possible) != 0 :

            coups_a_jouer = choice(coups_possible)

            x_coup = coups_a_jouer[0]
            y_coup = coups_a_jouer[1]

            x_preced = self.x
            y_preced = self.y

            self.x = x_coup
            self.y = y_coup

            #Vérifie si le requin a manger un poisson, si oui alors il gagne 1 d'énergie sinon il perd 1 d'énergie
            if isinstance(monde.grille[y_coup][x_coup], Poisson):
                self.energie += 1
            else :
                self.energie -= 1

            monde.grille[y_coup][x_coup] = self

            #Si la reproduction du requin est égale ou superieur à 6, alors il se reproduit dans la case précédente, sinon la case est vide
            if self.requin_repro >= 6 :
                monde.grille[y_preced][x_preced] = Requin(x_preced, y_preced)
                self.requin_repro = 0

            else :
                monde.grille[y_preced][x_preced] = "_"

            #return coups_a_jouer


    def vivre_une_journee(self, monde:Monde) -> None:
        """
        Fais vivre une journée au requin si son énergie est supérieur à 0 et lui ajoute +1 à sa reproduction, sinon on remplace la case par du vide
        :param monde: Grille utilisée
        """

        if self.energie > 0 :
            self.se_deplacer(monde)
            self.requin_repro += 1

        else:
            monde.grille[self.y][self.x] = "_"


monde = Monde(15, 10)
monde.peupler(15, 10)

nb_habitant = 10

while nb_habitant != 0:

    os.system("clear")
    nb_habitant = monde.jouer_un_tour()
    sleep(0.5)