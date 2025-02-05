class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"

    def marquer_comme_terminee(self):
        self.statut = "terminée"

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
            print(f"La tâche '{tache.titre}' est supprimée.")
        else:
            print("La tâche n'existe pas dans la liste.")

    def marquer_comme_terminee(self, tache):
        if tache in self.taches:
            tache.marquer_comme_terminee()
            print(f"La tâche '{tache.titre}' est marquée comme terminée.")
        else:
            print("La tâche n'existe pas dans la liste.")

    def afficher_liste_taches(self):
        if not self.taches:
            print("Aucune tâche dans la liste.")
        else:
            for tache in self.taches:
                statut = "[x]" if tache.statut == "terminée" else "[ ]"
                print(f"{statut} {tache.titre} → {tache.description}")



# Création de la liste de tâches
liste = ListeDeTaches()

# Création des tâches
tache1 = Tache("Finir le Job 3", "Pour faire le Job 4")
tache2 = Tache("Faire mon linge", "Aller au lavomatique")
tache3 = Tache("Regarder un drama", "Yong Pal")
tache4 = Tache("Appeler Kevin", "Pour ce week-end")
tache5 = Tache("Soutenance", "Faire la révision")

# Ajout des tâches dans la liste
liste.ajouter_tache(tache1)
liste.ajouter_tache(tache2)
liste.ajouter_tache(tache3)
liste.ajouter_tache(tache4)
liste.ajouter_tache(tache5)

# Affichage des tâches
print("Toutes les tâches :")
liste.afficher_liste_taches()
print("")



# Marquer la première tâche comme terminée
tache1.marquer_comme_terminee()

# Afficher la liste des tâches
liste.afficher_liste_taches()



