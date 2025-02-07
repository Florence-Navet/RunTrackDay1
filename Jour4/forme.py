class Forme:

    def aire(self):
        return 0

class Rectangle(Forme):
    
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur
    
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        return 3.14 * self.radius ** 2
    
    
    

#creation d'un rectangle
rectangle = Rectangle(10, 20)
cercle = Cercle(10)

#Affichage aire du rectangle
print(f"L'aire du rectangle est {rectangle.aire()}")
print(f"L'aire du cercle est : {cercle.aire():.2f}")