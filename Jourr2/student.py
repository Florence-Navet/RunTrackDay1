class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__student_eval()

    def _add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print(f"Erreur: le nombre de crédits doit être un nombre positif.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def student_info(self):
        print(f"Nom: {self.__nom} {self.__prenom}")
        print(f"Numéro d'étudiant: {self.__numero_etudiant}")
        print(f"Total de crédits: {self.__credits}")
        print(f"Niveau: {self.__level}")

# Instanciation de l'objet Student
john_doe = Student("Doe", "John", 145)

# Ajout de crédits
john_doe._add_credits(51) 
john_doe._add_credits(20)  
john_doe._add_credits(10)  

# Affichage des informations de l'étudiant
john_doe.student_info()
