class Commande:

    def __init__(self, numero_commande, catalogue_plats, taux_tva=20):
        self.__numero_commande = numero_commande
        self.__plats_commandes = []
        self.__statut = "en cours"
        self.__taux_tva = taux_tva
        self.__catalogue_plats = catalogue_plats

    def ajouter_plat(self, nom_plat):
        if nom_plat in self.__catalogue_plats:
            prix = self.__catalogue_plats[nom_plat]
            plat = {'nom': nom_plat, 'prix': prix}
            self.__plats_commandes.append(plat)
        else:
            print(f"Le plat '{nom_plat}' n'est pas disponible dans le catalogue.")

    def annuler_commande(self):
        if self.__statut == "en cours":
            self.__statut = "annulée"
            self.__plats_commandes = []
        else:
            print("La commande ne peut pas être annulée car elle est déjà terminée ou annulée.")
        return self.__statut

    def terminer_commande(self):
        if self.__statut == "en cours":
            self.__statut = "terminée"
        else:
            print("La commande ne peut pas être terminée car elle est déjà terminée ou annulée.")

    def calculer_total(self):
        total = 0
        for plat in self.__plats_commandes:
            total += plat["prix"]
            return total

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande} - Statut : {self.__statut}")
        for plat in self.__plats_commandes:
            print(f"- {plat['nom']}: {plat['prix']}€")
        total = self.calculer_total()
        tva = self.calculer_tva()
        print(f"Total à payer : {total}€")
        print(f"TVA ({self.__taux_tva}%) : {tva}€")
        print(f"Montant TTC : {total + tva}€")



    def calculer_tva(self):
        total = self.calculer_total()
        tva = total * self.__taux_tva / 100
        return tva

    def modifier_taux_tva(self, nouveau_taux):
        self.__taux_tva = nouveau_taux
        print(f"Taux de TVA modifié à {nouveau_taux}%")
    
    def get_status(self):
        return self.__statut


def main():
    catalogue_plats = {
        "Pizza": 15.6,
        "Ramen au poulet": 13.0,
        "Hamburger": 9.0,
        "Tacos": 17.5,
        "nem": 5.0
    }

    une_commande = Commande(123, catalogue_plats, taux_tva=30)

    une_commande.ajouter_plat("Pizza")
    une_commande.ajouter_plat("Tacos")
    print(une_commande.get_status())
    une_commande.terminer_commande()
    print(une_commande.get_status())


    une_commande.afficher_commande()


 

if __name__ == "__main__":
    main()
