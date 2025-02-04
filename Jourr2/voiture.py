class Voiture:
    def __init__(self, marque, modele, annee, kilometre, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometre = kilometre
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    # Accesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometre(self):
        return self.__kilometre

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometre(self, kilometre):
        self.__kilometre = kilometre

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def set_reservoir(self, reservoir):
        if reservoir >= 0:
            self.__reservoir = reservoir
        else:
            print("Erreur : le réservoir ne peut pas être négatif.")

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer : le réservoir est trop bas.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

    def __verifier_plein(self):
        return self.__reservoir > 5

# Création d'une instance de la classe Voiture
ma_voiture = Voiture(marque="Porsche", modele="911 Turbo S", annee=2017, kilometre=30000)

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()

# Affichage des informations de la voiture
print(f"Marque : {ma_voiture.get_marque()}")
print(f"Modèle : {ma_voiture.get_modele()}")
print(f"Année : {ma_voiture.get_annee()}")
print(f"Kilométrage : {ma_voiture.get_kilometre()} km")
print(f"Réservoir : {ma_voiture.get_reservoir()} litres")

