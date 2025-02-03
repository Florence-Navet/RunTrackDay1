class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}."

# Instanciation de plusieurs personnes
personne1 = Personne("Patenne", "Adeline")
personne2 = Personne("Navet", "Florence")
personne3 = Personne("Mangeot", "Jolyne")

# Appel de la méthode se_presenter pour chaque personne
print(personne1.se_presenter())
print(personne2.se_presenter())
print(personne3.se_presenter())
