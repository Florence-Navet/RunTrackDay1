class Produit():
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVT = TVA

    def caculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def afficher(self):
        return f"Produit: {self.nom}, Prix HT: {self.prixHT:.2f} €, TVA: {self.TVA}%, Prix TTC: {self.CalculerPrixTTC():.2f} €"
    