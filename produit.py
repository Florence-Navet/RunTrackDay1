class Produit:
    def __init__(self, nom, prixHT, TVA):
        """Initialise un produit avec son nom, son prix hors taxes et son taux de TVA."""
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        """Calcule et retourne le prix TTC du produit."""
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        """Retourne une chaîne de caractères avec les informations du produit."""
        return f"Produit: {self.nom}, Prix HT: {self.prixHT:.2f} €, TVA: {self.TVA}%, Prix TTC: {self.CalculerPrixTTC():.2f} €"

    def modifier_nom(self, nouveau_nom):
        """Modifie le nom du produit."""
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prixHT):
        """Modifie le prix HT du produit."""
        self.prixHT = nouveau_prixHT

    def get_nom(self):
        """Retourne le nom du produit."""
        return self.nom

    def get_prixHT(self):
        """Retourne le prix HT du produit."""
        return self.prixHT

    def get_TVA(self):
        """Retourne le taux de TVA du produit."""
        return self.TVA


# Création de plusieurs produits
produit1 = Produit("Chaise", 50, 20)
produit2 = Produit("Table", 150, 20)

# Affichage des informations des produits
print(produit1.afficher())
print(produit2.afficher())

# Modification du nom et du prix des produits
produit1.modifier_nom("Fauteuil")
produit1.modifier_prix(70)

produit2.modifier_nom("Bureau")
produit2.modifier_prix(200)

# Affichage des nouvelles informations des produits
print(produit1.afficher())
print(produit2.afficher())
