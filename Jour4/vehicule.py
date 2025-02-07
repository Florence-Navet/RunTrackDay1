class Vehicule:
    def __init__(self, marque, modele, année, prix):
        self.marque = marque
        self.modele = modele
        self.année = année
        self.prix = prix
        
        
    def informationsVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Modèle = {self.modele}")
        print(f"Année = {self.année}")
        print(f"Prix = {self.prix}")
        
    def demarrer(self):
        print("Attention, je roule !")
    
    def __str__(self):
        return self.infos()
    

class Voiture(Vehicule):
    def __init__(self, marque, modele, année, prix):
        super().__init__(marque, modele, année, prix)
        self.portes = 4
        
    def informationsVoiture(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.portes}")
        
    def demarrer(self):
        print("Je suis la voiture et démarre !")
        
class Moto(Vehicule):
    def __init__(self, marque, modele, année, prix):
        super().__init__(marque, modele, année, prix)
        self.roues = 2
        
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues = {self.roues}")

        
    def demarrer(self):
        print("Je suis la moto et démarre !")
        
    
        
    
    
    
# Instanciation de la classe Vehicule
voiture = Voiture("Porsche", "911", 2019, 15000)
moto = Moto("Ducati", "Monster", 2018, 10000)

# Affichage des informations des véhicules
print("\nInformations de la voiture :")
voiture.informationsVehicule()

print("\nInformations de la moto :")
moto.informationsVehicule()
        
        
# Démarrer les véhicules
print("\nDémarrage des véhicules :")
voiture.demarrer()
moto.demarrer()
        