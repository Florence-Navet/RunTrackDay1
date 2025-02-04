class Commande:
    def __init__(self, numéro_commande):
         self.__numero_commande = numéro_commande
         self.__plat_commandes = []
         self.__statut = "en cours"

    def ajouter_plats(self, nom_plat, prix):
         if self.__statut == "en cours":
             