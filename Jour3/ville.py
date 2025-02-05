class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def ajouter_habitant(self):
        self.__nombre_habitants += 1

    def retirer_habitant(self):
        if self.__nombre_habitants > 0:
            self.__nombre_habitants -= 1
        else:
            print("Le nombre d'habitants ne peut pas être négatif.")


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville

    def emmenager(self):
        self.__ville.ajouter_habitant()

    def demenager(self):
        self.__ville.retirer_habitant()


# Création des objets Ville
Seoul = Ville("Seoul", 10206972)
Lawless_city = Ville("Lawless City", 1000000)
Marseille = Ville("Marseille", 877215)
Paris = Ville("Paris", 2113705)

# Affichage du nombre d'habitants initial
print(f"Nombre d'habitants à {Seoul.get_nom()} : {Seoul.get_nombre_habitants()}")
print(f"Nombre d'habitants à {Lawless_city.get_nom()} : {Lawless_city.get_nombre_habitants()}")
print(f"Nombre d'habitants à {Marseille.get_nom()} : {Marseille.get_nombre_habitants()}")
print(f"Nombre d'habitants à {Paris.get_nom()} : {Paris.get_nombre_habitants()}")

# Création des objets Personne
john = Personne("John", 45, Paris)  # Lier John à Paris
myrtille = Personne("Myrtille", 4, Paris)  # Lier Myrtille à Paris
chloe = Personne("Chloé", 18, Marseille)  # Lier Chloé à Marseille

# Les personnes emménagent dans leur ville
john.emmenager()
myrtille.emmenager()
chloe.emmenager()

# Affichage du nombre d'habitants après l'arrivée des nouveaux
print(f"Nombre d'habitants à {Paris.get_nom()} après l'arrivée de nouvelles personnes : {Paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {Marseille.get_nom()} après l'arrivée de nouvelles personnes : {Marseille.get_nombre_habitants()}")

# Déménagement
john.demenager()
myrtille.demenager()
chloe.demenager()

# Affichage après déménagement
print(f"Nombre d'habitants à {Paris.get_nom()} après le départ de John : {Paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {Marseille.get_nom()} après le départ de Chloé : {Marseille.get_nombre_habitants()}")

# Emménagement à Lawless City
john.emmenager()
myrtille.emmenager()
chloe.emmenager()

# Affichage du nombre d'habitants à Lawless City après l'arrivée des nouvelles personnes
print(f"Nombre d'habitants à {Lawless_city.get_nom()} après l'arrivée de nouvelles personnes : {Lawless_city.get_nombre_habitants()}")
