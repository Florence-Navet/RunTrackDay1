class Forme:

    def aire(self):
        return 0

class Rectangle(Forme):
    
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur
    
    
    

#creation d'un rectangle
rectangle = Rectangle(10, 20)

#Affichage aire du rectangle
print(f"L'aire du rectangle est {rectangle.aire()}")
    