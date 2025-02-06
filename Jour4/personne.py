class Personne:
    def __init__(self, age=14):
        self.age = age  
        
    def afficherAge(self):
        print(f"Âge : {self.age}")  

    def bonjour(self):
        print("Hello")  

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age  


class Eleve(Personne):  
    def allerEnCours(self):
        self.bonjour()  
        print("Je vais en cours")  

    def afficherAge(self):
        print(f"J’ai {self.age} ans")  


class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age) 
        self.__matiereEnseignee = matiereEnseignee  

    def enseigner(self):
        self.afficherAge() 
        print("Le cours va commencer") 


# Instanciation d'une Personne, d'un Élève et d'un Professeur
personne1 = Personne()
eleve1 = Eleve()
professeur1 = Professeur(40, "Mathématiques")  

# Affichage de l'âge par défaut de l'élève
eleve1.afficherAge()  

# L'élève va en cours
eleve1.allerEnCours()  

# Le professeur enseigne
professeur1.enseigner()  

