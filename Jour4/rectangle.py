class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur
    
    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur


# Instanciation de la classe Rectangle
mon_rectangle = Rectangle(5, 3)

# Affichage du périmètre et de la surface
print(f"Le périmètre du rectangle")

# Affichage du périmètre et de la surface
print(f"Le périmètre du rectangle est : {mon_rectangle.perimetre()} unités.")
print(f"La surface du rectangle est : {mon_rectangle.surface()} unités carrées.")

# Modification des dimensions du rectangle
mon_rectangle.set_longueur(7)
mon_rectangle.set_largeur(4)

# Affichage des nouvelles dimensions, du périmètre et de la surface mis à jour
print(f"Nouvelle longueur : {mon_rectangle.get_longueur()} cm.")
print(f"Nouvelle largeur : {mon_rectangle.get_largeur()} cm.")
print(f"Nouveau périmètre : {mon_rectangle.perimetre()} cm.")
print(f"Nouvelle surface : {mon_rectangle.surface()} centimètres carrées.")

# Instanciation de la classe Parallelepipede
mon_parallelepipede = Parallelepipede(5, 3, 10)

# Affichage du volume
print(f"Le volume du parallélépipède est : {mon_parallelepipede.volume()} unités cubes.")

