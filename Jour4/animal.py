class Animal:
    def __init__(self, nom):
        self.nom = nom

    def move(self):
        print(f"{self.nom} se deplace")

class Chien(Animal):
    def __init__(self, nom, race):
        super().__init__(nom)
        self.race = race

    def move(self):
        print(f"Le chien {self.nom} court !")

    def cri_chien(self):
        print("Le chien aboie")

    

class Oiseau(Animal):
    def __init__(self, nom, race, couleur, ailes=2):
        super().__init__(nom)
        self.race = race
        self.couleur = couleur
        self.ailes = ailes


    def move(self):
        print(f"L'oiseau {self.nom} vole !")

    
class Perroquet (Oiseau):
    def __init__(self, nom, race, couleur):
        super().__init__(nom, race, couleur, 4)




un_oiseau = Oiseau("Coco", "Perroquet", "Bleu")
un_chien = Chien("Saya", "Berger australien")
un_perroquet = Perroquet("Kiki", "perroquet", "Multicolore")

un_oiseau.move()
un_chien.move()
un_chien.cri_chien()

un_perroquet.move()

print(un_perroquet.ailes)
        
