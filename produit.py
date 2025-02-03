class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Produit: {self.nom}, \nPrix HT: {self.prixHT:.2f} €, \nTVA: {self.TVA}%,\nPrix TTC: {self.CalculerPrixTTC():.2f} €\n"

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def get_nom(self):
        return self.nom

    def get_prixHT(self):
        return self.prixHT

    def get_TVA(self):
        return self.TVA


# Création de plusieurs produits
produit1 = Produit("Commode", 150, 20)
produit2 = Produit("Bureau", 120, 20)
produit3 = Produit("Téléphone", 380, 20)

# Affichage des informations des produits
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Modification du nom et du prix des produits
produit1.modifier_nom("Lit")
produit1.modifier_prix(400)

produit2.modifier_nom("Café")
produit2.modifier_prix(1.5)

produit3.modifier_nom("voiture")
produit3.modifier_prix(5000)

# Affichage des nouvelles informations des produits
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())
