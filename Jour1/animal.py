class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom
        print(f"Le nom de l'animal est maintenant : { self.prenom}.")


# Instanciation d'un objet Animal
mon_animal = Animal()

# Affichage de l'âge initial de l'animal
print(f"L'âge de l'animal est : {mon_animal.age} ans")

# Vieillissement de l'animal
mon_animal.vieillir()  

# Affichage de l'âge après vieillissement
print(f"Après avoir vieilli, l'âge de l'animal est : {mon_animal.age} ans")

#Attribution d'un nom à l'animal
mon_animal.nommer("Saya")



    