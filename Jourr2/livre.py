class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True

    # Accesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    # Mutateurs (setters)
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur : le nombre de pages doit être un nombre entier positif.")

    def verifier_disponibilité(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verifier_disponibilité():
            self.__disponible = False
            print(f"Le Livre {self.get_titre()} a été emprunté.")
        else:
            print(f"Le livre {self.get_titre()} n'est pas  disponible.")

    def rendre(self):
        if not self.verifier_disponibilité():
            self.__disponible = True
            print(f"Le livre '{self.get_titre()}' a été rendu.")
        else:
            print(f"Le livre {self.get_titre()} n'a pas été emprunté.")

            

#Creation du livre
mon_livre = Livre("Shadow", "The eminence of Shadow", 200)

#Verifier si livre disponible
if mon_livre.verifier_disponibilité():
    print(f"Le livre {mon_livre.get_titre()} est disponible.")
else:
    print(f"Le livre {mon_livre.get_titre()} n'est pas disponible.")

#Accès aux attirbuts
print(mon_livre.get_titre())
print(mon_livre.get_auteur())
print(mon_livre.get_nombre_pages())

# Modification des attributs
mon_livre.set_titre("Harry Potter")
mon_livre.set_auteur("J.K. Rowling")
mon_livre.set_nombre_pages(400)

# Affichage après modification
print(mon_livre.get_titre()) 
print(mon_livre.get_auteur())
print(mon_livre.get_nombre_pages())


#Emprunt du livre
mon_livre.emprunter()

#rendre le livre
mon_livre.rendre()

#Tentative d'emprunt d'un livre emprunt
mon_livre.emprunter()

# Tentative de rendre un livre qui n'a pas été emprunté
mon_livre.rendre()

