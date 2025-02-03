class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées du point : ({self.x}, {self.y})")



# Création d'un point avec les coordonnées (3, 4)
p = Point(3, 4)

# Affichage des coordonnées du point
p.afficherLesPoints()  