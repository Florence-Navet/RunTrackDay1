class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficher_age(self):
        print(f"Âge : {self.age}")

    def bonjour(self):
        print("Hello")

    def modifier_age(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours")

    def afficher_age(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age=14, matiere_enseignee=""):
        super().__init__(age)
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer")

# Instanciation d'une Personne et d'un Élève
personne1 = Personne()
eleve1 = Eleve()

#objet professeur
profMaths = Professeur("Kim Tae Young", 40)

#eleve disant bonjour
eleve1.bonjour()

#elve disant je vais en cours
eleve1.aller_en_cours()

# Affichage de l'âge par défaut de l'élève
eleve1.afficher_age()

#redefinir l'age
eleve1.modifier_age(15)
eleve1.afficher_age()

#professeur dis  bonjour
profMaths.bonjour()

#commencer le cours
profMaths.enseigner()
