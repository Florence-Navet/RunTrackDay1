class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=True):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert  # Si le client a droit à un découvert

    def affichercompte(self):
        """Affiche les informations sur le compte."""
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde} €")

    def afficherSolde(self):
        """Affiche le solde du compte."""
        print(f"Le solde du compte {self.__numero_compte} est de {self.__solde} €.")

    def versement(self, montant):
        """Ajoute un montant au solde du compte."""
        if montant > 0:
            self.__solde += montant
            print(f"Un versement de {montant} € a été effectué sur le compte {self.__numero_compte}.")
        else:
            print("Le montant du versement doit être positif.")

    def retrait(self, montant):
        """Effectue un retrait du compte si le solde est suffisant ou autorisé par le découvert."""
        if montant > 0:
            if self.__solde >= montant or self.__decouvert:
                self.__solde -= montant
                print(f"Un retrait de {montant} € a été effectué sur le compte {self.__numero_compte}.")
            else:
                print("Solde insuffisant. Vous allez être à découvert.")
        else:
            print("Le montant doit être positif.")

    def agios(self):
        if self.__solde < 0:
            agios_applques = self.__solde * 0.10
            self.__solde += agios_applques
            print(f"Des agios de {agios_applques}€ ont été appliqués. Nouveau solde : {self.__solde}€")
        else:
            print("Aucun agio à appliquer. Le solde est positif.")

    def virement(self, compte_destinaire, montant):
        if montant > 0 and self.__solde >= montant:
            compte_destinaire.versement(montant)
            print(f"Un virement de {montant}€ effectué vers le compte {compte_destinaire.get_nom()}")
        print("Erreur: Virement impossible, montant invalide ou solde insuffisant.")
    
    def get_solde(self):
        return self.__solde
    
    def get_nom(self):
        return self.__nom

# Création d'un compte bancaire
compte1 = CompteBancaire("123456789", "Patenne", "Adeline", 20000.00)
compte2 = CompteBancaire("123456789", "Patenne", "Thomas", 400.00)

# Affichage du solde du compte
compte1.affichercompte()
print("")
# Afficher solde du compte
compte1.afficherSolde()
print("")
# Versement de 720€
compte1.versement(720)
print("")
# Affichage du solde après le versement
compte1.afficherSolde()
print("")
# Retrait de 200€
compte1.retrait(200)
print("")
# Affichage du compte après retrait
compte1.afficherSolde()
print("")
# Tentative de retrait de 2000 € (fonds insuffisants)
compte1.retrait(2000)
print("")
# Affichage du compte après retrait
compte1.afficherSolde()
print("")
#aafficher compte thomas
compte2.affichercompte()
print("")
#de 500€ de thomas
compte2.retrait(500)
print("")
compte2.affichercompte()
compte2.afficherSolde()
compte2.agios()

#virement entre les deux comptes
compte1.virement(compte2, 700)

#affichage des soldes après opérations
compte1.afficherSolde()
compte2.afficherSolde()