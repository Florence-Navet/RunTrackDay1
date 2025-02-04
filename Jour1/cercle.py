class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        
    def diametre(self):
        return 2 * self.rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def circonference(self):
        return 2 * self.rayon * 3.14
    
    def aire(self):
        return self.rayon ** 2 * 3.14

    def afficherInfos(self):
        print(f"Cercle de rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")

    
#creation des cercles
cercle1 = Cercle(4)
cercle2 = Cercle(7)
cercle3 = Cercle(12)

#affichages des infos pour chaque cercle
print("Informations pour le cercle 1:")
cercle1.afficherInfos()

print("\nInformations pour le cercle 2:")
cercle2.afficherInfos()

print("\nInformations pour le cercle 3:")
cercle3.afficherInfos()