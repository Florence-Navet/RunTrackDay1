class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description  # Correction ici
        self.statut = "à faire"

    def __str__(self):
        return f'Titre: {self.titre}, Description: {self.description}, Statut: {self.statut}'


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        if tache not in self.taches:
            self.taches.append(tache)

    def supprimer_tache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"La tâche '{tache.titre}' est terminée.")
        else:
            print("La tâche n'existe pas dans la liste.")

    def afficher_liste(self):
        if not self.taches:
            print("Aucune tâche dans la liste.")
        else:
            for tache in self.taches:
                print(tache)
                print("-" * 20)

# Création de la liste de tâches
liste = ListeDeTaches()

# Création des tâches
tache1 = Tache("Finir le Job 3", "Pour faire le Job 4")
tache2 = Tache("Faire mon linge", "Allez au lavomatique")
tache3 = Tache("Regarder un drama", "Yong Pal")
tache4 = Tache("Appelez Kevin", "Pour ce week-end")
tache5 = Tache("Soutenance", "Faire la révision")

# Ajout des tâches dans la liste
liste.ajouter_tache(tache1)
liste.ajouter_tache(tache2)
liste.ajouter_tache(tache3)
liste.ajouter_tache(tache4)
liste.ajouter_tache(tache5)

# Affichage des tâches
print("Toutes les tâches :")
liste.afficher_liste()
