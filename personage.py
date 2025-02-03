class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        if self.x > 0:
            self.x -= 1
        else:
            print("Déplacement invalide : bord gauche atteint.")

    def droite(self, largeur_plateau):
        if self.x < largeur_plateau - 1:
            self.x += 1
        else:
            print("Déplacement invalide : bord droit atteint.")

    def haut(self):
        if self.y > 0:
            self.y -= 1
        else:
            print("Déplacement invalide : bord supérieur atteint.")

    def bas(self, hauteur_plateau):
        if self.y < hauteur_plateau - 1:
            self.y += 1
        else:
            print("Déplacement invalide : bord inférieur atteint.")

    def position(self):
        return (self.x, self.y)

def afficher_plateau(largeur, hauteur, personnage):
    for y in range(hauteur):
        for x in range(largeur):
            if x == personnage.x and y == personnage.y:
                print("P", end=" ")  # 'P' représente le personnage
            else:
                print(".", end=" ")  # '.' représente une case vide
        print()  # Nouvelle ligne à la fin de chaque rangée

# Dimensions du plateau de jeu
largeur_plateau = 5
hauteur_plateau = 5

# Création d'un personnage à la position initiale (2, 2)
personnage = Personnage(2, 2)

# Affichage de la position initiale
print("Position initiale du personnage :", personnage.position())
afficher_plateau(largeur_plateau, hauteur_plateau, personnage)

# Déplacements du personnage
personnage.gauche()
personnage.haut()
personnage.gauche()

# Affichage après déplacements
print("\nPosition après déplacements :", personnage.position())
afficher_plateau(largeur_plateau, hauteur_plateau, personnage)
