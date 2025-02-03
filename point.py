class Point:
    def __init__(self, x, y):
        """Initialise les coordonnées du point."""
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        """Affiche les coordonnées du point."""
        print(f"Les coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        """Affiche la coordonnée x."""
        print(f"Les coordonnées x : {self.x}")
    
    def afficherY(self):
        """Affiche la coordonnée y."""
        print(f"Les coordonnées y : {self.y}")

    def changeX(self, nouvelle_x):
        """Change la valeur de la coordonnée x."""
        self.x = nouvelle_x
        # print(f"Les coordonnées x : {self.x}")

    def changeY(self, nouvelle_y):
        """Change la valeur de la coordonnée y."""
        self.y = nouvelle_y 
        # print(f"Les coordonnées y : {self.y}")

# Création d'un point avec les coordonnées (3, 4)
p = Point(3, 4)

# Affichage des coordonnées du point
p.afficherLesPoints()  

# Affichage de la coordonnée X
p.afficherX()

# Affichage de la coordonnée Y
p.afficherY()

# Changement de la coordonnée X
p.changeX(5)
p.afficherX()

# Changement de la coordonnée Y
p.changeY(9)
p.afficherY()
