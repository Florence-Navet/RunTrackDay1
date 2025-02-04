import random

class Commande:
    numero_id = random.randrange(0, 100)

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

    def modifier_numero_commande(self, nouvel_id):
        self.__numero_commande += nouvel_id

    def calculer_total(self):
        total = 0
        for plat in self.__plats_commandes:
            total += plat['prix']
        return total

    def calculer_tva(self):
        total = self.calculer_total()
        tva = total * self.__taux_tva / 100
        return tva

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande} - Statut : {self.__statut}")
        for plat in self.__plats_commandes:
            print(f"- {plat['nom']}: {plat['prix']}€")
        total = self.calculer_total()
        tva = self.calculer_tva()
        print(f"Total à payer : {total}€")
        print(f"TVA ({self.__taux_tva}%) : {tva}€")
        print(f"Montant TTC : {total + tva}€")

    def modifier_taux_tva(self, nouveau_taux):
        self.__taux_tva = nouveau_taux
        print(f"Taux de TVA modifié à {nouveau_taux}%")


def main():
    catalogue_plats = {
        "Pizza": 15.6,
        "Ramen au poulet": 13.0,
        "Hamburger": 9.0,
        "Tacos": 17.5,
        "nem": 5.0
    }

    commande1 = Commande(1, catalogue_plats, taux_tva=10)
    commande2 = Commande(2, catalogue_plats, taux_tva=20)
    commande3 = Commande(3, catalogue_plats, taux_tva=30)

    commande1.ajouter_plat("Pizza")
    commande1.ajouter_plat("Ramen au poulet")
    commande2.ajouter_plat("Tacos")
    commande2.ajouter_plat("nem")
    commande3.ajouter_plat("couscous royal")

    commande1.afficher_commande()
    print("==================================")
    commande2.afficher_commande()

    commande2.annuler_commande()
    print("==================================")
    commande2.afficher_commande()
    print("==================================")

    commande1.terminer_commande()
    commande1.afficher_commande()
    print("==================================")
    commande3.afficher_commande()
    print("==================================")
    commande3.afficher_commande()


if __name__ == "__main__":
    main()
