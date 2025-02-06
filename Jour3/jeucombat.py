import random

class Personnage:
    def __init__(self, nom, vie_joueur):
        self.nom = nom
        self.vie_joueur = vie_joueur  # Définition correcte de l'attribut

    def attaquer(self, adversaire, degats):
        try:
            adversaire.vie_joueur -= degats  # Correction ici : vie_joueur au lieu de vie
        except AttributeError:
            print("Erreur : l'adversaire n'a pas d'attribut 'vie_joueur'.")
            return
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts.")
        if adversaire.vie_joueur <= 0:
            adversaire.vie_joueur = 0
            print(f"{adversaire.nom} est vaincu !")

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisir_niveau(self):
        while True:
            try:
                self.niveau = int(input("Choisissez le niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile) : "))
                if self.niveau in [1, 2, 3]:
                    break
                else:
                    print("Veuillez entrer un nombre entre 1 et 3.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")

    def lancer_jeu(self):
        self.choisir_niveau()

        # Définir les points de vie en fonction du niveau de difficulté
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 100
            vie_ennemi = 100
        else:
            vie_joueur = 100
            vie_ennemi = 150

        # Création des personnages
        joueur = Personnage("Shadow", vie_joueur)
        ennemi = Personnage("Diabolos", vie_ennemi)

        print(f"\nLe combat commence entre {joueur.nom} et {ennemi.nom} !\n")

        # Boucle de combat
        tour = 1
        while joueur.vie_joueur > 0 and ennemi.vie_joueur > 0:  # Correction ici
            print(f"--- Tour {tour} ---")
            # Le joueur attaque
            degats_joueur = random.randint(10, 20)
            joueur.attaquer(ennemi, degats_joueur)

            if ennemi.vie_joueur <= 0:
                print(f"{joueur.nom} a gagné le combat !")
                break

            # L'ennemi attaque
            degats_ennemi = random.randint(5, 15)
            ennemi.attaquer(joueur, degats_ennemi)

            if joueur.vie_joueur <= 0:
                print(f"{ennemi.nom} a gagné le combat !")
                break

            print(f"{joueur.nom} : {joueur.vie_joueur} PV restants.")  # Correction ici
            print(f"{ennemi.nom} : {ennemi.vie_joueur} PV restants.\n")  # Correction ici
            tour += 1

def main():
    jeu = Jeu()
    jeu.lancer_jeu()

if __name__ == "__main__":
    main()
